# 🌡️📊 Dashboard de Monitoramento de Sensores (Temperatura & Umidade)  

**Um dashboard interativo e visualmente atraente** para monitorar dados de sensores em tempo real, com gráficos animados, alertas personalizáveis e histórico de leituras.  

---

## 🚀 **Como Executar**  

1. **Clone o repositório** (ou copie o código):  
   ```bash
   git clone https://github.com/seu-usuario/sensor-dashboard.git
   cd sensor-dashboard
   ```

2. **Crie e ative um ambiente virtual** (recomendado):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências**:  
   ```bash
   pip install streamlit plotly pandas
   ```

4. **Execute o dashboard**:  
   ```bash
   streamlit run dashboard.py
   ```
   > O dashboard abrirá automaticamente no navegador em `http://localhost:8501`.

---

## ✨ **Recursos do Dashboard**  

### 📌 **Visualização em Tempo Real**  
- **Gráficos animados** de temperatura (°C) e umidade (%) usando Plotly.  
- **Métricas dinâmicas** com variação desde a última leitura.  
- **Tema escuro moderno** e layout responsivo.  

### ⚠️ **Alertas Personalizáveis**  
- Ajuste os limites de alerta para temperatura e umidade na sidebar.  
- Cores vermelhas indicam valores críticos.  

### ⚙️ **Controles Interativos**  
- **Slider** para definir o intervalo de atualização (1 a 10 segundos).  
- **Sidebar** com configurações rápidas.  

### 📈 **Dados Realistas**  
- Simulação inteligente: umidade varia inversamente à temperatura.  
- Histórico das últimas 50 leituras.  

---

## 🛠️ **Estrutura do Código**  

```plaintext
dashboard.py
├── Configuração do tema (Streamlit + CSS)
├── Função de simulação do sensor (ler_sensor())
├── Sidebar com controles
├── Layout principal (métricas + gráficos)
└── Loop de atualização em tempo real
```

---

## 📸 **Preview**  

![Dashboard Preview](https://via.placeholder.com/800x400/0E1117/FFFFFF?text=Dashboard+Interativo+com+Gráficos+Animados)  
*(Gráficos de linha com cores temáticas e métricas em destaque)*  

---

## 🧠 **Como Personalizar**  

1. **Conectar a um sensor físico** (ex: DHT22):  
   ```python
   # Substitua a função ler_sensor() por:
   import Adafruit_DHT
   def ler_sensor():
       umid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pino_sensor)
       return temp, umid
   ```

2. **Salvar dados em CSV**:  
   ```python
   st.session_state.dados.to_csv("historico_sensor.csv", index=False)
   ```

3. **Adicionar mais sensores**:  
   - Basta expandir o DataFrame com novas colunas (ex: `'CO2'`).  

---

## 📜 **Licença**  
MIT License - Livre para uso e modificação.  
