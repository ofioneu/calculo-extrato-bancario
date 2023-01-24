import pandas as pd

def calcular():
    df= pd.read_csv('extrato.csv', encoding='latin-1', index_col=False)

    c = 0
    d =0

    for i in df['Valor']:
        if i > 0:
            c+=i
        
        else:
            d+=i
            
    print('Entradas: ', c)
    print('Saidas: ', d)
