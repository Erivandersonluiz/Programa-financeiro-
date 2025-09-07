# app/db.py
import csv
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
DATA_PATH = BASE_PATH / "dados"

# Cria pasta "dados" se não existir
DATA_PATH.mkdir(exist_ok=True)

def salvar_csv(nome_arquivo, cabecalho, dados):
    """Salva uma linha em um CSV, criando o arquivo se não existir."""
    arquivo = DATA_PATH / nome_arquivo
    novo = not arquivo.exists()

    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if novo:
            writer.writerow(cabecalho)  # escreve cabeçalho só na 1ª vez
        writer.writerow(dados)
