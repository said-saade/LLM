## aula 79 do curso de AI
import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext

# =======================
# CONFIGURAÇÃO DO GEMINI
# =======================
load_dotenv(find_dotenv())
api_key = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# =======================
# FUNÇÃO PARA CHAMAR LLM
# =======================
def consultar_llm():
    pergunta = entrada_texto.get("1.0", tk.END).strip()
    if not pergunta:
        exibir_resposta("Por favor, digite uma pergunta.")
        return

    try:
        resposta_texto = ""
        stream = model.generate_content(pergunta, stream=True)
        for chunk in stream:
            resposta_texto += chunk.text

        exibir_resposta(resposta_texto)

    except Exception as e:
        exibir_resposta(f"Erro ao consultar o LLM: {str(e)}")

# ========================
# FUNÇÃO PARA EXIBIR RESPOSTA
# ========================
def exibir_resposta(texto):
    caixa_resposta.config(state=tk.NORMAL)
    caixa_resposta.delete("1.0", tk.END)
    caixa_resposta.insert(tk.END, texto)
    caixa_resposta.config(state=tk.DISABLED)

# ========================
# FUNÇÃO PARA LIMPAR
# ========================
def limpar_tela():
    entrada_texto.delete("1.0", tk.END)
    caixa_resposta.config(state=tk.NORMAL)
    caixa_resposta.delete("1.0", tk.END)
    caixa_resposta.config(state=tk.DISABLED)

# =======================
# INTERFACE GRÁFICA TKINTER
# =======================
janela = tk.Tk()
janela.title("Consulta LLM - Gemini")

# Caixa de entrada (pergunta)
label_pergunta = tk.Label(janela, text="Digite sua pergunta para o LLM:")
label_pergunta.pack(pady=5)

entrada_texto = scrolledtext.ScrolledText(janela, width=60, height=5)
entrada_texto.pack(padx=10, pady=5)

# Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

botao_submeter = tk.Button(frame_botoes, text="Submeter", command=consultar_llm)
botao_submeter.grid(row=0, column=0, padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_tela)
botao_limpar.grid(row=0, column=1, padx=5)

# Caixa de resposta
label_resposta = tk.Label(janela, text="Resposta do LLM:")
label_resposta.pack(pady=5)

caixa_resposta = scrolledtext.ScrolledText(janela, width=60, height=10, state=tk.DISABLED)
caixa_resposta.pack(padx=10, pady=5)

# Iniciar interface
janela.mainloop()
