#!/usr/bin/env python

import sys
import threading
from urllib.error import URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

import client.redis_client as redis_client


class FetchWeb:
    def __init__(self):
        self.redis_client = redis_client.RedisClient()

    def download_web(self, url_list):
        threads = list()
        for url in url_list:
            t = threading.Thread(target=self.download, args=(url,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()

    def download(self, url):
        try:
            resp = urlopen(url, timeout=30)
            web_content = resp.read()
            page = url.split('//')[1] + ".html"
            with open(page, 'w+b') as fid:
                fid.write(web_content)
            self.set_metadata(url, web_content)
        except URLError as e:
            print("Unable to create connection. Message: %s" % e.reason)
        except Exception as e:
            print("Failed to download the page. Message: %s" % e)

    def set_metadata(self, url, response):
        metadata = {'site': url}
        parser = 'html.parser'
        soup = BeautifulSoup(response, parser)
        metadata['num_links'] = len(soup.find_all('a'))
        metadata['images'] = len(soup.find_all('img'))
        metadata['last_fetch'] = datetime.utcnow().strftime('%a %h %d %Y %H:%M')
        self.redis_client.set(url, metadata)

    def get_metadata(self, url):
        metadata = self.redis_client.get(url)
        if not metadata:
            print("Metadata Not Found.")
        else:
            for k, v in metadata.items():
                print("%s: %s" % (k, v))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage:")
        print("./fetch.py <url> <url>...<url>")
        print("./fetch.py --metadata <url>")
        exit()
    urls = sys.argv[1:]
    try:
        fetchWeb = FetchWeb()
        if urls[0] == "--metadata":
            fetchWeb.get_metadata(urls[1])
        else:
            fetchWeb.download_web(urls)
    except IndexError as ex:
        print("usage:")
        print("./fetch.py <url> <url>...<url>")
        print("./fetch.py --metadata <url>")
    except Exception as ex:
        print("Something is wrong. Message: %s" % ex)
