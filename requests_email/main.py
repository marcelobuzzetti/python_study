import requests

def main():
    my_data = { 'name': 'Marcelo', 'email': 'marcelo@gmail.com'}
    r = requests.post('https://webhook.site/e6aba3f2-e5e2-4332-895f-673454bb15ca', data=my_data)
    with open('myfile.html', "w+") as newfile:
            newfile.write(r.text)
            newfile.close()

if __name__ == '__main__':
    main()