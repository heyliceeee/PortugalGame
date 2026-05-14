import turtle
from turtle import Screen
import os
import pandas

IMAGE = "/data/blank_portugal.gif"
DATASET = "/data/districts.csv"
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file

screen = Screen()

def setup_screen():
    """
    set up the screen
    """
    screen.title("Portugal District Game") # set the title of the screen
    screen.addshape(dir_path + IMAGE) # set background image
    turtle.shape(dir_path + IMAGE)
def get_mouse_click_coor(x, y):
    """
    get the mouse click coordinates
    :param x: x-axis
    :param y: y-axis
    :return: the mouse click coordinates
    """
    print(x, y)
def get_data_from_csv():
    """
    get data from csv file
    :return: list data
    """
    file_path = dir_path + DATASET
    return pandas.read_csv(file_path)
def game():
    """
    enter the district name until the user wins
    """
    answer_district = screen.textinput(title="Guess the District", prompt="What's another district's name?").title() # user answer
    print(answer_district)

setup_screen() # set up the screen
# screen.onscreenclick(get_mouse_click_coor) # get mouse click coordinates
game() # enter the district name until the user wins
screen.mainloop() # keep the screen running