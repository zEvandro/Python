"""
Nessa aula , vamos aprender como utilizar os códigos de escape sequence ANSI,
para configurar cores para os seus programas em python.
Veja como utilizar o código \33[m com todas as suas principais possibilidades.
"""

# CORES NO PYTHON
"""
\033[m --> codigo de cores

     text
       ↑
\033[0:0:0m → back
     ↓
  style



>>>>STYLE
# Código de comportamento

0 → none → significa sem estilo nenhum.
1 → bold → vai colocar em negrito.
4 → underline → vai coloca o texto sublinhado.
7 → negative → vai inverter as cores: oque você colocou pra fundo vai pra letra e vice-versa.


>>>>TEXTO(cores)
# Código do texto

30 → Preto
31 → Vermelho
32 → Verde
33 → Amarelo
34 → Azul
35 → Magenta(lilás)
36 → Ciano(azul claro)
37 → Cinza


>>>>BACK 
# Codigo da cor de fundo

40 → Branco
41 → Vermelho
42 → Verde
43 → Amarelo
44 → Azul
45 → Magenta(lilás)
46 → Ciano(azul claro)
47 → Cinza

"""
# \033[0:30:41m
# \033[4:33:44m
# \033[0:35:43m
# \033[30:42m
# \033[m
# \033[7:30m → letra preta e fundo branco.

print('\033[7:33mOlá Mundo!\033[m')