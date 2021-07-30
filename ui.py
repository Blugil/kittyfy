import json
import npyscreen
import util
import kitty


# returns a list of filenames from pilepaths

# returns index of selected theme


class App(npyscreen.NPSApp):

    def __init__(self, selected, themes):
        self.themes = themes
        self.selected_theme = selected

    def edit(self, data):

        return data

    def main(self):
       
        value = [0,]
        len_themes = len(self.themes)
        
        if len_themes > 0:
            value = [util.startSelect(self.themes, self.selected_theme),] 
        else:
            value = [0,]

        name =  "Select Theme" if len_themes > 0 else "No Themes"

        value_dict = util.nameSplitter(self.themes)
        value_keys = list(value_dict.keys())

        F = npyscreen.Form(name = "Kitty Theme", lines=20)
        select = F.add(
                npyscreen.TitleSelectOne, 
                max_height=(len_themes + 2), 
                value = value, 
                name = name, 
                values = value_keys)

        F.edit()

        selected = select.get_selected_objects()[0]
        
        # write selected theme to file
        if len_themes > 0:
            # get_selected_objects returns array and I want a string
            util.writeSelected(selected, 'test.json')
        
        selected_theme = json.load(open(value_dict[selected], 'rt')) 

        if util.validateTheme(selected_theme):
            data = kitty.readKitty('./kitty.conf')
            kitty_update = kitty.update(data, selected_theme)
            kitty.replace('./kitty.conf', kitty_update) 
        
        # planned 
        # read selected theme file
        # validate it 
        # data = kitty.readKitty(kitty_conf)
        # kitty = update(data, selected_theme)
        # replace(kitty_conf, kitty)

