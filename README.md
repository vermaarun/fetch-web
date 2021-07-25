Built with ❤️ using Python

A simple command line program that can fetch web pages and saves them to disk for later retrieval and browsing.

## Tech Stack
- Python3
- Redis

## Installation
### To install with Docker
##### Prerequisite
- docker

```
git clone https://github.com/vermaarun/fetch-web.git
cd fetch-web
docker-compose up -d
docker exec -it fetch_web_tool_1 bash
```

## Usage
To download the web page for later use
`./fetch.py url_1 url_2 ... url_n` this command will store the specified web page locally for later use. Example run:
```
./fetch.py https://github.com
```

To check the metadata of fetched web page
`./fetch.py --metadata url` this command will show the metadata for the specified url.
Example metadata:
```
$> ./fetch --metadata https://www.github.com
site: www.github.com
num_links: 115
images: 119
last_fetch: Sat Jul 24 2021 02:57
```

## Run
```
./fetch.py <url1> <url2>...<url3>
./fetch.py --metadata <url>
```