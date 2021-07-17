#! /usr/bin/env python3
import npyscreen
import util
import file


# returns a list of filenames from pilepaths

# returns index of selected theme


class App(npyscreen.NPSApp):

    def __init__(self, selected, themes):
        self.themes = themes
        self.selected_theme = selected

    def main(self):
       
        value = [0,]
        len_themes = len(self.themes)
        
        if len_themes > 0:
            value = [util.startSelect(self.themes, self.selected_theme),] 
        else:
            value = [0,]

        name =  "Select Theme" if len_themes > 0 else "No Themes"
        values = util.nameSplitter(self.themes)

        F = npyscreen.Form(name = "Kitty Theme", lines=20)
        select = F.add(
                npyscreen.TitleSelectOne, 
                max_height=(len_themes + 2), 
                value = value, 
                name = name, 
                values = values)

        F.edit()
        
        # write selected theme to file
        if len_themes > 0:
            # get_selected_objects returns array and I want a string
            file.writeSelected(select.get_selected_objects()[0], 'test.json')


if __name__ == "__main__":

    themes = file.readDir('./themes')
    selected = file.readSelected('./test.json')

    app = App(selected, themes)
    app.run()
