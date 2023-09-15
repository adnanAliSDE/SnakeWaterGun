import random

options = ["snake", "water", "gun"]
winCases = {
    (0, 2),
    (1, 0),
    (2, 1),
}


def checkwin(my_choice, friend_choice):
    if my_choice == friend_choice:
        return 0
    elif (friend_choice, my_choice) in winCases:
        return 1
    else:
        return -1
