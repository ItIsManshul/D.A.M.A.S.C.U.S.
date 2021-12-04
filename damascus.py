import wolframalpha
client = wolframalpha.Client("HT4YU8-T7P857JGQ7")

import wikipedia

import PySimpleGUI as sg

sg.theme('Topanga')
layout =[[sg.Text('Enter a command '),   sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('THURSDAY', layout)

import pyttsx3
engine = pyttsx3.init()

while True:
    engine.say(f'hello my name is thursday and your answer is')
    break

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])

engine.say(f'Operation completed !')

window.close()

#PLEASE READ
#WRITE THE FOLLOWING CODE IN THE TERMINAL TO IMPORT THE PROGRAMMES FIRST
#pip install wolframalpha
#pip install wikipedia
#pip install pyttsx3
#pip install PySimpleGUI
#pip install 
