# 📡 IoT Data Pipeline — Docker + PostgreSQL + Streamlit

## 🎯 Objetivo
Este projeto implementa um **pipeline de dados IoT** que:
1. Lê dados de temperatura de dispositivos IoT (arquivo CSV);
2. Armazena no banco de dados PostgreSQL (via Docker);
3. Cria *views* SQL para análises;
4. Exibe visualizações interativas em um dashboard com **Streamlit + Plotly**.

---

## 🧱 Tecnologias Utilizadas
- **Python** (pandas, SQLAlchemy, psycopg2-binary, Streamlit, Plotly)  
- **PostgreSQL** (rodando em container **Docker**)  
- **Git/GitHub** para versionamento e entrega  

---

## 📂 Estrutura do Projeto
```
iot-data-pipeline/
├─ data/                      # CSVs (adicione seu dataset aqui)
├─ docs/                      # documentação e prints do dashboard
│  ├─ screenshots/
│  └─ Relatorio_Projeto_IoT.pdf
├─ sql/                       # scripts SQL
│  └─ create_views.sql
├─ src/                       # código-fonte
│  ├─ process_data.py
│  └─ dashboard.py
├─ docker-compose.yml         # container PostgreSQL
├─ requirements.txt           # dependências Python
└─ README.md
```

---

## 🚀 Como Executar

### 1) Subir PostgreSQL com Docker
```bash
docker-compose up -d
```

### 2) Criar ambiente Python e instalar dependências
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```

### 3) Inserir os dados no banco
Coloque o CSV em `data/temperature_readings.csv` e rode:
```bash
python src/process_data.py
```

### 4) Criar/atualizar views (opcional, já carregam via Docker)
```bash
psql -U postgres -d iot_db -f sql/create_views.sql
```

### 5) Rodar o dashboard
```bash
streamlit run src/dashboard.py
```

---

## 🧠 Views SQL
- **`avg_temp_por_dispositivo`** → média de temperatura por dispositivo.  
- **`leituras_por_hora`** → número de leituras por hora do dia.  
- **`temp_max_min_por_dia`** → temperaturas máximas e mínimas por dia.  

---

## 🖼️ Prints do Dashboard
Exemplos em `docs/screenshots/`:

- Média de temperatura por dispositivo  
- Leituras por hora  
- Máximas e mínimas por dia  

---

## 🗃️ Base de Dados
- Kaggle: [Temperature Readings: IoT Devices](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices)  
- Ou use `data/temperature_readings.csv` (arquivo de exemplo incluído).  

---

## 🔧 Comandos Git usados
```bash
git init
git add .
git commit -m "feat: pipeline IoT com Docker, PostgreSQL e Streamlit"
git branch -M main
git remote add origin https://github.com/GoOrdinho10/iot-data-pipeline.git
git push -u origin main
```
