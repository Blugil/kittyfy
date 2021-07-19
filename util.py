kitty_theme_options = ['color0','color1','color2','color3','color4','color5','color6','color7','color8', 'color9','color10','color11','color12','color13','color14','color15','background', 'foreground', 'selection_background', 'selection_foreground']

# proof of concept parser that looks through a config file and prints (for now) each matching
# option
def parseKitty():
    
    theme = open("theme.conf", "rt")

    if theme:
        cond = True
        line_count = 0

        color_positions = {}

        # checks all lines for matching theme options and stores line number
        while cond: 

            line = theme.readline()
            option = line.split(' ')[0]
            
            if line:
                for theme_option in kitty_theme_options:
                    if theme_option == option:
                        color_positions[option] = line_count
                        break
            else:     
                theme.close()
                cond = False

            line_count += 1

        return color_positions

    else:
        return {}


def replace(theme: dict):

    return theme

# gets the index of the selected theme 
def startSelect(data, selected):
    if data and selected:
        for i, value in enumerate(data):
            print(selected, value)
            if selected in value:
               return i
        return 0
    else: 
        return 0

# parses filenames from filepaths
def nameSplitter(paths: list):
    if paths:
        themeNames = []
        for string in paths:
            themeNames.append(string[string.rindex('/')+1:string.rindex('.')])
        return themeNames
    else:
        return []

# validates that a theme contains *only* the available kitty theme config options
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

    print(parseKitty())

    # data = json.load(open('./themes/gruvbox.json', 'r'))
    # print(validateTheme(data))
