# app/main.py
import tkinter as tk
from tkinter import ttk

from app import entrada, saida, parcelas, viagem, analise, relatorio
from app.core import azul_padrao


# Função para carregar o frame selecionado
def carregar_frame(frame_func):
    for widget in frame_principal.winfo_children():
        widget.destroy()
    frame_func(frame_principal)


# Janela principal
root = tk.Tk()
root.title("Finança de Casa")
root.geometry("900x600")
root.configure(bg="white")

# Header azul
header = tk.Frame(root, bg=azul_padrao, height=50)
header.pack(fill="x")

titulo = tk.Label(
    header, text="Finança de Casa", bg=azul_padrao, fg="white", font=("Arial", 18)
)
titulo.pack(pady=10)

# Menu lateral
menu = tk.Frame(root, bg="#f0f0f0", width=200)
menu.pack(fill="y", side="left")

# Botões de navegação
botoes = [
    ("Entrada", entrada.tela_entrada),
    ("Saída", saida.tela_saida),
    ("Parcelas", parcelas.tela_parcelas),
    ("Viagem", viagem.tela_viagem),
    ("Análise", analise.tela_analise),
    ("Relatório", relatorio.tela_relatorio),
]
"""
for texto, comando in botoes:
    btn = tk.Button(menu, text=texto, command=lambda c=comando: carregar_frame(c), width=20)
    btn.pack(pady=5, padx=10)
"""
#texto adicionado
for texto, comando in botoes:
    btn = tk.Button(
        menu,
        text=texto,
        command=lambda c=comando: carregar_frame(c),
        width=20,
        bg="white",
        relief="flat",
        font=("Arial", 12)
    )
    btn.pack(pady=8, padx=10)


# Frame principal onde os módulos são exibidos
frame_principal = tk.Frame(root, bg="white")
frame_principal.pack(fill="both", expand=True)

root.mainloop()
