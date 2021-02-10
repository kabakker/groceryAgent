from PIL import Image
import math

class ImageGrid:

    def __init__(self):
        self.image = Image.open("store.png")
        self.pixels = self.image.load()
        print(self.pixels[10,10])

    def create_sensor_lines(self, starting_point, N_lines, orientation):
        X = []
        Y = []
        for i in range(N_lines):
            angle = i * 360/N_lines
            x, y = self.create_sensor_line(starting_point, orientation, angle)
            X.append(starting_point[0])
            X.append(x)
            Y.append(starting_point[1])
            Y.append(y)
        return X,Y

    def create_sensor_line(self, starting_point, orientation, angle):
        idxx = starting_point[0]
        idxy = starting_point[1]
        pos = self.pixels[idxx, idxy]
        step = 1
        i = 0
        while pos == (255, 255, 255, 255):
            i += 1
            idxx = round(starting_point[0] -i * step * math.sin((orientation + angle) * math.pi / 180))
            idxy = round(starting_point[1] -i * step * math.cos((orientation + angle) * math.pi / 180))
            pos = self.pixels[idxx, idxy]
        return idxx, idxy
