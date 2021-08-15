#! /usr/bin/env python3
import ui
import util

if __name__ == "__main__":

    # launch app
    themes = util.readDir('./themes')
    selected = util.readSelected('./selected.json')

    app = ui.App(selected, themes)
    app.run()
