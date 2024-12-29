import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from urllib.parse import unquote
import json
from datetime import datetime

def main():
    search = input("Enter search term: ")
    params = {"q": search}
    r = requests.get("http://bing.com/images/search", params=params)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a", {"class": "iusc"})
    for item in links:
        # Acrescentando a url do bing
        href = "http://bing.com"+item.attrs["href"]
        # veriricando se possui o atributo url no href
        if "url=" in href:
            # removendo a partido do url e pegando o 2 item
            split = href.split("url=")[1]
            #  remove o &cdn do fim da url
            split = split.replace("&cdn", "")
            # decodificando a url
            decoded_url = unquote(split)
            print(decoded_url)
            # pegando a imagem
            img_obj = requests.get(decoded_url)
            try:
                img = Image.open(BytesIO(img_obj.content))
                if img:
                    # Pegadno o atributo m que contem todos os dados do arquivo
                    m_attr = item.attrs.get("m")
                    if m_attr:
                        # convertendo o m_attr para json
                        m_data = json.loads(m_attr)
                        #  pegando o valor do atributo t
                        t_value = m_data.get("t")
                        if t_value:
                            # removendo espaços e limitando o tamanho a 10 caracteres
                            title = t_value.replace(" ", "").replace(".","")[:10]
                    if title:
                        img.save(f"./scraped_images/{title}.{img.format}", img.format)
                    else:
                        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                        print(timestamp)
                        img.save(f"./scraped_images/{timestamp}.{img.format}", img.format)
            except Exception as e:
                print(f"Could not save image: {e}")

if __name__ == '__main__':
    main()