from pico2d import load_image
grass_count = 0

class Grass:
    count = 0
    def __init__(self):
        self.image = load_image('grass.png')
        grass_count += 1

    def draw(self):
        if grass_count == 0:
            self.image.draw(400, 30)
        else:
            self.image.draw(400, 50)
            
            

    def update(self):
        pass
