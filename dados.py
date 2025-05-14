import csv
import os
import re

ARQUIVO = 'dados.csv'

def normalizar_telefone(telefone):
    """Remove todos os caracteres que não são números."""
    return re.sub(r'\D', '', str(telefone))


def adicionar_dados(dados):
    try:
        with open(ARQUIVO, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(dados)
    except Exception as e:
        print(f"Erro ao adicionar dados: {e}")


def ver_dados_com_indices():
    """Retorna dados do CSV com seus índices (posições originais)."""
    if not os.path.exists(ARQUIVO):
        return []

    dados = []
    try:
        with open(ARQUIVO, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if row:
                    dados.append((i, row))
    except Exception as e:
        print(f"Erro ao ler dados com índice: {e}")
    return dados


def remover_dados(indices_para_remover):
    """Remove linhas com base nos índices exatos no arquivo."""
    try:
        with open(ARQUIVO, 'r', newline='', encoding='utf-8') as arquivo:
            linhas = list(csv.reader(arquivo))
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")
        return

    nova_lista = [linha for i, linha in enumerate(linhas) if i not in indices_para_remover]

    try:
        with open(ARQUIVO, 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(nova_lista)
        print(f"{len(indices_para_remover)} linha(s) removida(s).")
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")


def atualizar_dados(dados_atualizados):
    telefone_original = normalizar_telefone(dados_atualizados[0])
    dados_novos = dados_atualizados[1:]
    nova_lista = []
    atualizado = False

    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3:
                    telefone_existente = normalizar_telefone(row[2])
                    if telefone_original == telefone_existente:
                        nova_lista.append(dados_novos)
                        atualizado = True
                    else:
                        nova_lista.append(row)

        if atualizado:
            with open(ARQUIVO, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(nova_lista)
        else:
            print("Telefone original não encontrado para atualização.")

    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")

    return atualizado


def pesquisar_dados(termo):
    if not termo:
        return []

    termo = termo.lower()
    resultados = []

    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if any(termo in campo.lower() for campo in row):
                    resultados.append(row)
    except Exception as e:
        print(f"Erro ao pesquisar dados: {e}")

    return resultados