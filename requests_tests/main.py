import requests
import re

def main():
    searchInGoogle("pizza", "search.html")
    copySite("http://x.com", "x.html")
    searchInSite("http://google.com", "google")

def copySite(url: str = "http://google.com", file: str = "test.html"):
    """
    Copia o conteúdo de um site para um arquivo local.

    Parâmetros:
    url (str): A URL do site que será copiado. Padrão é "http://google.com".
    file (str): O nome do arquivo onde o conteúdo do site será salvo.  Padrão é "test.html".
    """
     
    if(isUrl(url) & isHtml(file)):
        r = requests.get(url)
        print(f"Status {r.status_code}")
        content = r.text
        with open(file, "w+") as html:
            html.write(content)

def searchInSite(url: str = "http://google.com", text: str = "test"):
    """
    Procura um texto específico no conteúdo de uma URL fornecida.
    Args:
        url (str): A URL do site onde será feita a busca. Padrão é "http://google.com".
        text (str): O texto a ser procurado no conteúdo do site. Padrão é "test".
    Retorna:
        Imprime "YES! We have a match!" se o texto for encontrado, caso contrário imprime "No match".
    """

    r = requests.get(url)
    x = re.search(text, r.text)
    if x:
        print("YES! We have a match!")
    else:
        print("No match")
    
def isUrl(url: str) -> bool:
    """
    Verifica se foi fornecida uma URL.
    Args:
        url (str): A URL a ser verificada
    Retorna:
        False: Imprime "URL inválida" se não for uma URL.
        True: Se for uma URL
    """
    # Regex para validar URL
    url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// ou https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domínio...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...ou endereço IP
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...ou endereço IPv6
        r'(?::\d+)?' # porta opcional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    # Verifica se a URL é válida
    if not re.match(url_regex, url):
        print("URL inválida")
        return False
    
    return True
    
def isHtml(file: str) -> bool:
    """
    Verifica se o nome fornecido possui '.html'.
    Args:
        file (str): Nome a ser verificada
    Retorna:
        False: Imprime "Nome de arquivo inválido. Deve ser um arquivo HTML.".
        True: Se possui '.html'
    """
     # Regex para validar arquivo HTML
    file_regex = re.compile(r'^.*\.html?$', re.IGNORECASE)   

    # Verifica se o arquivo é um arquivo HTML
    if not re.match(file_regex, file):
        print("Nome de arquivo inválido. Deve ser um arquivo HTML.")
        return False

    return True

def searchInGoogle(text: str, file: str = "search_google.html"):
    """
    Realiza uma busca no Google e salva o resultado em um arquivo HTML.
    Args:
        text (str): O texto a ser procurado no Google.
    """
    params = {"q": text, "oq": text}
    r = requests.get("http://google.com/search", params=params)
    content = r.text
    if isHtml(file):
        with open(file, "w+") as html:
            html.write(content)

if __name__ == '__main__':
    main()