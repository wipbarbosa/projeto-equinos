# Monitoramento Cardíaco Equino

## 1. Sobre o projeto

O projeto consiste no desenvolvimento de um sistema capaz de monitorar a frequência cardíaca de equinos, permitindo acompanhar os batimentos por minuto (BPM), registrar o histórico de medições e identificar possíveis alterações que mereçam atenção.

A proposta utiliza sensores de eletrocardiograma (ECG) conectados a um microcontrolador ESP32, responsável pela coleta e transmissão dos dados para uma aplicação que permitirá visualizar e armazenar as informações.

## 2. Objetivo geral

Desenvolver um protótipo de monitoramento cardíaco equino que permita acompanhar a frequência cardíaca dos animais em diferentes situações, como repouso, atividade física e recuperação.

O sistema deverá possibilitar o acompanhamento das medições em tempo real, a consulta ao histórico e a identificação de possíveis alterações na frequência cardíaca.

## 3. Tecnologias e componentes

| Componente | Função |
|---|---|
| ESP32-WROOM-32 | Receber e processar os dados do sensor e realizar a comunicação. |
| AD8232 | Capturar e amplificar os sinais elétricos cardíacos. |
| Eletrodos ECG | Realizar o contato com o animal para captar os sinais cardíacos. |
| Bateria | Fornecer alimentação ao dispositivo. |
| Cinta ou suporte | Permitir a fixação dos sensores no animal. |
| Computador ou servidor | Receber e disponibilizar os dados para a aplicação. |

### 3.1. Tecnologia de monitoramento

A tecnologia escolhida inicialmente será o ECG (Eletrocardiograma), que permite captar a atividade elétrica do coração por meio de eletrodos posicionados no animal.

O módulo AD8232 será utilizado como parte do circuito de aquisição do sinal, enquanto o ESP32 ficará responsável pela leitura e transmissão das informações.

O protótipo será desenvolvido inicialmente com o animal parado, permitindo avaliar a qualidade dos sinais capturados antes de avançar para testes com movimentação.

## 4. Requisitos funcionais (RF)

Os requisitos funcionais representam as funcionalidades que o sistema deverá oferecer.

| Código | Requisito |
|---|---|
| RF01 | Permitir cadastrar e identificar os cavalos monitorados. |
| RF02 | Receber os sinais cardíacos capturados pelo sensor AD8232. |
| RF03 | Processar os sinais para calcular a frequência cardíaca em BPM. |
| RF04 | Exibir a frequência cardíaca do animal em tempo real. |
| RF05 | Armazenar o histórico das medições no banco de dados. |
| RF06 | Apresentar gráficos e relatórios das medições realizadas. |
| RF07 | Identificar possíveis alterações na frequência cardíaca conforme parâmetros definidos. |
| RF08 | Gerar alertas sobre possíveis alterações identificadas. |
| RF09 | Identificar falhas de conexão ou interrupções no recebimento dos dados. |
| RF10 | Permitir consultar o histórico de monitoramento de cada animal. |

## 5. Requisitos não funcionais (RNF)

Os requisitos não funcionais representam características de qualidade e funcionamento esperadas para o sistema.

| Código | Requisito |
|---|---|
| RNF01 | O sistema deverá permitir a transmissão dos dados por Wi-Fi ou Bluetooth. |
| RNF02 | A aplicação deverá apresentar os dados de maneira clara e organizada. |
| RNF03 | O sistema deverá armazenar as medições associadas ao respectivo animal e horário de coleta. |
| RNF04 | O dispositivo deverá permitir funcionamento contínuo durante os períodos de monitoramento planejados. |
| RNF05 | O sistema deverá possuir mecanismos para identificar falhas na comunicação entre os dispositivos. |
| RNF06 | O armazenamento deverá preservar o histórico das medições realizadas. |

## 6. Funcionamento esperado

O funcionamento geral do sistema deverá seguir as seguintes etapas:

1. Os eletrodos captam os sinais elétricos do coração do cavalo.
2. O módulo AD8232 recebe e condiciona os sinais.
3. O ESP32 realiza a leitura dos dados.
4. O processamento identifica os batimentos e calcula a frequência cardíaca.
5. Os dados são transmitidos para a aplicação.
6. O sistema armazena as medições no banco de dados.
7. O dashboard apresenta os resultados e o histórico do animal.

## 7. Informações apresentadas pelo sistema

A aplicação deverá disponibilizar informações que permitam acompanhar o estado do monitoramento.

- Identificação do cavalo.
- Frequência cardíaca atual em BPM.
- Gráfico de acompanhamento cardíaco.
- Histórico de medições.
- Valores mínimos, máximos e médios registrados.
- Data e horário das medições.
- Alertas de possíveis alterações.
- Situação da conexão com o dispositivo.

## 8. Situações de monitoramento

O sistema deverá considerar três situações principais:

**Repouso:** acompanhamento da frequência cardíaca habitual do animal.

**Atividade física:** observação das alterações cardíacas durante exercícios.

**Recuperação:** acompanhamento do comportamento da frequência cardíaca após atividades físicas ou durante períodos de observação.

Como referência inicial, cavalos adultos em repouso normalmente apresentam frequência cardíaca entre 28 e 44 BPM. Esse intervalo não deverá ser utilizado isoladamente para determinar alterações clínicas, pois os parâmetros podem variar conforme o animal e as circunstâncias.

## 9. Limitações e considerações

O projeto será desenvolvido inicialmente como um protótipo experimental.

Algumas limitações que deverão ser consideradas:

- A movimentação do animal pode gerar interferências nos sinais capturados.
- Será necessário avaliar o posicionamento e a fixação dos eletrodos.
- O processamento dos sinais deverá ser desenvolvido para identificar corretamente os batimentos.
- As medições deverão ser comparadas com equipamentos de referência.
- Os parâmetros utilizados para alertas deverão ser avaliados com acompanhamento veterinário.

O sistema tem finalidade de monitoramento e apoio à observação, não substituindo exames ou avaliações veterinárias.

## 10. Considerações finais

O monitoramento cardíaco equino busca integrar sensores eletrônicos, processamento de dados e uma aplicação digital para acompanhar a frequência cardíaca dos animais.

A primeira etapa do desenvolvimento será construir e testar o circuito utilizando o ESP32-WROOM-32 e o AD8232, verificando a qualidade dos sinais capturados.

Posteriormente, serão desenvolvidos os mecanismos de processamento, comunicação, armazenamento e visualização dos dados.