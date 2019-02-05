from bearlibterminal import terminal as blt  # renderer
import objects


class Engine:

    # constructor
    def __init__(self):
        self.controller = objects.GameController(self)
        self.objects = list() # (dependancy injection)
        self.running = True

    def init(self):
        blt.open()
        blt.refresh()

    # update method
    def update(self):
        self.controller.update()

    # render method
    def render(self):
        # Prints to the screen
        self.controller.render()
        blt.refresh()

    # main event loop // entry point
    def main(self):
        # every frame
        while self.running:
            # read all of the events
            while blt.has_input():
                event = blt.read()
                print(event)
                if event in (blt.TK_CLOSE, blt.TK_ESCAPE):
                    self.running = False
            self.update()
            self.render()


