# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- **Nome completo:** Theógenes Gabriel Araújo de Andrade
- **GitHub:** https://github.com/TheogenesGabriel

---

## Visão Geral da Solução

O projeto simula um sistema de monitoramento para um ambiente refrigerado (tipo geladeira/estufa), alertando sobre porta aberta por muito tempo e variação brusca de temperatura. O ESP32 lê continuamente um sensor de temperatura e um botão que simula a porta, imprimindo mensagens de status no Serial Monitor. Não há interação direta do usuário: o comportamento é acionado pelas mudanças simuladas nos sensores durante o teste.


## Arquitetura do Sistema Embarcado

O firmware é organizado em quatro estados, cada um implementado como uma função dedicada e chamada explicitamente no `main()`. O loop principal é não-bloqueante, usando `time.ticks_ms()`/`time.ticks_diff()` para todas as temporizações, com um único `time.sleep_ms(50)` de tick — sem `sleep` de segundos em nenhum ponto. Além disso, o firmware é dividido em quatro estados, cada um em uma função própria, chamados em sequência dentro de um loop principal não-bloqueante. O botão alimenta os Estados B e C (tempo de porta aberta e condição para atualizar a referência térmica). O MPU6050 alimenta o Estado C (leitura de temperatura). O Estado D só normaliza quando porta e temperatura estão OK ao mesmo tempo.
git 

## Componentes Utilizados na Simulação

A placa é uma **ESP32 DevKit C v4**, que executa o firmware. O **MPU6050** funciona como sensor de temperatura, lido via I2C (GPIO21/22). O **botão** (`btn1`) simula a porta, ligado ao GPIO27 com pull-up interno: pressionado = fechada, solto = aberta. Os pinos TX/RX enviam as mensagens de status ao Serial Monitor.


---

## Decisões Técnicas Relevantes

O código foi dividido em **quatro estados** (A–D), cada um em uma função própria, seguindo o cenário do `TEMPERATURE.md`. Não há **drivers externos**: o sensor é lido diretamente via I2C, usando só módulos nativos do MicroPython. Toda a **temporização é não-bloqueante**, com `ticks_ms`/`ticks_diff` no lugar de `sleep` longo. As **mensagens de status** ficam como constantes fixas, copiadas literalmente do cenário, para evitar erro de digitação. A **temperatura de referência** é congelada durante o alarme térmico, evitando que ele se resolva sozinho.

## Resultados Obtidos

A lógica foi validada isoladamente e reproduziu a sequência esperada: porta aberta, alerta em 5 segundos, fechamento e normalização, com mensagens exatas. Um erro de fiação no `diagram.json` (botão ligado ao 3V3 em vez de GND) foi encontrado e corrigido, restaurando a leitura correta do botão. Após a correção, todos os requisitos críticos foram atendidos: strings exatas, código não-bloqueante e estados alinhados ao cenário.


## Comentários Adicionais (Opcional)

A principal dificuldade encontrada foi perceber que o bug de normalização não estava na lógica do firmware, e sim na fiação do `diagram.json`, o que reforça a importância de validar hardware e software separadamente antes de assumir que o problema está necessariamente no código. Como limitação observada, o intervalo de leitura periódica de 200 ms introduz uma pequena margem de atraso na detecção de transições de abertura e fechamento da porta, o que pode ser relevante caso o teste exija tolerância de tempo muito estreita; como melhoria futura, reduzir o `INTERVALO_LEITURA_MS` para algo entre 50 e 100 ms aumentaria a precisão de temporização sem custo relevante de desempenho no ESP32. O principal aprendizado do desafio foi que manter as mensagens de status como constantes centralizadas, e separar claramente os estados do sistema em funções nomeadas, tornou a depuração muito mais rápida, permitindo conferir o alinhamento entre o cenário, o `diagram.json` e o `main.py` item a item.


> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
