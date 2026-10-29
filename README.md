
# 💸 Sistema de Automação de Troco (Cashier Flow)

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Projeto-Acadêmico-orange?style=for-the-badge)](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque)

## 📝 Descrição do Projeto

O Sistema de Automação de Troco é um projeto de lógica de programação voltado à simulação de transações financeiras em pontos de venda. Seu principal objetivo é validar pagamentos, calcular o troco e determinar a quantidade de cédulas necessárias para devolver o valor ao cliente.

O algoritmo verifica se o valor pago é suficiente para cobrir o custo da compra. Quando o pagamento é válido, calcula a diferença e decompõe o troco utilizando operações matemáticas de divisão inteira e resto.

## ⚙️ Funcionalidades e Lógica

- 💳 **Validação de Pagamento:** verifica se o valor recebido é suficiente para pagar a compra.
- 🧮 **Cálculo de Troco:** subtrai o valor da compra do pagamento recebido.
- 💵 **Decomposição de Cédulas:** calcula a quantidade de notas de R$ 100, R$ 50, R$ 10, R$ 5 e R$ 1.
- ⚠️ **Tratamento de Pagamento Insuficiente:** apresenta uma mensagem quando o valor pago não cobre a compra.
- ✅ **Validação de Valores:** impede o processamento de valores negativos.

## 🚀 Tecnologias Utilizadas

- 🐍 **Linguagem:** Python 3.10 ou superior.
- 🧠 **Conceitos:** funções, estruturas condicionais, operadores aritméticos, divisão inteira (`//`) e resto da divisão (`%`).
- 💻 **Ambiente de execução:** terminal, Visual Studio Code ou Google Colab.

## 📊 Estrutura de Decomposição

O algoritmo utiliza uma sequência de divisões para calcular a quantidade de cédulas de cada valor:

| Cédula | Operação |
|---|---|
| R$ 100 | `troco // 100` |
| R$ 50 | `troco_restante // 50` |
| R$ 10 | `troco_restante // 10` |
| R$ 5 | `troco_restante // 5` |
| R$ 1 | `troco_restante // 1` |

Após calcular cada quantidade, o valor correspondente é subtraído do saldo restante para determinar as próximas cédulas.

## 🔧 Como Executar

### 📋 Pré-requisitos

- Python 3.10 ou superior instalado na máquina.

### ▶️ Passo a Passo

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/cashier-flow.git
```

**2. Acesse a pasta do projeto**

```bash
cd cashier-flow
```

**3. Execute o programa**

```bash
python troco.py
```

**4. Informe os valores**

Digite o valor total da compra e o valor pago pelo cliente. O sistema calculará o troco e exibirá a quantidade de cédulas de cada denominação.

## 📂 Estrutura do Projeto

```text
cashier-flow/
├── README.md
└── troco.py
```

- 📘 `README.md`: documentação do projeto.
- 🐍 `troco.py`: código Python responsável pela validação do pagamento e pelo cálculo do troco.

## 💻 Acesse o Projeto

🐍 **[Visualizar código-fonte (main.py)](main.py)**

📁 **[Acessar portfólio no GitHub](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque/tree/main)**

## 👤 Autor

**Matheus Chagas Mauriz Coque**

🎓 Estudante de Engenharia de Software

- 💼 [LinkedIn](https://www.linkedin.com/in/matheus-chagas-coque-b190ba39b/)
- 🐙 [GitHub](https://github.com/chagasmatheus1211)
- 📧 [E-mail](mailto:chagasmatheus1211@gmail.com)

---

⭐ *Projeto acadêmico com foco em lógica de programação, cálculos financeiros, validação de pagamentos e decomposição de valores monetários.*

⬅️ **[Voltar ao portfólio principal](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque/tree/main)**
