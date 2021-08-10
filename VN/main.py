import text
import path
import textwrap

userName = input('Please enter your name:\n')
iniText = 0

def choices(option1 = False, option2 = False, option3 = False, option4 = False):
    print('\n'.join(path.split1()[0]))
    userInp = int(input())
    if userInp == option1:
        print(1)
    elif userInp == option2:
        print(2)
    elif userInp == option3:
        print(3)
    elif userInp == option4:
        print(4)

def textDisplay(scene):
    global iniText
    for i in scene:
        try:
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
            input()
        except IndexError:
            input()
            break

textDisplay(text.scene1(userName, iniText))
choices(path.split1()[1], path.split1()[2])