import webview
import os
import json
import database
import webview.menu as wm

import exposedAPI as api


def menuAction():
    pass

def closeApp():
    window.destroy()

jsonData = open("window.json")
windowData = json.load(jsonData)
mainWindow = windowData['mainWindow']

pyjs = api.Api()

if (mainWindow['useDatabase'] == True):
    database.CanUseDatabase()


menu = [
    wm.Menu('File',
            [
                wm.MenuAction('Placeholder', menuAction),     
                wm.MenuSeparator(),
                 wm.Menu(
                    'Close App',
                    [
                        wm.MenuAction('Placeholder', menuAction),
                        wm.MenuAction('Quit', closeApp),
                    ],)
            ])
]

window = webview.create_window(
                        title=mainWindow['title'],
                        url=mainWindow['mainFile'],
                        fullscreen=mainWindow['fullscreen'],
                        confirm_close=mainWindow['confirm_close'],
                        maximized=mainWindow['maximised'],
                        min_size=(mainWindow['min_size_x'], mainWindow['min_size_y']),
                        js_api=pyjs
                    )




webview.start(debug=False, menu=menu)