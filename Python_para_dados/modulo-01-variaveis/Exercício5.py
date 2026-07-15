'''
Situação:
Recebemos uma variável com o nome de uma professora da escola para inserimos no cadastro. No entanto, precisamos tratar esse texto antes de inserirmos no sistema

texto = '  Geovana Alessandra dias Sanyos '

O objetivo final é que o nome esteja da seguinte forma:
'GEOVANA ALESSANDRA DIAS SANTOS'

'''
texto = '  Geovana Alessandra dias Sanyos '
print(f'Texto redefinido: {texto}')
print(f'Tipo após redefinição: {type(texto)}')

texto = texto.strip().replace('y','t').upper()
print(f'Texto processado: {texto}')