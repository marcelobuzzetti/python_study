import requests
from io import BytesIO
from PIL import Image

def main():
    """
    Salvando uma image usando pillow
    """
    r = requests.get("https://img.freepik.com/free-photo/abstract-dark-background-with-flowing-colouful-waves_1048-13124.jpg?t=st=1734884226~exp=1734887826~hmac=b132352e1cabcc15bf785b5d6eb2fe8883b2064200a0e87adc544e28f2138a1c&w=996")
    print(f"Status code {r.status_code}")
    image = Image.open(BytesIO(r.content))
    print(image.size, image.format, image.mode)
    path = "image." + image.format

    try:
        image.save(path, image.format)
    except IOError:
        print("Cannot save image")

if __name__ == '__main__':
    main()