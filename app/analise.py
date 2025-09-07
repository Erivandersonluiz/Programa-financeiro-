"""
# app/analise.py
import tkinter as tk

def tela_analise(frame):
    titulo = tk.Label(frame, text="Análise Financeira", font=("Arial", 16), bg="white")
    titulo.pack(pady=20)

    tk.Label(frame, text="Aqui você verá gráficos e análises de entradas/saídas.").pack(pady=10)

    # Exemplo de resultado fictício
    resumo = tk.Label(frame, text="Saldo atual: R$ 5000,00", fg="green", font=("Arial", 14))
    resumo.pack(pady=20)

    tk.Button(frame, text="Atualizar Análise", command=lambda: print("Análise atualizada!")).pack(pady=10)
"""
# codigo adicionado

# app/analise.py
import tkinter as tk

def tela_analise(frame):
    titulo = tk.Label(frame, text="Análise Financeira", font=("Arial", 16, "bold"), bg="white")
    titulo.pack(pady=20)

    resumo = tk.Label(frame, text="Saldo atual: R$ 5.000,00", fg="green", font=("Arial", 14, "bold"), bg="white")
    resumo.pack(pady=10)

    detalhe = tk.Label(frame, text="Entradas: R$ 8.000,00\nSaídas: R$ 3.000,00", bg="white", font=("Arial", 12))
    detalhe.pack(pady=10)

    atualizar_btn = tk.Button(
        frame, text="🔄 Atualizar", bg="#1E90FF", fg="white",
        font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5,
        command=lambda: print("Análise atualizada!")
    )
    atualizar_btn.pack(pady=20)
