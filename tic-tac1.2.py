from tkinter import *
from datetime import datetime
import pyglet
import os

# Adicionar a fonte digital personalizada
#fonte_caminho = os.path.join(os.path.dirname(__file__), "digital-7.ttf")
#pyglet.font.add_file(fonte_caminho)

pyglet.font.add_file("digital-7.ttf")

##### Cores ########
cor1 = "#3d3d3d"  # preta
cor2 = "#FFFFFF"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelho
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor2

janela = Tk()
janela.title("Relógio Digital")
janela.geometry("400x180")
janela.resizable(width=FALSE, height=FALSE)
janela.config(bg=cor1)

# Função para atualizar o relógio
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    # Atualizar o texto do Label cx1 para mostrar a hora
    cx1.config(text=hora)
    # Atualizar o texto do Label cx2 para mostrar a data completa
    cx2.config(text=f"{dia_semana} {dia}/{mes}/{ano}")
    
    # Atualiza o relógio a cada segundo
    cx1.after(1000, relogio)

# Label para mostrar o relógio
cx1 = Label(janela, text="", font=("digital-7", 70), bg=fundo, fg=cor)
cx1.grid(row=0, column=0, sticky=NW, padx=5)

# Label para mostrar o dia, mês e ano
cx2 = Label(janela, text="", font=("digital-7.ttf", 20), bg=fundo, fg=cor)
cx2.grid(row=1, column=0, sticky=NW, padx=5)

# Inicia o relógio
relogio()

janela.mainloop()


#https://www.1001fonts.com/digital-7-font.html
#https://pypi.org/project/pyglet/