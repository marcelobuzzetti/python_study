class File:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        with open(self.filename, "w+") as newfile:
            newfile.write(self.text)
            newfile.close()
    
    def __str__(self):
        return f"{self.filename} contains {self.text}"