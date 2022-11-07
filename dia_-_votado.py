segunda = int(input('Informe quantos alunos votaram na segunda: '))
terça =  int(input('Informe quantos alunos votaram na terça: '))
quarta = int(input('Informe quantos alunos votaram na quarta: '))
quinta = int(input('Informe quantos alunos votaram na quinta: '))
sexta = int(input('Informe quantos alunos votaram na sexta: '))

if (segunda >= terça) and (segunda >= quarta) and (segunda >= quinta) and (segunda >= sexta):
    input(f'Segunda-Feira foi o dia mais votado para as lives! Total de votos {segunda + terça + quarta + quinta + sexta}')
elif (terça >= segunda) and (terça >= quarta) and (terça >= quinta) and (terça >= sexta):
    input(f'Terça-Feira foi o dia mais votado para as lives! Total de votos {segunda + terça + quarta + quinta + sexta}' ) 
elif (quarta >= terça) and (quarta >= segunda) and (quarta >= quinta) and (quarta >= sexta):
    input(f'Quarta-Feira foi o dia mais votado para as lives! Total de votos {segunda + terça + quarta + quinta + sexta}')
elif (quinta >= terça) and (quinta >= quarta) and (quinta >= segunda) and (quinta >= sexta):
    input(f'Quinta-Feira foi o dia mais votado para fazer as lives! Total de votos {segunda + terça + quarta + quinta + sexta}')
elif (sexta >= terça) and (sexta >= quarta) and (sexta >= quinta) and (sexta >= segunda):
    input(f'Sexta-Feira foi o dia mais votado para as lives! Total de votos {segunda + terça + quarta + quinta + sexta}')
