-- Monitoramento Cardíaco Equino — rode este script no MySQL Workbench (raio, na parte superior)
CREATE DATABASE IF NOT EXISTS equino
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE equino;

CREATE TABLE IF NOT EXISTS cavalos (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    nome      VARCHAR(80) NOT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dispositivos (
    id        VARCHAR(50) PRIMARY KEY,
    cavalo_id INT NULL,
    CONSTRAINT fk_disp_cavalo FOREIGN KEY (cavalo_id)
        REFERENCES cavalos (id) ON DELETE SET NULL
);

-- Horários guardados no fuso de Brasília (America/Sao_Paulo)
CREATE TABLE IF NOT EXISTS medicoes (
    id             BIGINT AUTO_INCREMENT PRIMARY KEY,
    cavalo_id      INT NOT NULL,
    dispositivo_id VARCHAR(50) NOT NULL,
    bpm            SMALLINT NOT NULL,
    signal_ok      TINYINT(1) NOT NULL DEFAULT 1,
    criado_em      DATETIME NOT NULL,
    CONSTRAINT fk_med_cavalo FOREIGN KEY (cavalo_id) REFERENCES cavalos (id),
    CONSTRAINT fk_med_disp   FOREIGN KEY (dispositivo_id) REFERENCES dispositivos (id),
    INDEX idx_cavalo_tempo (cavalo_id, criado_em)
);

-- Dados de demonstração (só insere se ainda não houver cavalos)
INSERT INTO cavalos (nome)
SELECT 'Trovão' FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM cavalos);

INSERT IGNORE INTO dispositivos (id, cavalo_id)
SELECT 'esp32-01', MIN(id) FROM cavalos;