# ⚡️ Simulador PowerTrack
Este projeto é um protótipo de dashboard em tempo real para o projeto PowerTrack – monitoramento inteligente de energia , desenvolvido para a disciplina de Usina de Projetos Experimentais (UPx) do Centro Universitário Facens.


## 🎯Objetivo
O objetivo deste simulador é demonstrar a interface gráfica e a experiência do usuário final, conforme descrito nos objetivos do projeto, sem a necessidade do hardware físico (ESP32, sensores de corrente).

Além disso, este dashboard simula o "painel digital acessível por computador ou celular"  que o usuário final utilizaria para monitorar o consumo de energia de sua residência. Ele gera dados aleatórios, mas realistas, para diferentes cômodos/circuitos da casa, permitindo visualizar:
- **Consumo em Tempo Real**: Métricas atualizadas do consumo (em Watts) de cada setor monitorado.
- **Histórico de Consumo**: Um gráfico de linhas que mostra a variação do consumo ao longo do tempo.
- **Identificação de Picos**: A simulação inclui picos aleatórios para representar o acionamento de aparelhos de alto consumo (como o chuveiro), facilitando a visualização de "quais setores consomem mais".


## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)  
↪️ Linguagem principal utilizada no desenvolvimento do projeto.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)  
↪️ Usado para a criação rápida da interface web e do dashboard interativo.

![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)  
↪️ Responsável pela manipulação e estruturação dos dados históricos.

![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)  
↪️ Utilizado para a geração de dados aleatórios simulados.


## 🚀 Como Executar
1. **Pré-requisitos**  
Certifique-se de que você tem o Python 3 instalado em sua máquina.

2. **Instalação das Dependências**  
Abra seu terminal ou prompt de comando e instale as bibliotecas necessárias:
~~~
pip install streamlit pandas numpy
~~~

3. **Executando o Simulador**  
Salve o código do simulador em um arquivo chamado `simulador.py`.

- Navegue pelo terminal até a pasta onde você salvou o arquivo.
- Execute o seguinte comando:
~~~
streamlit run simulador.py
~~~
> O Streamlit abrirá automaticamente uma aba no seu navegador padrão, exibindo o dashboard.

3. 1 **Executando em outro sistema operacional**  
Caso você esteja em um sistema operacional Linux, abra a pasta onde está salvo o arquivo e execute o seguinte comando:
~~~
python3 -m streamlit run simulador.py
~~~
>O Streamlit abrirá normalmente pelo navegador padrão do usúario.

## 📊 O que você verá?
O dashboard apresentará um título e um conjunto de métricas e gráficos que se atualizam automaticamente a cada 5 segundos.

*Métricas e dados apresentados*:
- Consumo em Tempo Real por Cômodo/Setor:
    - Consumo Total: A soma de todos os circuitos;
    - Quarto Principal: Simula o consumo de aparelhos como Ar-Condicionado (com picos) e tomadas;
    - Cozinha: Simula o consumo de base (Geladeira) e picos (Micro-ondas, Airfryer);
    - Chuveiro: Simula um circuito dedicado que apresenta picos muito altos de forma intermitente;
    - Iluminação/Geral: Simula o consumo de luzes e tomadas de uso geral;
- Histórico de Consumo:
    - Um gráfico de linhas dinâmico que plota o histórico recente de consumo de cada um dos circuitos (exceto o "Total", para manter a escala).

>Este protótipo atende à validação do público-alvo de ter uma solução "intuitiva, com acesso remoto por aplicativo ou site".