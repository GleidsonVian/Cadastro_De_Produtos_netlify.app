from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tkinter import *
from tkinter import ttk
import sys


def iniciar_preenchimento():
  # Carregar os dados da planilha
  produtos = pd.read_excel(r"C:\pasta4\Python\projeto site dev aprender\produtos.xlsx")

  # Inicializar o driver do Chrome
  driver = webdriver.Chrome()
  driver.get("https://cadastroprodutos-devaprender.netlify.app/")

  # Preencher o formulário com os itens da planilha
  for i in range(int(len(produtos))):
    produto = driver.find_element(By.XPATH, "//input[@name='first_name']")
    produto.send_keys(produtos.iloc[i, 0])  # Preencher o primeiro item da primeira coluna

    fornecedor = driver.find_element(By.XPATH, "//input[@name='last_name']")
    fornecedor.send_keys(produtos.iloc[i, 1])  # Preencher o primeiro item da segunda coluna

    categoria = driver.find_element(By.XPATH, "//input[@name='categoria']")
    categoria.send_keys(produtos.iloc[i, 2])  # Preencher o primeiro item da terceira coluna

    valorUnitario = driver.find_element(By.XPATH, "//input[@name='email']")
    valorUnitario.send_keys(str(produtos.iloc[i, 3]))  # Preencher o primeiro item da quarta coluna

    registrarProduto = driver.find_element(By.XPATH, "//button[@class='btn btn--radius-2 btn--blue']")
    registrarProduto.click()

    # Aguardar o alerta e aceitá-lo
    time.sleep(0.3)  # Espera 0,5 segundos para que o alerta apareça
    driver.switch_to.alert.accept()

  # Fechar o navegador
  driver.quit()

def cancelar():
  tela.destroy() #fecha a janela do tkinter
  sys.exit() #fecha o programa pra nao rodar

tela = Tk()

display = ttk.Frame(tela, padding=10)
display.grid()
ttk.Label(display, text='Começar o preenchimento de dados ?').grid(column=0, row=0)
ttk.Button(display, text="Sim", command=iniciar_preenchimento).grid(column=0, row=1)
ttk.Button(display, text="Cancelar", command=cancelar).grid(column=1, row=1)
tela.mainloop()