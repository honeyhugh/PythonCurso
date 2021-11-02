# tive que ver o prof fazendo
print('Descubra se um número é primo ou não')
n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
print('Esse número foi dividido {} vezes.'.format(total))
if total == 2:
    print('Portanto, ele é primo.')
else:
    print('Portanto, ele não é primo.')