# Pipeline de Dados IoT

## Descrição
Projeto para processar leituras de temperatura de dispositivos IoT, armazenar em PostgreSQL via Docker e visualizar dados em um dashboard Streamlit.

## Tecnologias
- Python (pandas, SQLAlchemy, Streamlit, Plotly)
- PostgreSQL (Docker)
- Docker
- Git/GitHub

## Estrutura de Pastas
- `/data`: CSV com leituras de temperatura
- `/src`: Scripts Python
- `/sql`: Views SQL
- `/docs`: Documentação
- `docker-compose.yml`: Configuração PostgreSQL

## Execução
1. Suba o container PostgreSQL:
```bash
docker-compose up -d
```

2. Instale dependências Python:
```bash
pip install pandas sqlalchemy psycopg2-binary streamlit plotly
```

3. Processar dados e inserir no PostgreSQL:
```bash
python src/process_data.py
```

4. Criar views no PostgreSQL:
```bash
psql -U postgres -d iot_db -f sql/create_views.sql
```

5. Rodar dashboard:
```bash
streamlit run src/dashboard.py
```

## Insights
- Identificação de horários com maior atividade de leitura
- Dispositivos com temperaturas médias mais altas ou baixas
- Dias com picos de temperatura

## Comandos Git usados
```bash
git init
git add .
git commit -m "Projeto IoT inicial"
git push -u origin main
```