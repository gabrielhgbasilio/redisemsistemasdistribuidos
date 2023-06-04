import redis  # biblioteca utilizada para os comandos redis
import json  # biblioteca utilizada para formatar os dados das remessas
import time  # biblioteca utilizada para análise quantitativa

# Conecta ao servidor Redis com o IP e porta selecionados para o Redis
# Armazena a conexão na variável 'r'
r = redis.Redis(host='192.168.96.4', port=6379)

# Função para processar uma remessa
def processar_remessa(remessa):
    # Formata os dados recebidos para uma string
    remessa_str = json.dumps(remessa)
    print("Processando remessa:")
    print(json.dumps(remessa, indent=4, ensure_ascii=False))  # formatação
    print()  # print para separar as remessas que estão sendo processadas para facilitar a visualização

    # Simula o processamento da remessa com o tempo de 1 segundo para cada processamento
    time.sleep(1)

    # Atualiza o status da remessa processada
    remessa['status'] = f"Enviado para {remessa['destino']}"

    print("Remessa processada:")
    print(json.dumps(remessa, indent=4, ensure_ascii=False))
    print()

    # Retorna a remessa processada
    return remessa

# Limpa a chave 'remessas_processadas' antes de iniciar o processamento
r.delete('remessas_processadas')

# Loop principal para processar remessas
while True:
    # Obtém uma remessa da fila de remessas
    remessa_str = r.lpop('fila_remessas')

    if remessa_str is not None:  # Se houver remessa, entra no if
        remessa = json.loads(remessa_str)  # converte para um objeto python
        remessa_processada = processar_remessa(remessa)  # processa e obtém a remessa processada

        # Adiciona a remessa processada à lista de remessas processadas utilizando rpush
        r.rpush('remessas_processadas', json.dumps(remessa_processada))
    else:
        # Não há mais remessas na fila, então interrompe o loop
        break

# Verifica se a chave 'remessas_processadas' contém uma lista
tipo_valor = r.type('remessas_processadas')  # identifica o tipo do dado contido na chave
if tipo_valor == b'list':  # verifica se é do tipo bytes para ver se é do tipo lista
    # Obtém a quantidade de remessas processadas
    remessas_processadas = r.llen('remessas_processadas')

    # Para uma análise quantitativa:
    print("Métricas da MV2:")
    print("Remessas processadas:", remessas_processadas)  # exibe a quantidade de remessas processadas

    # Obtém o tempo total de processamento através do método r.get
    tempo_total = r.get('tempo_total')

    # Se existir valor, converte para float e calcula a média do tempo de processamento
    if tempo_total is not None:
        tempo_total = float(tempo_total)
        media_tempo_processamento = tempo_total / remessas_processadas
        print("Média dos tempos de processamento:", media_tempo_processamento)
    else:
        print("Erro: O valor do tempo total de processamento não foi encontrado.")
else:
    print("Erro: A chave 'remessas_processadas' não contém uma lista.")
