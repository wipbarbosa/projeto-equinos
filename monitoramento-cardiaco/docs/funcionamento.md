# Monitoramento Cardíaco Equino — Funcionamento do Sistema

## 1. Visão geral

O sistema de monitoramento cardíaco equino será desenvolvido utilizando a tecnologia de eletrocardiograma (ECG), permitindo capturar os sinais elétricos do coração do animal e acompanhar sua frequência cardíaca.

O funcionamento será baseado na integração entre sensores, microcontrolador, comunicação de dados, banco de dados e uma aplicação responsável pela apresentação das informações.

O ESP32-WROOM-32 será utilizado como unidade de processamento e comunicação, enquanto o módulo AD8232 será responsável pela aquisição e condicionamento dos sinais cardíacos.

## 2. Arquitetura do sistema

O sistema será dividido em cinco etapas principais:

1. Captura dos sinais cardíacos.
2. Processamento dos sinais pelo ESP32.
3. Transmissão dos dados.
4. Armazenamento no banco de dados.
5. Apresentação das informações na aplicação.

## 3. Etapa 1 — Captura dos sinais cardíacos

A primeira etapa consiste na aquisição dos sinais elétricos produzidos pelo coração do cavalo.

Para isso, serão utilizados:

- Eletrodos ECG: posicionados em contato com a pele do animal.
- AD8232: módulo responsável por receber e amplificar os sinais elétricos captados pelos eletrodos.

O AD8232 disponibilizará um sinal analógico que poderá ser lido pelo ESP32.

A qualidade da captura dependerá do posicionamento dos eletrodos, da fixação e das condições de contato com a pele.

## 4. Etapa 2 — Processamento pelo ESP32

O ESP32-WROOM-32 será responsável por receber os sinais provenientes do AD8232 e realizar o processamento necessário para identificar os batimentos cardíacos.

As principais atividades dessa etapa serão:

- Realizar a leitura do sinal analógico.
- Analisar as variações do sinal cardíaco.
- Identificar os picos correspondentes aos batimentos.
- Calcular a frequência cardíaca em batimentos por minuto (BPM).
- Preparar os dados para transmissão.

O processamento deverá considerar possíveis interferências e ruídos presentes nos sinais capturados.

## 5. Etapa 3 — Transmissão dos dados

Após o processamento, o ESP32 será responsável por transmitir as informações para a aplicação.

Inicialmente, serão consideradas duas possibilidades:

**Wi-Fi:** permite enviar os dados para um computador ou servidor conectado à mesma rede ou a uma infraestrutura de comunicação disponível.

**Bluetooth:** permite estabelecer comunicação direta com outro dispositivo compatível.

A escolha definitiva dependerá dos testes realizados e das condições de utilização do sistema.

As informações transmitidas poderão incluir:

- Identificação do dispositivo.
- Frequência cardíaca em BPM.
- Data e horário da medição.
- Situação da conexão.

## 6. Etapa 4 — Armazenamento no banco de dados

Os dados recebidos pela aplicação serão armazenados em um banco de dados, permitindo manter o histórico de monitoramento dos animais.

O armazenamento deverá relacionar as medições ao respectivo cavalo e registrar o momento em que foram realizadas.

Entre as informações armazenadas estão:

- Identificação do cavalo.
- Frequência cardíaca registrada.
- Data e horário da medição.
- Identificação do dispositivo utilizado.

Esses registros permitirão consultar medições anteriores e acompanhar a evolução da frequência cardíaca de cada animal.

## 7. Etapa 5 — Apresentação das informações

A aplicação contará com um dashboard para apresentar os dados recebidos e armazenados.

As principais informações disponíveis serão:

- Frequência cardíaca atual.
- Gráfico de acompanhamento em tempo real.
- Histórico de medições.
- Valores mínimos, máximos e médios.
- Identificação do animal monitorado.
- Alertas de possíveis alterações.
- Situação da conexão com o dispositivo.

A interface deverá permitir que os responsáveis acompanhem os animais e consultem informações de monitoramentos anteriores.

## 8. Fluxo geral de funcionamento

O fluxo completo do sistema seguirá esta sequência:

1. Os eletrodos captam a atividade elétrica do coração.
2. O AD8232 recebe e amplifica os sinais.
3. O ESP32 realiza a leitura do sinal.
4. O ESP32 processa os dados e calcula os BPM.
5. As informações são transmitidas por Wi-Fi ou Bluetooth.
6. A aplicação recebe os dados.
7. Os registros são armazenados no banco de dados.
8. O dashboard apresenta as informações ao usuário.

## 9. Frequência de atualização

A proposta inicial é realizar o monitoramento continuamente, com atualização dos resultados apresentados entre 1 e 5 segundos.

Esse intervalo deverá ser avaliado durante os testes, considerando a qualidade dos sinais, o processamento e a comunicação entre os dispositivos.

## 10. Testes e validação

O desenvolvimento será realizado de forma gradual, começando pela validação dos componentes de hardware.

### 10.1. Teste do AD8232

- Verificar se o módulo está recebendo os sinais dos eletrodos.
- Observar o sinal analógico disponibilizado pelo sensor.
- Avaliar a presença de ruídos e interferências.

### 10.2. Teste do ESP32

- Verificar a leitura dos sinais provenientes do AD8232.
- Testar o processamento dos sinais.
- Desenvolver e avaliar o cálculo da frequência cardíaca.

### 10.3. Teste de comunicação

- Verificar a transmissão dos dados.
- Avaliar a estabilidade da conexão.
- Identificar possíveis perdas ou interrupções.

### 10.4. Teste integrado

- Integrar o hardware à aplicação.
- Verificar o recebimento e armazenamento das medições.
- Avaliar a apresentação dos dados no dashboard.

### 10.5. Testes com equinos

Inicialmente, os testes deverão ser realizados com o animal parado, buscando garantir uma captura adequada dos sinais.

Posteriormente, poderão ser realizados testes em diferentes situações, como repouso, atividade física e recuperação, com acompanhamento e validação veterinária.

## 11. Diagrama simplificado do funcionamento

```text
       CAVALO
          |
          v
    ELETRODOS ECG
          |
          v
       AD8232
  (Condicionamento)
          |
          v
        ESP32
 (Leitura e processamento)
          |
          v
  WI-FI / BLUETOOTH
          |
          v
      APLICAÇÃO
          |
          v
    BANCO DE DADOS
          |
          v
      DASHBOARD
          |
          v
 VISUALIZAÇÃO DOS DADOS
```

## 12. Considerações finais

O funcionamento do sistema será baseado na integração entre aquisição de sinais cardíacos, processamento eletrônico e apresentação digital das informações.

A primeira etapa prática será desenvolver o circuito utilizando o ESP32-WROOM-32 e o AD8232, realizando testes de captura e leitura dos sinais pelo computador.

Após validar essa etapa, o desenvolvimento poderá avançar para o processamento dos batimentos, transmissão dos dados, armazenamento e construção do dashboard.

O sistema terá finalidade experimental e de apoio ao monitoramento, não substituindo avaliações ou diagnósticos veterinários.