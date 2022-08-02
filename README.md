# Web Scraper

A simple python program for scraping images from web pages. It will search a web page based on provided tags and print the image sources to the console.

## Requirements

This program is compatible with Python 3. It requires the following modules:

 * [requests](https://pypi.org/project/requests/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests. 
```bash
pip install requests
```

## Usage

The "web_urls" variable in main.py file contains a list of web pages. This program will scrape images from this list. Modify this list to specify which pages the program needs to scrape from. 
```python
web_urls = [
    'https://www.vecteezy.com/free-photos',
    'https://burst.shopify.com/',
    'https://www.freeimages.com/',
]
```
The "search_tags" variable in main.py file contains a list of tags. This list is used to filter and find only the intended images out of all the images retrieved from a web page. 

```python
search_tags = [
    'squirrel', 'John', 'riding', 'aurora', 'office', 'palm', 'young', 'works', 
]
```
Modify this list to look for the image containing required tag or keyword. Adding an empty string `''` to the list will print out all the image sources.

```python
search_tags = [
    'squirrel', 'John', '', 
]
```

## Running the program

From the project directory run the below command to execute the program 

```bash
python main.py
```