#projeto final 

# imports
from msilib.schema import Class
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.datasets import load_files


def carregando_arquivos():
    load_file = "dados_compras.json"
    purchase = pd.read_json(load_file, orient = "records" )
    purchase.head()

def verifica_exclusivos():
    tot0 =  lambda purchase_file: purchase_file['Login'].drop_duplicates()
    tot1 =  lambda purchase_file: purchase_file['Idade'].drop_duplicates()
    tot2 =  lambda purchase_file: purchase_file['Sexo'].drop_duplicates()
    tot3 =  lambda purchase_file: purchase_file['Item ID'].drop_duplicates()
    tot4 =  lambda purchase_file: purchase_file['Nome do Item'].drop_duplicates()
    return [tot0, tot1, tot2, tot3, tot4]

def consumidores():
    total_vendas = purchase['Login'].count()
    total_consumidores = purchase['Login'].drop_duplicates()
    return [total_vendas,total_consumidores]

#criar um main com o passo a passo da solução

