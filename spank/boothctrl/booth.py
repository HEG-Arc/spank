import web
import pysimpledmx
import time

urls = (
    '/ambiant', 'ambiant',
    '/roulette', 'roulette',
    '/win', 'win',
    '/bye', 'bye'
)


def ambiant_light():
    mydmx = pysimpledmx.DMXConnection(4)
    mydmx.setChannel(1, 0) # set DMX channel 1 Red
    mydmx.setChannel(2, 138) # set DMX channel 2 Green
    mydmx.setChannel(3, 201)   # set DMX channel 3 Blue
    mydmx.setChannel(4, 0)   # set DMX channel 4 Dimmer
    mydmx.setChannel(5, 0)   # set DMX channel 5 Strobe
    mydmx.setChannel(6, 0)   # set DMX channel 5 Strobe
    mydmx.setChannel(7, 150)   # set DMX channel 5 Strobe
    mydmx.render()           # render all of the above changes onto the DMX network
    #mydmx.setChannel(4, 255, autorender=True) # set channel 4 to full and render to the network

def roulette_light():
    mydmx = pysimpledmx.DMXConnection(4)
    mydmx.setChannel(1, 0) # set DMX channel 1 Red
    mydmx.setChannel(2, 138) # set DMX channel 2 Green
    mydmx.setChannel(3, 201)   # set DMX channel 3 Blue
    mydmx.setChannel(4, 0)   # set DMX channel 4 Dimmer
    mydmx.setChannel(5, 220)   # set DMX channel 5 Strobe
    mydmx.setChannel(6, 0)   # set DMX channel 5 Strobe
    mydmx.setChannel(7, 255)   # set DMX channel 5 Strobe
    mydmx.render()           # render all of the above changes onto the DMX network


def win_light():
    mydmx = pysimpledmx.DMXConnection(4)
    for i in range(1, 6):
        mydmx.setChannel(1, 0) # set DMX channel 1 Red
        mydmx.setChannel(2, 138) # set DMX channel 2 Green
        mydmx.setChannel(3, 201)   # set DMX channel 3 Blue
        mydmx.setChannel(4, 0)   # set DMX channel 4 Dimmer
        mydmx.setChannel(5, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(6, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(7, 255)   # set DMX channel 5 Strobe
        mydmx.render()           # render all of the above changes onto the DMX network
        time.sleep(0.2)
        mydmx.setChannel(1, 239) # set DMX channel 1 Red
        mydmx.setChannel(2, 130) # set DMX channel 2 Green
        mydmx.setChannel(3, 20)   # set DMX channel 3 Blue
        mydmx.setChannel(4, 0)   # set DMX channel 4 Dimmer
        mydmx.setChannel(5, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(6, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(7, 255)   # set DMX channel 5 Strobe
        mydmx.render()           # render all of the above changes onto the DMX network
        time.sleep(0.2)
        mydmx.setChannel(1, 230) # set DMX channel 1 Red
        mydmx.setChannel(2, 0) # set DMX channel 2 Green
        mydmx.setChannel(3, 98)   # set DMX channel 3 Blue
        mydmx.setChannel(4, 0)   # set DMX channel 4 Dimmer
        mydmx.setChannel(5, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(6, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(7, 255)   # set DMX channel 5 Strobe
        mydmx.render()           # render all of the above changes onto the DMX network
        time.sleep(0.2)
        mydmx.setChannel(1, 123) # set DMX channel 1 Red
        mydmx.setChannel(2, 170) # set DMX channel 2 Green
        mydmx.setChannel(3, 32)   # set DMX channel 3 Blue
        mydmx.setChannel(4, 0)   # set DMX channel 4 Dimmer
        mydmx.setChannel(5, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(6, 0)   # set DMX channel 5 Strobe
        mydmx.setChannel(7, 255)   # set DMX channel 5 Strobe
        mydmx.render()           # render all of the above changes onto the DMX network
        time.sleep(0.2)
    mydmx.setChannel(1, 0) # set DMX channel 1 Red
    mydmx.setChannel(2, 138) # set DMX channel 2 Green
    mydmx.setChannel(3, 201)   # set DMX channel 3 Blue
    mydmx.setChannel(4, 0)   # set DMX channel 4 Dimmer
    mydmx.setChannel(5, 0)   # set DMX channel 5 Strobe
    mydmx.setChannel(6, 0)   # set DMX channel 5 Strobe
    mydmx.setChannel(7, 150)   # set DMX channel 5 Strobe
    mydmx.render()           # render all of the above changes onto the DMX network

def no_light():
    mydmx = pysimpledmx.DMXConnection(4)
    mydmx.setChannel(7, 0)   # set DMX channel 4 Dimmer
    mydmx.render()           # render all of the above changes onto the DMX network
    #mydmx.setChannel(4, 255, autorender=True) # set channel 4 to full and render to the network

class ambiant:
    def GET(self):
        ambiant_light()
        return "Hello, light is blue"

class roulette:
    def GET(self):
        roulette_light()
        return "Hello, light is roulette"

class win:
    def GET(self):
        win_light()
        return "Hello, light is roulette"


class bye:
    def GET(self):
        no_light()
        return "Hello, light is off"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()