import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from urllib.parse import unquote
import json
from datetime import datetime
import os

def main():
    """
    Buscando e salvando imagens do Bing
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    search = input("Enter search term: ")
    searchSanitized = search.replace(" ", "_").lower()
    folder = f"{timestamp}_{searchSanitized}"
    if not os.path.exists(folder):
        os.makedirs(folder)
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
            print(f"Getting: {decoded_url}")
            # pegando a imagem
            try:
                img_obj = requests.get(decoded_url)
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
                    # Verificando se o arquivo já existe
                    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
                    if title:
                        file_path = f"./{folder}/{title}.{img.format}"
                        if os.path.exists(file_path):
                            img.save(f"./{folder}/{title}_{current_time}.{img.format}", img.format)                        
                        else:
                            img.save(f"./{folder}/{title}.{img.format}", img.format)
                    else:
                        img.save(f"./{folder}/{current_time}.{img.format}", img.format)
            except Exception as e:
                print(f"Could not save image: {e}")
    # fazendo a busca ser reiniciada
    main()

if __name__ == '__main__':
    main()