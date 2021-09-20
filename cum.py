userInp = str(input('text')).lower()
find = str(input('find')).lower()
replace = str(input('replace'))

outcome = userInp.replace(find, replace)
outcome = userInp.replace(find.upper(), replace)
outcome = userInp.replace(find.capitalize(), replace)

print(outcome)