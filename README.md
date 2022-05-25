Built with ❤️ using Python

A simple command line program that can fetch web pages and saves them to disk for later retrieval and browsing.

Note: All assets are not downloaded so page might not load properly during browsing.    


## Tech Stack
- Python3
- Redis (Used for storing meta data)

## Installation
### To install with Docker
##### Prerequisite
- Docker

```
git clone https://github.com/vermaarun/fetch-web.git
cd fetch-web
docker-compose up -d
docker exec -it fetch_web_tool_1 bash
```

## Usage
1. To download the web page 
```
./fetch.py https://www.github.com
```

2. To check the metadata of fetched web page
```
$> ./fetch.py --metadata https://www.github.com
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
