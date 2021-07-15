def parser():
    
    # successfully parses my kitty conf file, just gotta work on changing it now
    # kitty = open("./kitty.conf", "wt")
    theme = open("theme.conf", "rt")

    if theme:
        cond = True
        color_count = 0
        line_count = 0

        initial_color = 0
        
        # runs through 
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

                #removes \n just from print (keep it for actual file)
                print(line.strip('\n'))

            elif color_count > 15:
                cond = False
    else:
        return



if __name__ == "__main__":
    parser()
