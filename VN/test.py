import text
import path
import textwrap
import time

userName = input('Please enter your name:\n')
saveList = ['Empty', 'Empty', 'Empty', 'Empty', 'Empty']
saveIni = ['', '', '', '', '']
saveKey = [0, 0, 0, 0, 0]
saveChara = ['', '', '', '', '']
loadList = saveList
iniText = 0
charaDic = {
    'lisa': 0,
    'rebecca': 0,
    'chris': 0
}

def errorMsg():
    print('\n' * 50)
    print('─' * 100)
    print('\n')
    print('-Invalid Input-\n\nPress \'Enter\' to Continue')
    print('─' * 100)
    time.sleep(2)

def scenes(key):
    global iniText
    while True:
        userIn = input()
        try:
            if key == 1:
                if userIn.lower() == 'save':
                    saveScreen(text.scene1(userName, iniText), 1)
                    iniText -= 1
                elif userIn.lower() == 'load':
                    loadScreen()
                elif userIn != '':
                    raise ValueError
                iniText += 1
                return section_1()
            elif key == 2:
                if userIn.lower() == 'save':
                    saveScreen(text.scene2(userName, iniText), 2)
                    iniText -= 1
                elif userIn.lower() == 'load':
                    loadScreen()
                elif userIn != '':
                    raise ValueError
                iniText += 1
                return section_2()
            elif key == 'c1-1':
                if userIn.lower() == 'save':
                    saveScreen(path.outcome1(userName, iniText)[0], 'c1-1')
                    iniText -= 1
                elif userIn.lower() == 'load':
                    loadScreen()
                elif userIn != '':
                    raise ValueError
                iniText += 1
                return section_1_1()
            elif key == 'c1-2':
                if userIn.lower() == 'save':
                    saveScreen(path.outcome1(userName, iniText)[1], 'c1-2')
                    iniText -= 1
                elif userIn.lower() == 'load':
                    loadScreen()
                elif userIn != '':
                    raise ValueError
                iniText += 1
                return section_1_2()
            elif key == '2_1':
                if userIn.lower() == 'save':
                    saveScreen(text.scene2_1(userName, iniText), '2_1')
                    iniText -= 1
                elif userIn.lower() == 'load':
                    loadScreen()
                elif userIn != '':
                    raise ValueError
                iniText += 1
                return section_2_1()
            elif key == '2_2':
                if userIn.lower() == 'save':
                    saveScreen(text.scene2_2(userName, iniText), '2_2')
                    iniText -= 1
                elif userIn.lower() == 'load':
                    loadScreen()
                elif userIn != '':
                    raise ValueError
                iniText += 1
                return section_2_2()
        except ValueError:
            errorMsg()
            iniText -= 1
            continue
        except IndexError or TypeError:
            break

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
            errorMsg()
            input()
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
            scene = scenes(key)
        except IndexError:
            break

def saveScreen(scene, key):
    global saveIni
    global saveList
    global saveKey
    global saveChara
    while True:
        num = 1
        index = 0
        print('\n' * 50)
        print('─' * 100)
        print('\n' * 2)
        for i in saveList:
            print(f'{num}. {saveList[index]}')
            num += 1
            index += 1
        print('\n' * 2)
        print('─' * 100)
        try:
            userIn = input('Which slot would you like to save in? (Type \'back\' to Cancel)   ')
            if userIn == '1':
                saveList[0] = textwrap.shorten(scene, 50, placeholder = '...')
                saveIni[0] = iniText
                saveKey[0] = key
                saveChara[0] = dict(charaDic)
                time.sleep(1)
                print('Saved')
                input()
                break
            elif userIn == '2':
                saveList[1] = textwrap.shorten(scene, 50, placeholder = '...')
                saveIni[1] = iniText
                saveKey[1] = key
                saveChara[1] = dict(charaDic)
                time.sleep(1)
                print('Saved')
                input()
                break
            elif userIn == '3':
                saveList[2] = textwrap.shorten(scene, 50, placeholder = '...')
                saveIni[2] = iniText
                saveKey[2] = key
                saveChara[2] = dict(charaDic)
                time.sleep(1)
                print('Saved')
                input()
                break
            elif userIn == '4':
                saveList[3] = textwrap.shorten(scene, 50, placeholder = '...')
                saveIni[3] = iniText
                saveKey[3] = key
                saveChara[3] = dict(charaDic)
                time.sleep(1)
                print('Saved')
                input()
                break
            elif userIn == '5':
                saveList[4] = textwrap.shorten(scene, 50, placeholder = '...')
                saveIni[4] = iniText
                saveKey[4] = key
                saveChara[4] = dict(charaDic)
                time.sleep(1)
                print('Saved')
                input()
                break
            elif userIn.lower() == 'back':
                time.sleep(1)
                print('Save Cancelled | Press \'Enter\' to Continue')
                input()
                break
            else:
                raise ValueError
        except:
            errorMsg()
            input()
            continue

def loadScreen():
    global iniText
    global saveList
    global saveIni
    global saveKey
    global saveChara
    global charaDic
    while True:
        num = 1
        index = 0
        print('\n' * 50)
        print('─' * 100)
        print('\n' * 2)
        for i in saveList:
            print(f'{num}. {saveList[index]}')
            num += 1
            index += 1
        print('\n' * 2)
        print('─' * 100)
        try:
            userIn = input('Which slot would you like to load? (Type \'back\' to Cancel)   ')
            if userIn == '1':
                if saveIni[0] == '':
                    raise ValueError
                iniText = saveIni[0]
                charaDic = saveChara[0]
                time.sleep(1)
                print('Loaded')
                iniText -= 1
                scenes(saveKey[0])
                break
            elif userIn == '2':
                if saveIni[1] == '':
                    raise ValueError
                iniText = saveIni[1]
                charaDic = saveChara[1]
                time.sleep(1)
                print('Loaded')
                iniText -= 1
                scenes(saveKey[1])
                break
            elif userIn == '3':
                if saveIni[2] == '':
                    raise ValueError
                iniText = saveIni[2]
                charaDic = saveChara[2]
                time.sleep(1)
                print('Loaded')
                iniText -= 1
                scenes(saveKey[2])
                break
            elif userIn == '4':
                if saveIni[3] == '':
                    raise ValueError
                iniText = saveIni[3]
                charaDic = saveChara[3]
                time.sleep(1)
                print('Loaded')
                iniText -= 1
                scenes(saveKey[3])
                break
            elif userIn == '5':
                if saveIni[4] == '':
                    raise ValueError
                iniText = saveIni[4]
                charaDic = saveChara[4]
                time.sleep(1)
                print('Loaded')
                iniText -= 1
                scenes(saveKey[4])
                break
            elif userIn.lower() == 'back':
                time.sleep(1)
                print('Load Cancelled | Press \'Enter\' to Continue')
                iniText -= 1
                input()
                break
            else:
                raise ValueError
        except:
            errorMsg()
            input()
            continue

def section_1():
    global iniText
    textDisplay(text.scene1(userName, iniText), 1)
    iniText = 0
    pathway_1()

def pathway_1():
    global iniText
    choice1 = choices(path.split1()[0], path.split1()[1], path.split1()[2])
    if choice1 == 1:
        section_1_1()
    elif choice1 == 2:
        section_1_2()
    iniText = 0
    section_2()

def section_1_1():
    global iniText
    textDisplay(path.outcome1(userName, iniText)[0], 'c1-1')

def section_1_2():
    global iniText
    textDisplay(path.outcome1(userName, iniText)[1], 'c1-2')

def section_2():
    global iniText
    textDisplay(text.scene2(userName, iniText), 2)
    iniText = 0
    pathway_2()

def pathway_2():
    global iniText
    global lisa
    choice2 = choices(path.split2()[0], path.split2()[1], path.split2()[2])
    if choice2 == 1:
        charaDic['lisa'] += 1
        section_2_1()
    elif choice2 == 2:
        section_2_2()
    iniText = 0

def section_2_1():
    global iniText
    textDisplay(text.scene2_1(userName, iniText), '2_1')

def section_2_2():
    global iniText
    textDisplay(text.scene2_2(userName, iniText), '2_2')

section_1()