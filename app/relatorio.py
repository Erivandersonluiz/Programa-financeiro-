"""
# app/relatorio.py
import tkinter as tk

def tela_relatorio(frame):
    titulo = tk.Label(frame, text="Relatórios Financeiros", font=("Arial", 16), bg="white")
    titulo.pack(pady=20)

    tk.Label(frame, text="Selecione o tipo de relatório:").pack(pady=5)

    tk.Button(frame, text="Relatório de Entradas", command=lambda: print("Gerar relatório de entradas")).pack(pady=5)
    tk.Button(frame, text="Relatório de Saídas", command=lambda: print("Gerar relatório de saídas")).pack(pady=5)
    tk.Button(frame, text="Relatório Geral", command=lambda: print("Gerar relatório geral")).pack(pady=5)
"""
# codigo adicionado
# app/relatorio.py
import tkinter as tk

def tela_relatorio(frame):
    titulo = tk.Label(frame, text="Relatórios Financeiros", font=("Arial", 16, "bold"), bg="white")
    titulo.pack(pady=20)

    botoes = [
        ("📊 Relatório de Entradas", "Gerar relatório de entradas"),
        ("📉 Relatório de Saídas", "Gerar relatório de saídas"),
        ("📑 Relatório Geral", "Gerar relatório geral")
    ]

    for texto, msg in botoes:
        btn = tk.Button(
            frame, text=texto, bg="#444", fg="white",
            font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5,
            command=lambda m=msg: print(m)
        )
        btn.pack(pady=8)
