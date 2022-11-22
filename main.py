from PIL import Image
import numpy as np

class Encode():
    def __init__(self) -> None:
        self.img = []
        

    def load(self, filename):
        img = Image.open(filename)
        for i in range(0, img.size[0]):
            row = []
            for j in range(0, img.size[1]):
                row.append(img.getpixel(xy=(i, j)))
            print(f"{i} : {j}")
            self.img.append(row)


    def encodeImg(self, data):
        # convert data to bits
        counter = 0
        print(f"size=({len(self.img)}, {len(self.img[0])})")
        new_img = Image.new('RGB', (len(self.img),len(self.img[0])))

        for row in range(0, len(self.img)):
            new_row = []
            for element in range(len(self.img[row])):

                r = bin(self.img[row][element][0])
                g = bin(self.img[row][element][1])
                b = bin(self.img[row][element][2])

                new_r = r[0:-2] + data[counter+0:counter+2] + ('0'*(2-len(data[counter+0:counter+2]))) 
                new_g = g[0:-2] + data[counter+2:counter+4] + ('0'*(2-len(data[counter+2:counter+4]))) 
                new_b = b[0:-2] + data[counter+4:counter+6] + ('0'*(2-len(data[counter+4:counter+6]))) 

                new_r = int(new_r, 2)
                new_g = int(new_g, 2)
                new_b = int(new_b, 2)

                # print(f"({new_r}, {new_g}, {new_b})")
                
                new_img.putpixel(xy=(row, element), value=(new_r, new_g, new_b))

                counter += 6

            print(f"{row} : {element}")

        new_img.save("image2.jpg")




class Decode():
    def __init__(self) -> None:
        self.img = []

    def load(self, filename):
        img = Image.open(filename)
        for i in range(0, img.size[0]):
            row = []
            for j in range(0, img.size[1]):
                row.append(img.getpixel(xy=(i, j)))
            print(f"{i} : {j}")
            self.img.append(row)
    
    def decodeImg(self):
        decoded = ""
        for row in range(0, len(self.img)):
            for element in range(0, len(self.img[row])):
                r = bin(self.img[row][element][0])
                g = bin(self.img[row][element][1])
                b = bin(self.img[row][element][2])

                decoded += r[-2:] + g[-2:] + b[-2:]
        print(decoded[0:20]) 




if __name__ == "__main__":
    enc = Encode()
    dec = Decode()

    # enc.load(filename="/home/wiktor/Desktop/python/hidden_image_data/image.jpg")
    # enc.encodeImg(data="0101010101010101010101")

    dec.load(filename="/home/wiktor/Desktop/python/hidden_image_data/image2.jpg")
    dec.decodeImg()

