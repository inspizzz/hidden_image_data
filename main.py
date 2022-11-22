from PIL import Image

class Encode():
    def __init__(self) -> None:
        self.loaded = False
        self.img = []
        

    def load(self, filename):
        img = Image.open(filename)
        for i in range(0, img.size[0]):
            row = []
            for j in range(0, img.size[1]):
                row.append(img.getpixel(xy=(i, j)))
            print(f"{i} : {j}")
            self.img.append(row)

        print(self.img)


    def encryptImg(self, data):
        for row in self.img:
            for element in row:
                


class Decode():
    def __init__(self) -> None:
        self.loaded = False

    def load(self):
        pass
    
    def decodeImg():
        pass

if __name__ == "__main__":
    enc = Encode()
    enc.load(filename="/home/wiktor/Desktop/python/hidden_image_data/image.jpg")

