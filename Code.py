# ==============================================================
# PROJETO INTEGRADO - 2025
# SISTEMA CLÍNICA VIDA+
# Autor: Luis Gustavo Santos
# Curso: Projeto Integrado Inovação
# Data: Dezembro de 2025
# --------------------------------------------------------------
# Descrição:
# Este programa simula o sistema de uma clínica médica que permite:
# - Cadastrar pacientes (nome, idade, telefone, e-mail)
# - Consultar estatísticas da base de pacientes
# - Buscar e listar cadastros
# - Editar e excluir informações
# - Gerar relatório em PDF com logotipo e estatísticas
#
# Tecnologias utilizadas:
# - Python (linguagem principal)
# - JSON (armazenamento de dados)
# - ReportLab (geração de PDF)
# ==============================================================

import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

# --------------------------------------------------------------
# Constantes globais (arquivos de dados e imagem)
# --------------------------------------------------------------
ARQUIVO = "pacientes.json"
RELATORIO = "relatorio_clinica.pdf"
LOGO = "logo.png"  # logotipo da clínica

# --------------------------------------------------------------
# Funções auxiliares para salvar e carregar dados
# --------------------------------------------------------------
def carregar_pacientes():
    """Lê o arquivo JSON com os pacientes cadastrados"""
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de pacientes. Um novo será criado.")
            return []
    return []

def salvar_pacientes(pacientes):
    """Grava os dados dos pacientes no arquivo JSON"""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=4)

# --------------------------------------------------------------
# Funções principais do sistema
# --------------------------------------------------------------
def cadastrar_paciente(pacientes):
    """Permite o cadastro de um novo paciente"""
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome completo: ").strip()
    if not nome:
        print("Erro: nome não pode ser vazio.")
        return

    try:
        idade = int(input("Idade: "))
        if idade <= 0:
            print("Erro: idade deve ser positiva.")
            return
    except ValueError:
        print("Erro: idade inválida (use números inteiros).")
        return

    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email
    }

    pacientes.append(paciente)
    salvar_pacientes(pacientes)
    print(f"Paciente '{nome}' cadastrado com sucesso!")

def ver_estatisticas(pacientes):
    """Calcula e exibe informações gerais dos pacientes"""
    print("\n--- Estatísticas da Clínica ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    idade_media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {idade_media:.1f} anos")
    print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente(pacientes):
    """Permite buscar um paciente pelo nome"""
    print("\n--- Buscar Paciente ---")
    termo = input("Digite o nome (ou parte dele): ").strip().lower()

    resultados = [p for p in pacientes if termo in p["nome"].lower()]
    if resultados:
        for p in resultados:
            print(f"\nNome: {p['nome']}")
            print(f"Idade: {p['idade']}")
            print(f"Telefone: {p['telefone']}")
            print(f"E-mail: {p['email']}")
    else:
        print("Nenhum paciente encontrado.")

def listar_pacientes(pacientes):
    """Exibe todos os pacientes cadastrados"""
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} - {p['idade']} anos - Tel: {p['telefone']} - E-mail: {p['email']}")

def editar_paciente(pacientes):
    """Permite alterar dados de um paciente existente"""
    listar_pacientes(pacientes)
    if not pacientes:
        return

    try:
        indice = int(input("\nNúmero do paciente para editar: ")) - 1
        if indice < 0 or indice >= len(pacientes):
            print("Número inválido.")
            return
    except ValueError:
        print("Erro: digite um número válido.")
        return

    paciente = pacientes[indice]
    print(f"\nEditando paciente: {paciente['nome']}")

    paciente["nome"] = input(f"Novo nome ({paciente['nome']}): ").strip() or paciente["nome"]
    try:
        nova_idade = input(f"Nova idade ({paciente['idade']}): ").strip()
        paciente["idade"] = int(nova_idade) if nova_idade else paciente["idade"]
    except ValueError:
        print("Erro: idade inválida.")
        return

    paciente["telefone"] = input(f"Novo telefone ({paciente['telefone']}): ").strip() or paciente["telefone"]
    paciente["email"] = input(f"Novo e-mail ({paciente['email']}): ").strip() or paciente["email"]

    salvar_pacientes(pacientes)
    print("Dados atualizados com sucesso!")

def excluir_paciente(pacientes):
    """Remove um paciente do cadastro"""
    listar_pacientes(pacientes)
    if not pacientes:
        return

    try:
        indice = int(input("\nNúmero do paciente para excluir: ")) - 1
        if indice < 0 or indice >= len(pacientes):
            print("Número inválido.")
            return
    except ValueError:
        print("Erro: entrada inválida.")
        return

    removido = pacientes.pop(indice)
    salvar_pacientes(pacientes)
    print(f"Paciente '{removido['nome']}' removido com sucesso!")

# --------------------------------------------------------------
# Função para gerar relatório PDF
# --------------------------------------------------------------

def gerar_relatorio(pacientes):
    """Gera um relatório em PDF com os dados e estatísticas"""
    if not pacientes:
        print("Nenhum paciente cadastrado para gerar relatório.")
        return

    doc = SimpleDocTemplate(RELATORIO, pagesize=A4)
    estilos = getSampleStyleSheet()
    elementos = []

    # Adiciona logotipo
    if os.path.exists(LOGO):
        logo = Image(LOGO, width=100, height=100)
        logo.hAlign = "CENTER"
        elementos.append(logo)
        elementos.append(Spacer(1, 10))

    elementos.append(Paragraph("Clínica Vida+ - Relatório de Pacientes", estilos["Title"]))
    elementos.append(Spacer(1, 20))

    # Monta tabela de pacientes
    dados = [["Nome", "Idade", "Telefone", "E-mail"]]
    for p in pacientes:
        dados.append([p["nome"], str(p["idade"]), p["telefone"], p["email"]])

    tabela = Table(dados)
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elementos.append(tabela)
    elementos.append(Spacer(1, 20))

    # Estatísticas
    idades = [p["idade"] for p in pacientes]
    total = len(pacientes)
    idade_media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    resumo = f"""
    <b>Total de pacientes:</b> {total}<br/>
    <b>Idade média:</b> {idade_media:.1f} anos<br/>
    <b>Mais novo:</b> {mais_novo['nome']} ({mais_novo['idade']} anos)<br/>
    <b>Mais velho:</b> {mais_velho['nome']} ({mais_velho['idade']} anos)
    """
    elementos.append(Paragraph(resumo, estilos["Normal"]))

    doc.build(elementos)
    print(f"\nRelatório gerado com sucesso: {RELATORIO}")

# --------------------------------------------------------------
# Menu principal do sistema
# --------------------------------------------------------------
def iniciar_sistema():
    pacientes = carregar_pacientes()

    while True:
        print("\n=== SISTEMA CLINICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatisticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Editar paciente")
        print("6. Excluir paciente")
        print("7. Gerar relatorio PDF")
        print("8. Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            ver_estatisticas(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            listar_pacientes(pacientes)
        elif opcao == "5":
            editar_paciente(pacientes)
        elif opcao == "6":
            excluir_paciente(pacientes)
        elif opcao == "7":
            gerar_relatorio(pacientes)
        elif opcao == "8":
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# --------------------------------------------------------------
# Execução do programa principal
# --------------------------------------------------------------
if __name__ == "__main__":
    iniciar_sistema()
