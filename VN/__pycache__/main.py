import text
import textwrap

userName = input('Please enter your name:\n')
iniText = 0

def textDisplay(scene):
    global iniText
    for i in scene:
        textwrapping = len(scene)
        print('\n' * 50)
        print('─' * 100)
        if '\n' in scene:
            print(scene)
            print('\n' * (3 - scene.count('\n')))
        else:
            print(textwrap.fill(scene, 90, break_long_words=False))
            if 90 >= textwrapping:
                print('\n' * 3)
            elif 180 >= textwrapping > 90:
                print('\n' * 2)
            elif 270 >= textwrapping > 180:
                print('\n')
            elif 360 >= textwrapping > 270:
                print()
            elif 450 >= textwrapping > 360:
                print(end = '')
        print('─' * 100, end = '')
        iniText += 1
        scene = text.scene1(userName, iniText)
        input('')

textDisplay(text.scene1(userName, iniText))