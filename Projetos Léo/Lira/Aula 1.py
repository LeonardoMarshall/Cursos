import pyautogui as pa
import pyperclip as pp
import pandas as pd
import time
import numpy
import openpyxl
from datetime import datetime

hora = datetime.now()


tabela = pd.read_excel (r"C:\Users\marca\OneDrive - UNIVALI\Ensino\Python\Intensivo\Aula 1\Vendas - Dez.xlsx")

print(tabela)

faturamento = tabela["Valor Final"].sum()
Quantidade = tabela["Quantidade"].sum()

pa.PAUSE = 1

pa.press("win")
pa.write("Outlook")
pa.press("enter")

time.sleep(5)


pa.click(x=71,y=85)
pa.write("marcalleo@hotmail.com.br")
pa.press("tab")
pa.press("tab")
pa.press("tab")
titulo = "Controle Diário de Vendas"
pp.copy(titulo)
pa.hotkey("ctrl","v")
pa.press("tab")
#print(pa.position())


texto = f"""Ola! 

segue relatório diário:
Faturamento: R$ {faturamento:,.2f}
Quantidade: R$ {Quantidade:,.2f}

Obrigado pela atenção!
Leonardo Flores Marçal
Momento da análise = {hora.hour}:{hora.minute}:{hora.second}"""

pp.copy(texto)
pa.hotkey("ctrl","v")
pa.hotkey("ctrl","enter")



