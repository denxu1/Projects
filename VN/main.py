import text
import path
import textwrap
import time

userName = input('Please enter your name:\n')
iniText = 0
rebecca = 0
lisa = 0
chris = 0

def scenes(key):
    global iniText
    if key == 1:
        input()
        return textDisplay(text.scene1(userName, iniText), 1)
    elif key == 2:
        input()
        return textDisplay(text.scene2(userName, iniText), 2)
    elif key == 'c1-1':
        input()
        return textDisplay(path.outcome1(userName, iniText)[0], 'c1-1')
    elif key == 'c1-2':
        input()
        return textDisplay(path.outcome1(userName, iniText)[1], 'c1-2')
    elif key == '2_1':
        input()
        return textDisplay(text.scene2_1(userName, iniText), '2_1')
    elif key == '2_2':
        input()
        return textDisplay(text.scene2_1(userName, iniText), '2_2')

def choices(scenario, option1 = False, option2 = False, option3 = False, option4 = False):
    while True:
        print('\n' * 50)
        print('─' * 100)
        a = '\n'.join(scenario)
        print(a)
        print('\n' * (3 - a.count('\n')))
        print('─' * 100)
        try:
            userInp = input()
            if int(userInp) == option1:
                return 1
                break
            elif int(userInp) == option2:
                return 2
                break
            elif int(userInp) == option3:
                return 3
                break
            elif int(userInp) == option4:
                return 4
                break
            else:
                raise ValueError
        except:
            print('\n' * 50)
            print('─' * 100)
            print('-Invalid input-')
            print('\n' * 3)
            print('─' * 100)
            time.sleep(2)
            continue

def textDisplay(scene, key):
    global iniText
    for i in scene:
        if scene is None:
                break
        try:
            print('\n' * 50)
            if scene.find('User') == 0:
                print(userName)
                scene = scene.replace('User', '', 1)
            elif scene.find('!') == 0:
                scene = scene.replace('!', '', 1)
            elif scene.find('Jimmy') == 0:
                print('Jimmy')
                scene = scene.replace('Jimmy', '', 1)
            elif scene.find('Aiya') == 0:
                print('Aiya')
                scene = scene.replace('Aiya', '', 1)
            elif scene.find('Lisa') == 0:
                print('Lisa')
                scene = scene.replace('Lisa', '', 1)
            elif scene.find('Rebecca') == 0:
                print('Rebecca')
                scene = scene.replace('Rebecca', '', 1)
            elif scene.find('Woman') == 0:
                print('Woman')
                scene = scene.replace('Woman', '', 1)
            elif scene.find('Man') == 0:
                print('Man')
                scene = scene.replace('Man', '', 1)
            elif scene.find('Ben') == 0:
                print('Ben')
                scene = scene.replace('Ben', '', 1)
            elif scene.find('Chris') == 0:
                print('Chris')
                scene = scene.replace('Chris', '', 1)
            print('─' * 100)
            textwrapping = len(scene)
            if '\n' in scene:
                print(scene)
                print('\n' * (3 - scene.count('\n')))
            else:
                print(textwrap.fill(scene, 90, break_long_words = False))
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
                else:
                    print('\n' * 4)
            print('─' * 100, end = '')
            iniText += 1
            scene = scenes(key)
        except IndexError:
            break

#textDisplay(text.scene1(userName, iniText), 1)
#iniText = 0
#choice1 = choices(path.split1()[0], path.split1()[1], path.split1()[2])
#if choice1 == 1:
#    textDisplay(path.outcome1(userName, iniText)[0], 'c1-1')
#elif choice1 == 2:
#    textDisplay(path.outcome1(userName, iniText)[1], 'c1-2')
#iniText = 0
textDisplay(text.scene2(userName, iniText), 2)
iniText = 0
choice2 = choices(path.split2()[0], path.split2()[1], path.split2()[2])
if choice2 == 1:
    lisa += 1
    textDisplay(text.scene2_1(userName, iniText), '2_1')
elif choice2 == 2:
    textDisplay(text.scene2_2(userName, iniText), '2_2')