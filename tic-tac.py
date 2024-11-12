from tkinter import*
import tkinter 
from datetime import datetime


##### Cores ########

cor1 = "#3d3d3d" #preta
cor2 = "#faafcff" #branca
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelho
cor5 = "#dedcdc" #cinza
cor6 = "#3080f0" #azul

fundo = cor1
cor = cor2

janela = Tk()
janela.title("Relógio Digital")
janela.geometry("400x180")
janela.resizable(width=FALSE, height=FALSE)
janela.config(bg = cor1)

tempo= datetime.now()

hora=tempo.strftime("%H:%M, %S")
dia_semana=tempo.strftime("%A")
dia=tempo.day
mes=tempo.strftime("%b")
ano=tempo.strftime("%Y")


janela.mainloop()

