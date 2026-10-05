-- Verificación del entorno: tabla de prueba en curso_data_analytics
CREATE TABLE prueba_entorno (
    id         SERIAL PRIMARY KEY,
    mensaje    TEXT NOT NULL,
    creado_en  TIMESTAMP DEFAULT now()
);

INSERT INTO prueba_entorno (mensaje)
VALUES ('Mi entorno de Data Analytics funciona');

SELECT * FROM prueba_entorno;
