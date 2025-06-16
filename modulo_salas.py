
salas = [
    {
        "nome_sala": "sala 01",
        "sessoes": [
            {
                'id_sala': 'S01',
                'horario_inicio': "10:30",
                'horario_termino': '12:00',
                'filme': 'os vingadores',
            },
            {
                'id_sala': 'S01',
                'horario_inicio': "10:30",
                'horario_termino': '12:00',
                'filme': 'os 101 dalmatas',
            } ,
        ]
    }
]

def cadastra_sala():
    nome_sala = input("Digite o nome da sala de cinema: ")
    
    for i in range(3):
        
        horario_inicio_sessao = input(f"Digite o horario de inicio da {i}º sessão da sala {i}: ")
        horario_termino_sessao = input(f"Digite o horario de termino da {i}º sessão da sala {i}: ")
        
        sessao = {
            'id_sala': 'S01',
            'horario_inicio': horario_inicio_sessao,
            'horario_termino': horario_termino_sessao,
        }

        sessoes = {
            'sessao': sessao
        }
        
        sala = {
            "nome_sala": nome_sala,
            'sessoes': sessoes,
        }
        
        salas.append(sala)