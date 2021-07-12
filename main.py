import npyscreen

class App(npyscreen.NPSApp):
    def __init__(self, themes):
        self.themes = themes

    def main(self):

        F = npyscreen.Form(name = "Hello World!",)

        F.add(npyscreen.TitleSelectOne, 
                max_height=(len(themes)+1), 
                value = [0,], 
                name = "Select Theme",
                values = themes)

        F.edit()

if __name__ == "__main__":

    themes = ["Nord", "Gruvbox", "Solarized", "One Dark"]
    app = App(themes)
    app.run()
