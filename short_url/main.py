import requests
import simplejson as json
import re

def main():
    url = urlShortner("http://www.google.com")
    print(url)
    
def urlShortner(url: str) -> str:
    """
    Encurtador de URL
     Args:
        url (str): A URL do site onde será feita a busca.
    Retorna:
        String com o link encurtado.
    """
    if(isUrl(url)):
        payload = { 'url': url}
        header = {"Content-Type": "application/json"}
        r = requests.post("https://api.encurtador.dev/encurtamentos", json=payload, headers=header)
        return (json.loads(r.text)['urlEncurtada'])

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

if __name__ == '__main__':
    main()