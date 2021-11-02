frase = input('Digite a frase: ').strip().upper()
print('A frase possui {} letras "a", cuja primeira se localiza na posição {} e a segunda na {}'.format(frase.count('A'), frase.find('A') + 1, frase.rfind('A') + 1))
