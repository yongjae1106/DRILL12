from pico2d import get_canvas_width

world = [[], []] # layers for game objects

def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol, depth):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise Exception("Object not found")


def update():
    for layer in world:
        for o in layer[:]:
            o.update()
            if hasattr(o, 'x') and (o.x < 0 or o.x > get_canvas_width()):
                remove_object(o)

def render():
    for layer in world:
        for o in layer:
            o.draw()


