def parser():
    
    # kitty = open("./kitty.conf", "wt")
    theme = open("./theme.conf", "rt")

    cond = True
    color_count = 0
    line_count = 0

    initial_color = 0

    while cond: 

        line = theme.readline()
        line_count += 1
        color = "color" + str(color_count) + " "

        if not line and color_count < 15:
            line_count = 0
            theme.seek(initial_color)

        elif color in line:
            if color_count == 0:
                initial_color = line_count

            color_count += 1
            print(line)

        elif color_count > 15:
            cond = False


   
if __name__ == "__main__":

    parser()
