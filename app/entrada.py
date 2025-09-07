"""
# app/entrada.py
import tkinter as tk
from tkinter import ttk

def tela_entrada(frame):
    titulo = tk.Label(frame, text="Entrada de Valores", font=("Arial", 16), bg="white")
    titulo.pack(pady=20)

    tk.Label(frame, text="Descrição:").pack()
    descricao = tk.Entry(frame)
    descricao.pack()

    tk.Label(frame, text="Valor:").pack()
    valor = tk.Entry(frame)
    valor.pack()

    tk.Button(frame, text="Salvar", command=lambda: print("Valor salvo!")).pack(pady=10)
"""
"""
# app/entrada.py
import tkinter as tk
from tkinter import ttk

def tela_entrada(frame):
    # Título
    titulo = tk.Label(frame, text="Entrada de Valores", font=("Arial", 16, "bold"), bg="white")
    titulo.pack(pady=20)

    # Container para formulário
    form = tk.Frame(frame, bg="white")
    form.pack(pady=10)

    # Campo Descrição
    tk.Label(form, text="Descrição:", bg="white", anchor="w").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    descricao = tk.Entry(form, width=40)
    descricao.grid(row=0, column=1, padx=5, pady=5)

    # Campo Valor
    tk.Label(form, text="Valor:", bg="white", anchor="w").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    valor = tk.Entry(form, width=20)
    valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # Botão
    salvar_btn = tk.Button(
        frame,
        text="💾 Salvar",
        bg="#1E90FF", fg="white",
        font=("Arial", 12, "bold"),
        relief="flat",
        padx=10, pady=5,
        command=lambda: print(f"Valor salvo! {descricao.get()} - {valor.get()}")
    )
    salvar_btn.pack(pady=20)
"""
#tualizado o codigo
import tkinter as tk
from app import db

def tela_entrada(frame):
    titulo = tk.Label(frame, text="Entrada de Valores", font=("Arial", 16, "bold"), bg="white")
    titulo.pack(pady=20)

    form = tk.Frame(frame, bg="white")
    form.pack(pady=10)

    tk.Label(form, text="Descrição:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    descricao = tk.Entry(form, width=40)
    descricao.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Valor:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    valor = tk.Entry(form, width=20)
    valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    def salvar():
        db.salvar_csv("entradas.csv", ["Descrição", "Valor"], [descricao.get(), valor.get()])
        print(f"Entrada salva: {descricao.get()} - R$ {valor.get()}")

    tk.Button(frame, text="💾 Salvar", bg="#1E90FF", fg="white",
              font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5,
              command=salvar).pack(pady=20)
