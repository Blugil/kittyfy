import json


kitty_theme_options = ['color0','color1','color2','color3','color4','color5','color6','color7','color8', 'color9','color10','color11','color12','color13','color14','color15','background', 'foreground', 'selection_background', 'selection_foreground']

# proof of concept parser that looks through a config file and prints (for now) each matching
# option
def parseKitty(kitty_conf: str) -> dict:
    
    kitty = open(kitty_conf, "rt")

    if kitty:
        cond = True
        line_count = 0

        color_positions = {}

        # checks all lines for matching theme options and stores line number
        while cond: 

            line = kitty.readline()
            option = line.split(' ')[0]
            
            if line:
                for theme_option in kitty_theme_options:
                    if theme_option == option:
                        color_positions[option] = line_count
                        break
            else:     
                kitty.close()
                cond = False

            line_count += 1
        
        kitty.close()
        return color_positions

    else:
        kitty.close()
        return {}


# stores only the lines not listed in line numbers
def readKitty(filename: str) -> list:
  
    # grabs the array of line numbers needing to be replaced
    line_numbers = parseKitty(filename)
    line_numbers_array = line_numbers.values()

    data = open(filename, 'rt')
    
    #read will return this
    document = []

    cond = True
    current_line = 0

    # adds line numbers not listed to array
    while cond:

        line = data.readline()

        if line and current_line not in line_numbers_array:
            document.append(line)

        if not line:
            cond = False

        current_line += 1
    
    data.close()
    return document

# adds new theme values in a constructed string to the array
def update(new_kitty_conf: list, new_theme: dict) -> list:
    
    new_kitty_conf = new_kitty_conf

    keys = new_theme.keys()

    for key in keys: 
        string = key + ' ' + new_theme[key] + '\n'
        new_kitty_conf.append(string)

    
    return new_kitty_conf
    
def replace(kitty_conf: str, kitty_conf_array: list):

    kitty = open(kitty_conf, 'wt')
    kitty.writelines(kitty_conf_array)
    kitty.close()

# gets the index of the selected theme 

# parses filenames from filepaths


if __name__ == "__main__":

    # print(parseKitty('./theme.conf'))
    # print(readKitty('./theme.conf'))
    new_theme = json.load(open('./themes/gruvbox.json'))
    kitty = update(readKitty('./theme.conf'), new_theme)

    replace('./theme.conf', kitty)

