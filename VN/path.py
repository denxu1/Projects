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