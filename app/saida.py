"""
# app/saida.py
import tkinter as tk

def tela_saida(frame):
    titulo = tk.Label(frame, text="Saída de Valores", font=("Arial", 16), bg="white")
    titulo.pack(pady=20)

    tk.Label(frame, text="Descrição:").pack()
    descricao = tk.Entry(frame)
    descricao.pack()

    tk.Label(frame, text="Valor:").pack()
    valor = tk.Entry(frame)
    valor.pack()

    tk.Button(frame, text="Registrar Saída", command=lambda: print("Saída registrada!")).pack(pady=10)
"""
# codigo adicionado
# app/saida.py
import tkinter as tk

def tela_saida(frame):
    titulo = tk.Label(frame, text="Saída de Valores", font=("Arial", 16, "bold"), bg="white")
    titulo.pack(pady=20)

    form = tk.Frame(frame, bg="white")
    form.pack(pady=10)

    tk.Label(form, text="Descrição:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    descricao = tk.Entry(form, width=40)
    descricao.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Valor:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    valor = tk.Entry(form, width=20)
    valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    salvar_btn = tk.Button(
        frame, text="➖ Registrar Saída", bg="#FF4500", fg="white",
        font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5,
        command=lambda: print(f"Saída: {descricao.get()} - R$ {valor.get()}")
    )
    salvar_btn.pack(pady=20)
