def split1():
    scenario = ['1. Coffee, the classic.', '2. Let\'s have some tea for a change.']
    return scenario, 1, 2

def outcome1(name, line):
    option1 = ['Of course it has to be coffee. No contest there.',
'User*Sip*... Ahhh, that\'s the good stuff. Can\'t go wrong with a good ol\' cup of joe']
    option2 = ['Haven\'t had a nice cup of tea in a while. Why not?',
'User*Sip*... Ah, something about tea in the morning is nice and calming. (Maybe I should drink it more often).']
    display1 = option1[line]
    display2 = option2[line]
    return display1, display2

def split2():
    scenario = ['1. I can\'t leave Lisa like that. I\'ve got to do what I can to help.', '2. There are other things I want to do, I can\'t \
work this much without going crazy.']
    return scenario, 1, 2

def split2_1():
    scenario = ['1. Have Ben connect me with some people.', '2. Find a new hobby to get into.', '3. Spend some \'me time\'.',
'4. I don\'t have to decide right now. Something will come to me.']
    return scenario, 1, 2, 3, 4