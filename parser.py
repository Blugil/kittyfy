import json


def parseKitty():
    
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

#TODO: make sure validation works even if out of order
# rethink this functions purpose, do we want to enable themes to set only
# the values within the theme or be required to set all values
def validateTheme(filename):
    
    # this is lazy programming, other file already has a load fn
    # just for test do NOT use in prod, no need to open files twice
    data = json.load(open(filename, 'r'))
    theme_keys = list(data.keys())

    # temp proof of concept
    colors = ['hello', 'test'] 

    ## checks to make sure all required colors are in the theme.json file
    for i, color in enumerate(colors):
        try:
            print(theme_keys[i], color)
            if theme_keys[i] != color:
                return False
        except:
            print('Exception handled')
            return False
    return True
    

if __name__ == "__main__":
    # parseKitty()
    print(validateTheme('./themes/gruvbox.json'))
