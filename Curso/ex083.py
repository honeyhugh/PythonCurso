exp = input('Digite uma expressão: ').strip()
monte = []
for i in exp:
    if i == '(':
        monte.append('(')
    elif i == ')':
        if len(monte) > 0:
            monte.pop()
        else:
            monte.append(')')
            break
if len(monte) == 0:
    print('Sua expressão está correta :)')
else:
    print('Sua expressão está incorreta :(')
