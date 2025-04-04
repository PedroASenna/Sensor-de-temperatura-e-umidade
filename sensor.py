import random
import time
import matplotlib.pyplot as plt
from datetime import datetime

# Função para simular leituras do sensor
def ler_sensor():
    temperatura = round(random.uniform(20.0, 30.0), 1)
    umidade = round(random.uniform(40.0, 80.0), 1)
    return temperatura, umidade

# Coletar dados ao longo do tempo
dados = {'tempo': [], 'temperatura': [], 'umidade': []}

print("Iniciando coleta de dados...")
try:
    while True:
        temp, umid = ler_sensor()
        agora = datetime.now().strftime("%H:%M:%S")
        
        dados['tempo'].append(agora)
        dados['temperatura'].append(temp)
        dados['umidade'].append(umid)
        
        print(f"{agora} - Temperatura: {temp}°C, Umidade: {umid}%")
        
        # Plotar gráfico a cada 5 leituras
        if len(dados['tempo']) % 5 == 0:
            plt.figure(figsize=(10, 5))
            plt.plot(dados['tempo'], dados['temperatura'], label='Temperatura (°C)', marker='o')
            plt.plot(dados['tempo'], dados['umidade'], label='Umidade (%)', marker='x')
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        
        time.sleep(2)  # Intervalo de 2 segundos

except KeyboardInterrupt:
    print("\nColeta de dados encerrada.")