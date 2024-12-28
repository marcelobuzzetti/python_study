import simplejson as json
import os

# funcao para escrever no arquivo json
def write(file, data):
        # vai para a primeira posicao no arquivo
        file.seek(0)
        file.write(json.dumps(data))

def ages():
    if os.path.isfile('./ages.json') and os.stat('./ages.json').st_size != 0:
        with open('./ages.json', 'r+') as old_file:
            data = json.loads(old_file.read())
            print(f"Current age is {data['age']} -- adding a year")
            data["age"] = data["age"] + 1
            print(f"New age is {data['age']}")
            write(old_file, data)
    else:
        with open("ages.json", "w+") as old_file:
            data = {"name": "Marcelo", "age": 38}
            print("No file found. Creating a new one")
            write(old_file, data)

def main():
    ages()
    
if __name__ == '__main__':
    main()