import requests
from bs4 import BeautifulSoup

def main():
    search = input("Enter search term: ")
    params = {"q": search, "oq": search}
    r = requests.get("http://bing.com/search", params=params)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    # Extract the title of the webpage
    results = soup.find("ol", {"id": "b_results"})
    links = results.find_all("li", {"class": "b_algo"})
    for item in links:
        a_tag = item.find("a")
        item_text = a_tag.get_text()
        item_href = a_tag["href"]

        if item_text and item_href:
            print(item_text)
            print(item_href)
            print("Parent: ", item.find("a").parent.parent.find("h2").get_text())
            print("Summary: ", item.find("a").parent.parent.find("p").get_text())
            children = item.find("h2")
            print(children.get_text())
            print("Next Sibling of the h2: ", children.next_sibling)

if __name__ == '__main__':
    main()