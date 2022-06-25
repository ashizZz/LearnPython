def show_star():
    rows = 6
    for i in range(rows):
        for j in range(i):
            print('* ', end="")
        print('')


show_star()
