options = ["snake", "water", "gun"]
winCases = {
    (0, 2),
    (1, 0),
    (2, 1),
}


def checkwin(my_choice, friend_choice):
    """
    Check if the choices made by the player and their friend result in a win, loss, or tie in a game.

    Args:
        my_choice (int): An integer representing the player's choice.
        friend_choice (int): An integer representing the friend's choice.

    Returns:
        int: 0 if the choices result in a tie, 1 if the player wins, -1 if the player loses.
    """
    if my_choice == friend_choice:
        return 0
    elif (friend_choice, my_choice) in winCases:
        return 1
    else:
        return -1