from turtle import Screen
import turtle
import os
import pandas

IMAGE = "/data/blank_portugal.gif"
DATASET = "/data/districts.csv"
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file
dataset = []

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
def write_district_name(x, y, district):
    """
    write the district name in xy coordinates
    :param district: district name
    :param x: x-axis
    :param y: y-axis
    """
    text = turtle.Turtle()
    text.hideturtle() # hide the turtle
    text.penup() # put the pen down
    text.goto(x, y)
    text.write(district, align="center", font=("Arial", 10, "normal"))
def game():
    """
    enter the district name until the user wins
    """

    is_game_on = True
    guessed_districts = []
    total_districts = len(dataset)
    while is_game_on:  # while the game happens
        answer_district = screen.textinput(title=f"{len(guessed_districts)}/{total_districts} Districts Correct", prompt="What's another district's name?").title() # user answer

        if len(dataset[dataset["district"].str.lower() == answer_district.lower()]) >= 1: # check if answer_district exists in the dataset
            district = dataset[dataset["district"].str.lower() == answer_district.lower()]
            x = district["x"].values[0]
            y = district["y"].values[0]
            write_district_name(x, y, district["district"].values[0]) # write the district name in xy given
            guessed_districts.append(district)

            if total_districts == len(guessed_districts): # check if complete all districts
                is_game_on = False # the game is over

setup_screen() # set up the screen
# screen.onscreenclick(get_mouse_click_coor) # get mouse click coordinates
dataset = get_data_from_csv()
game() # enter the district name until the user wins
screen.mainloop() # keep the screen running