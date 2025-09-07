"""
# app/viagem.py
import tkinter as tk

def tela_viagem(frame):
    titulo = tk.Label(frame, text="Planejamento de Viagem", font=("Arial", 16), bg="white")
    titulo.pack(pady=20)

    tk.Label(frame, text="Destino:").pack()
    destino = tk.Entry(frame)
    destino.pack()

    tk.Label(frame, text="Orçamento:").pack()
    orcamento = tk.Entry(frame)
    orcamento.pack()

    tk.Label(frame, text="Data da Viagem:").pack()
    data = tk.Entry(frame)
    data.pack()

    tk.Button(frame, text="Salvar Viagem", command=lambda: print("Viagem salva!")).pack(pady=10)
"""
# codigo adicionado
# app/viagem.py
import tkinter as tk

def tela_viagem(frame):
    titulo = tk.Label(frame, text="Planejamento de Viagem", font=("Arial", 16, "bold"), bg="white")
    titulo.pack(pady=20)

    form = tk.Frame(frame, bg="white")
    form.pack(pady=10)

    tk.Label(form, text="Destino:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    destino = tk.Entry(form, width=30)
    destino.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Orçamento:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    orcamento = tk.Entry(form, width=20)
    orcamento.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form, text="Data:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    data = tk.Entry(form, width=15)
    data.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    salvar_btn = tk.Button(
        frame, text="✈️ Salvar Viagem", bg="#8A2BE2", fg="white",
        font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5,
        command=lambda: print(f"Viagem: {destino.get()} - R$ {orcamento.get()} em {data.get()}")
    )
    salvar_btn.pack(pady=20)
