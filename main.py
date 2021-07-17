#! /usr/bin/env python3
import ui
import file

if __name__ == "__main__":

    themes = file.readDir('./themes')
    selected = file.readSelected('./test.json')

    app = ui.App(selected, themes)
    app.run()
