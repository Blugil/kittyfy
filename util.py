import json

kitty_theme_options = ['color0','color1','color2','color3','color4','color5','color6','color7','color8', 'color9','color10','color11','color12','color13','color14','color15','background', 'foreground', 'selection_background', 'selection_foreground']

# parseKitty needs to only examine and record *possible* options, without expecting all color 
# sets to be there per new ideas. need to check in a smilar fashion to validateTheme()
def parseKitty():
    
    # successfully parses my kitty conf file, just gotta work on changing it now
    # kitty = open("./kitty.conf", "wt")
    theme = open("theme.conf", "rt")

    if theme:
        cond = True
        color_count = 0
        line_count = 0

        initial_color = 0
        final_color = 0

        non_color_options = kitty_theme_options[-4:]
        
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
                
                elif line_count > final_color:
                    final_color = line_count
                color_count += 1

                #removes \n just from print (keep it for actual file)
                print(line.strip('\n'))

            elif color_count > 15:
                cond = False
        
        return (initial_color, final_color)
    else:
        return ()

def startSelect(data, selected):
    if data:
        for i, value in enumerate(data):
            print(selected, value)
            if selected in value:
               return i
        return 0
    else: 
        return 0

def nameSplitter(paths: list):
    if paths:
        themeNames = []
        for string in paths:
            themeNames.append(string[string.rindex('/')+1:string.rindex('.')])
        return themeNames
    else:
        return []

def validateTheme(data: dict):

    theme_keys = list(data.keys())

    # available kitty color theming options

    check_theme = 0
    validated_theme = len(theme_keys)

    # checks that all options in theme.json file are valid
    for i in range(len(theme_keys)):
        for option in kitty_theme_options:
            try:
                if theme_keys[i] == option:
                    check_theme += 1
                    break
            except:
                print('Exception handled')
                return False
    if check_theme == validated_theme:
        return True
    else:
        return False



if __name__ == "__main__":

    parse = parseKitty()
    print(parse)

    # data = json.load(open('./themes/gruvbox.json', 'r'))
    # print(validateTheme(data))
