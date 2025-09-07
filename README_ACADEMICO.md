# 📡 Relatório do Projeto: Pipeline de Dados IoT

## 1. Contextualização
O crescimento da Internet das Coisas (IoT) gera enormes volumes de dados que precisam ser processados, armazenados e analisados de forma eficiente.  
Neste projeto foi construído um **pipeline de dados IoT** para demonstrar como leituras de sensores de temperatura podem ser integradas a um banco de dados, processadas e visualizadas em dashboards interativos.

---

## 2. Passos Realizados

### 🔧 Configuração do Ambiente
- Instalação do **Python** e criação de ambiente virtual (`venv`);
- Instalação de dependências com `pip install -r requirements.txt`;
- Instalação e configuração do **Docker** para rodar o PostgreSQL.

### 🐳 Criação do Container PostgreSQL
```bash
docker-compose up -d
```
Banco criado com:
- usuário: `postgres`
- senha: `42418214`
- database: `iot_db`

### 📝 Inserção dos Dados
- Arquivo CSV `data/temperature_readings.csv` com dados de dispositivos IoT.
- Script `src/process_data.py` lê o CSV, trata colunas e insere no PostgreSQL.

### 🗄️ Criação das Views SQL
Arquivo `sql/create_views.sql` contém três views:
1. `avg_temp_por_dispositivo`
2. `leituras_por_hora`
3. `temp_max_min_por_dia`

### 📊 Construção do Dashboard
- Script `src/dashboard.py` utiliza **Streamlit + Plotly** para criar gráficos interativos a partir das views SQL.

---

## 3. Explicação das Views SQL

1. **`avg_temp_por_dispositivo`**  
   Calcula a **média de temperatura por sensor**.  
   Útil para comparar sensores e identificar desvios.  

2. **`leituras_por_hora`**  
   Conta o **número de registros por hora do dia**.  
   Permite avaliar a frequência de coleta e detectar horários com falhas.  

3. **`temp_max_min_por_dia`**  
   Retorna a **temperatura máxima e mínima de cada dia**.  
   Importante para monitorar extremos e comportamentos anômalos.  

---

## 4. Visualizações no Dashboard
- **Gráfico 1:** Média de temperatura por dispositivo (barras)  
- **Gráfico 2:** Leituras por hora (linha)  
- **Gráfico 3:** Temperaturas máximas e mínimas por dia (linha dupla)  

*(prints disponíveis em `/docs/screenshots/` e no PDF `docs/Relatorio_Projeto_IoT.pdf`)*

---

## 5. Insights e Aplicações Reais
- Identificação de sensores com comportamento fora do padrão;  
- Monitoramento de ambientes críticos (refrigeração, estufas, data centers);  
- Geração de alertas automáticos em caso de temperaturas extremas;  
- Apoio a estratégias de **manutenção preditiva** e otimização de recursos energéticos.  

---

## 6. Conclusão
O projeto demonstrou um **pipeline de dados IoT completo**:  
- ingestão → armazenamento → processamento → visualização.  
Mostra como é possível transformar dados brutos de sensores em informações valiosas para tomada de decisão em tempo real.
