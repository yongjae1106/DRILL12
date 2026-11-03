from pico2d import load_image


class Ball:
    image = None

    def __init__(self, x, y, velocity):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity

    def draw(self):
        self.image.draw(self.x, self.y)
