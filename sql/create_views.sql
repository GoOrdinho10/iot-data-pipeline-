-- Média de temperatura por dispositivo
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT 
    device_id, 
    AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;

-- Leituras por hora
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT 
    EXTRACT(HOUR FROM timestamp) AS hora, 
    COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- Temperaturas máximas e mínimas por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT 
    DATE_TRUNC('day', timestamp) AS data,   -- => timestamp no início do dia (meia-noite)
    MAX(temperature) AS temp_max, 
    MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY DATE_TRUNC('day', timestamp)
ORDER BY data;

