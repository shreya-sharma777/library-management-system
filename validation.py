def valid_menu_choice(choice):
    if choice.isdigit():
        number = int(choice)

        if 1 <= number <= 10:
            return True

    return False