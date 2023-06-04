import redis  # biblioteca utilizada para os comandos redis
import json  # biblioteca utilizada para formatar os dados das remessas

# Conecta ao servidor Redis com o IP e porta selecionados para o Redis
# Armazena a conexão na variável 'r'
r = redis.Redis(host='192.168.96.4', port=6379)

# Dados das remessas a serem enviadas
# Os dados são exemplos de como poderiam ser implementados em um centro de distribuição
remessas = [
    {
        "id": "123456",
        "origem": "Centro de Distribuição",
        "destino": "Agência São Paulo",
        "status": "Aguardando coleta"
    },
    {
        "id": "234567",
        "origem": "Centro de Distribuição",
        "destino": "Agência Rio de Janeiro",
        "status": "Aguardando coleta"
    },
    {
        "id": "345678",
        "origem": "Centro de Distribuição",
        "destino": "Agência Belo Horizonte",
        "status": "Aguardando coleta"
    },
    {
        "id": "456789",
        "origem": "Centro de Distribuição",
        "destino": "Agência Manaus",
        "status": "Aguardando coleta"
    }
]

# Envia as remessas para a fila
for remessa in remessas:  # percorre a lista
    remessa_str = json.dumps(remessa)  # converte os dados em uma string json para armazenar no Redis
    r.rpush('fila_remessas', remessa_str)  # utiliza o método rpush para adicionar a remessa à fila

    print("Remessa enviada:")  # imprime os dados cadastrados
    print(json.dumps(remessa, indent=4, ensure_ascii=False))  # formata os dados da remessa
    print()  # print para separar as remessas de forma a ficar agradável de analisar

# Obtem a quantidade de remessas enviadas utilizando o método llen
remessas_enviadas = r.llen('fila_remessas')
# Para uma análise quantitativa:
print("Métricas da MV1:")
print("Remessas enviadas:", remessas_enviadas)  # exibe a quantidade de remessas enviadas

# Obtem o tempo total de processamento através do método get
tempo_total = r.get('tempo_total')

# Verifica se tempo_total é None
if tempo_total is not None:  # Verifica se o tempo total foi diferente de None. Caso contrário, não há dados disponíveis
    tempo_total = float(tempo_total)  # converte o valor em float
    print("Tempo total de processamento:", tempo_total, "segundos")
else:
    print("Tempo total de processamento: N/A")
