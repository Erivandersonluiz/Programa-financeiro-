"""
# app/parcelas.py
import tkinter as tk

def tela_parcelas(frame):
    titulo = tk.Label(frame, text="Controle de Parcelas", font=("Arial", 16), bg="white")
    titulo.pack(pady=20)

    tk.Label(frame, text="Descrição da Parcela:").pack()
    descricao = tk.Entry(frame)
    descricao.pack()

    tk.Label(frame, text="Valor da Parcela:").pack()
    valor = tk.Entry(frame)
    valor.pack()

    tk.Label(frame, text="Quantidade de Parcelas:").pack()
    qtd = tk.Entry(frame)
    qtd.pack()

    tk.Button(frame, text="Salvar", command=lambda: print("Parcela salva!")).pack(pady=10)
"""
# codigo adicionado

# app/parcelas.py
import tkinter as tk

def tela_parcelas(frame):
    titulo = tk.Label(frame, text="Controle de Parcelas", font=("Arial", 16, "bold"), bg="white")
    titulo.pack(pady=20)

    form = tk.Frame(frame, bg="white")
    form.pack(pady=10)

    tk.Label(form, text="Descrição:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    descricao = tk.Entry(form, width=40)
    descricao.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Valor da Parcela:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    valor = tk.Entry(form, width=20)
    valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(form, text="Quantidade:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    qtd = tk.Entry(form, width=10)
    qtd.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    salvar_btn = tk.Button(
        frame, text="📑 Salvar Parcelas", bg="#228B22", fg="white",
        font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5,
        command=lambda: print(f"Parcela: {descricao.get()} - {qtd.get()}x de R$ {valor.get()}")
    )
    salvar_btn.pack(pady=20)

