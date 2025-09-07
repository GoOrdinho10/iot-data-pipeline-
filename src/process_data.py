import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco (ajuste user, senha e DB se necessário)
engine = create_engine('postgresql://postgres:42418214@localhost:5432/iot_db')

# Lê o CSV
df = pd.read_csv('data/temperature_readings.csv')

# Normaliza nomes das colunas
df.columns = [c.lower() for c in df.columns]

# Converte timestamp para datetime se existir
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])

# Insere os dados na tabela (troque para append se não quiser sobrescrever)
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("✅ Dados inseridos na tabela temperature_readings com sucesso!")
