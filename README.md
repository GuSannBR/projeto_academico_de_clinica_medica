SISTEMA CLÍNICA VIDA+
---

📅 Projeto Integrado - 2025
👨‍💻 Autor: Luis Gustavo Santos
📚 Curso: Analise e Desenvolvimento de Sistemas
🏫 Instituição: ANHANGUERA EDUCACIONAL
💾 Linguagem: Python
📁 Versão: 1.0

---

## 🩺 DESCRIÇÃO DO PROJETO

O sistema "Clínica Vida+" foi desenvolvido para auxiliar no
cadastro e gerenciamento de pacientes em uma clínica médica.

Com ele, é possível:

* Cadastrar pacientes (nome, idade, telefone e e-mail)
* Calcular estatísticas gerais (total, média de idade, mais novo e mais velho)
* Buscar pacientes pelo nome
* Editar e excluir cadastros
* Listar todos os pacientes
* Gerar um relatório em PDF com todos os dados e estatísticas

Os dados são armazenados em um arquivo JSON, garantindo
que as informações permaneçam salvas mesmo após o fechamento
do programa.

---

## ⚙️ REQUISITOS TÉCNICOS

* Python 3.8 ou superior
* Biblioteca `reportlab` (para gerar relatórios em PDF)

Para instalar o `reportlab`, execute no terminal:
pip install reportlab

---

## ▶️ COMO EXECUTAR O SISTEMA

1. Certifique-se de ter o Python instalado no computador.
2. Salve todos os arquivos na mesma pasta:

   * sistema_clinica.py
   * pacientes.json  (será criado automaticamente)
   * logo.png        (opcional)
3. Execute o programa pelo terminal ou editor de código:
   python sistema_clinica.py
4. Escolha uma das opções do menu principal:

   1. Cadastrar paciente
   2. Ver estatísticas
   3. Buscar paciente
   4. Listar todos os pacientes
   5. Editar paciente
   6. Excluir paciente
   7. Gerar relatório PDF
   8. Sair

---

## 📊 ESTRUTURA DE DADOS

Os dados dos pacientes são armazenados em listas e dicionários:

Exemplo:
[
{
"nome": "João Silva",
"idade": 45,
"telefone": "(11) 99999-9999",
"email": "[joao@gmail.com](mailto:joao@gmail.com)"
}
]

---

## 📄 RELATÓRIO PDF

O relatório inclui:

* Cabeçalho com logotipo (opcional)
* Tabela com todos os pacientes cadastrados
* Estatísticas (total, média de idade, mais novo, mais velho)
* Arquivo gerado: "relatorio_clinica.pdf"

---

## 🧩 DIFERENCIAIS DO PROJETO

✔ Código totalmente comentado e documentado
✔ Estrutura original e personalizada
✔ Campo adicional de e-mail
✔ Geração automática de relatórios em PDF
✔ Salvamento permanente em JSON
✔ Tratamento de erros de entrada

---

## 🧠 SOBRE O AUTOR

Luis Gustavo Santos é estudante dedicado à área de tecnologia
e desenvolvimento de sistemas.
Este projeto foi criado com o objetivo de aplicar os
conceitos de programação estruturada e manipulação de dados
em Python em um contexto realista e funcional.

Contato: [www.linkedin.com/in/gusannbr]

---

## 🚀 FIM DO DOCUMENTO

# Obrigado por utilizar o Sistema Clínica Vida+!
