from turtle import Screen
import turtle
import os
import pandas

IMAGE = "/data/blank_portugal.gif"
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file
dataset = []

screen = Screen()
text = turtle.Turtle()

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
def get_data_from_csv(dataset):
    """
    get data from csv file
    :param: dataset: csv file
    :return: list data
    """
    file_path = dir_path + dataset
    return pandas.read_csv(file_path)
def write_district_name(x, y, district, color):
    """
    write the district name in xy coordinates
    :param color: color of the district name
    :param district: district name
    :param x: x-axis
    :param y: y-axis
    """
    text.hideturtle() # hide the turtle
    text.penup() # put the pen down
    text.goto(x, y)
    text.color(color)
    text.write(district, align="center", font=("Arial", 10, "normal"))
def create_failed_districts_csv(guessed):
    """
    csv file with districts that the user failed
    :param guessed: districts that the user guessed
    :return: csv file with districts that the user failed
    """
    guessed_names = [row["district"].values[0] for row in guessed]
    districts_failed = dataset[~dataset["district"].isin(guessed_names)]
    districts_failed.to_csv("data/districts_failed.csv", index=False)
def write_failed_districts_map():
    dataset_failed = get_data_from_csv("/data/districts_failed.csv")
    for _, row in dataset_failed.iterrows():
        write_district_name(row["x"], row["y"], row["district"], "red")
def game():
    """
    enter the district name until the user wins
    """

    is_game_on = True
    guessed_districts = []
    total_districts = len(dataset)
    while is_game_on:  # while the game happens
        answer_district = screen.textinput(title=f"{len(guessed_districts)}/{total_districts} Districts Correct", prompt="What's another district's name?") # user answer

        if answer_district is None: # if the user clicks on the cancel button
            continue

        if answer_district.lower() == "exit": # if the user clicks on the exit button
            create_failed_districts_csv(guessed_districts) # generate csv with districts I failed
            write_failed_districts_map()  # show in a map
            return # exit the game without a close map

        answer_district = answer_district.title() # format the answer

        match = dataset[dataset["district"].str.lower() == answer_district.lower()] # if answer_district exists in the dataset
        if len(match) >= 1:
            x = match["x"].values[0]
            y = match["y"].values[0]
            write_district_name(x, y, match["district"].values[0], "green") # write the district name in xy given
            guessed_districts.append(match)

            if total_districts == len(guessed_districts): # check if complete all districts
                is_game_on = False # the game is over

setup_screen() # set up the screen
# screen.onscreenclick(get_mouse_click_coor) # get mouse click coordinates
dataset = get_data_from_csv("/data/districts.csv")
game() # enter the district name until the user wins
screen.mainloop()