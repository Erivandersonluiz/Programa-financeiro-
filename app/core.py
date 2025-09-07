# app/core.py

azul_padrao = "#1E90FF"
cinza_claro = "#f0f0f0"

def limpar_frame(frame):
    """Remove todos os widgets de um frame."""
    for widget in frame.winfo_children():
        widget.destroy()
