'''
Temos uma tabela de informação de empregos quanto ao cargo, quantidade de pessoas empregadas e o salário correspondente:

|Cargo     | Quantidade | Salário|
|Segurança | 5          | 3000   |
|Docente   | 16         | 6000   |
|Diretoria | 1          | 12500  |

Precisamos trabalhar com esses dados fornecendo:

- A quantidade total de empregados;
- A diferença entre o salário mais baixo e mais alto;
- A média ponderada da faixa salarial da escola.

'''
#A quantidade total de empregados
q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

q_total_empregados = (q_seguranca + q_docente + q_diretoria)
print( 'A quantidade total de empregados é:', q_total_empregados)

#A diferença entre o salário mais baixo e mais alto
D_Salarial = (s_diretoria - s_seguranca)
print('A diferença entre o salário mais baixo e mais alto é:', D_Salarial)

#A média ponderada da faixa salarial da escola.
M_ponderada_salarios = (q_seguranca * s_seguranca + q_docente * s_docente + q_diretoria * s_diretoria) / (q_seguranca + q_docente + q_diretoria)
print(' A média ponderada dos salários entre os empregados é:', M_ponderada_salarios)