import requests
from bs4 import BeautifulSoup

def main():
    search = input("Enter search term: ")
    params = {"q": search, "oq": search}
    r = requests.get("http://google.com/search", params=params)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    # Extract the title of the webpage
    title = soup.title.text
    print("Page Title:", title)
    links = soup.find_all("a") # Find all elements with the tag <a>
    for link in links:
        print("Link:", link.get("href"), "Text:", link.string)

if __name__ == '__main__':
    main()