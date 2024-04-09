import csv
import random
import os

# Função para gerar um valor aleatório para uma coluna específica, caso necessitar de alguma coluna em especifico com valor nulo adicionar o "None" na lista.
# Para meus testes utilizei o IMC.
def generate_random_value(column):
    if column == 'idade':
        return random.choice([random.randint(18, 80)])
    elif column == 'gênero':
        return random.choice(['feminino', 'masculino'])
    elif column == 'imc':
        return random.choice([round(random.uniform(18.5, 40), 2), None])
    elif column == 'filhos':
        return random.choice([random.randint(0, 5)])
    elif column == 'fumante':
        return random.choice(['sim', 'não'])
    elif column == 'região':
        return random.choice(['nordeste', 'noroeste', 'sudeste', 'sudoeste'])
    elif column == 'encargos':
        return random.choice([round(random.uniform(10000, 50000), 2)])

# Lista das colunas do arquivo CSV
columns = ['idade', 'gênero', 'imc', 'filhos', 'fumante', 'região', 'encargos']

# Número de linhas a serem geradas
num_rows = 5000

# Diretório atual onde o script está sendo executado
current_directory = os.path.dirname(os.path.abspath(__file__))

# Nome do arquivo CSV de saída
output_file = os.path.join(current_directory, 'seguro_medico.csv')

# Abrir o arquivo CSV para escrita
with open(output_file, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    
    # Escrever o cabeçalho do arquivo CSV
    writer.writeheader()
    
    # Gerar e escrever as linhas aleatórias no arquivo CSV
    for _ in range(num_rows):
        row = {column: generate_random_value(column) for column in columns}
        writer.writerow(row)

print(f'Arquivo CSV "{output_file}" gerado com sucesso.')
