# Projeto de Monitoramento de Equinos

## Sobre o projeto

O **Projeto de Monitoramento de Equinos** tem como objetivo desenvolver soluções tecnológicas voltadas ao acompanhamento da saúde e do bem-estar de cavalos, utilizando conceitos de Internet das Coisas (IoT), sensores, processamento de dados e visão computacional.

O projeto está dividido em dois subprojetos independentes, cada um com suas próprias funcionalidades, tecnologias, códigos e estruturas de banco de dados.

## Subprojetos

### 1. Monitoramento Cardíaco Equino

Desenvolvimento de um sistema capaz de monitorar a frequência cardíaca dos equinos, permitindo acompanhar os batimentos por minuto (BPM), registrar o histórico de medições e identificar possíveis alterações que mereçam atenção.

**Principais tecnologias e componentes:**
- ESP32-WROOM-32
- Sensor ECG AD8232
- Eletrodos para captura dos sinais cardíacos
- Comunicação Wi-Fi ou Bluetooth
- Banco de dados para armazenamento das medições
- Dashboard para visualização dos resultados

[ Acessar Monitoramento Cardíaco](./monitoramento-cardiaco/)

### 2. Monitoramento de Pré-Parto Equino

Desenvolvimento de um sistema para acompanhar alterações físicas e comportamentais das éguas durante o período que antecede o parto, buscando identificar sinais que possam indicar sua aproximação.

A proposta envolve o monitoramento por imagens e o uso de processamento computacional para identificar possíveis alterações na região vulvar.

**Principais tecnologias e componentes:**
- Raspberry Pi
- Câmera com visão noturna
- ESP32 (quando necessário)
- Visão computacional
- Processamento e armazenamento de imagens
- Sistema de alertas

[ Acessar Monitoramento Pré-Parto](./monitoramento-pre-parto/)

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| ESP32 | Coleta e transmissão de dados |
| Raspberry Pi | Processamento de imagens |
| Python | Desenvolvimento e processamento |
| SQL | Armazenamento de informações |
| IoT | Comunicação entre dispositivos |
| Visão computacional | Análise de imagens |

## Organização do repositório

O repositório está organizado para manter os dois subprojetos separados, facilitando o desenvolvimento, a manutenção e a documentação.

- `docs/` — Pesquisas, requisitos e documentação geral.
- `monitoramento-cardiaco/` — Código, hardware, banco de dados e documentação do monitoramento cardíaco.
- `monitoramento-pre-parto/` — Código, hardware, banco de dados e documentação do monitoramento de pré-parto.

Cada subprojeto possui sua própria estrutura de desenvolvimento e documentação.

## Objetivo geral

Desenvolver soluções tecnológicas que contribuam para o monitoramento de equinos, permitindo a coleta, o armazenamento e a visualização de informações relevantes para o acompanhamento dos animais.

---

**Projeto de Monitoramento de Equinos**

Desenvolvimento de soluções tecnológicas aplicadas à saúde e ao bem-estar animal.