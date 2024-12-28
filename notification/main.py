import requests
from bs4 import BeautifulSoup
from win11toast import toast

def main():
    search = input("Enter search term: ")
    params = {"q": search, "oq": search}
    r = requests.get("http://google.com/search", params=params)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    # Extract the title of the webpage
    title = soup.title.text
    print("Page Title:", title)
    toast("Page Title:", title)
    # print page
    page = soup.prettify()
    with open("search.html", "w+", encoding="utf-8") as index:
        index.write(page)
        index.close()

if __name__ == '__main__':
    main()