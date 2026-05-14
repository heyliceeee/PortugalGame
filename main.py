import turtle
from turtle import Screen
IMAGE = "blank_portugal.gif"

screen = Screen()

def setup_screen():
    """
    set up the screen
    """
    screen.title("Portugal District Game") # set the title of the screen
    screen.addshape(IMAGE) # set background image
    turtle.shape(IMAGE)
def get_mouse_click_coor(x, y):
    """
    get the mouse click coordinates
    :param x: x-axis
    :param y: y-axis
    :return: the mouse click coordinates
    """
    print(x, y)


setup_screen() # set up the screen
screen.onscreenclick(get_mouse_click_coor) # get mouse click coordinates
screen.mainloop() # keep the screen running