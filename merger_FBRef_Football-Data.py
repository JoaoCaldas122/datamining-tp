import pandas as pd

anos = ['201819','201920','202021','202122','202223']

conversao = {'Benfica': 'Benfica',
     'Vitória Setúbal': 'Setubal',
     'Tondela': 'Tondela',
     'Porto': 'Porto',
     'Marítimo': 'Maritimo',
     'Feirense': 'Feirense',
     'Moreirense': 'Moreirense',
     'Braga': 'Sp Braga',
     'Portimonense': 'Portimonense',
     'Aves': 'Aves',
     'Chaves': 'Chaves',
     'Boavista': 'Boavista',
     'Sporting CP': 'Sp Lisbon',
     'Rio Ave': 'Rio Ave',
     'Nacional': 'Nacional',
     'B-SAD': 'Belenenses',
     'Santa Clara': 'Santa Clara',
     'Gil Vicente FC': 'Gil Vicente',
     'Famalicão': 'Famalicao',
     'Paços': 'Pacos Ferreira',
     'Vitória': 'Guimaraes',
     'Farense': 'Farense',
     'Arouca': 'Arouca',
     'Vizela': 'Vizela',
     'Estoril': 'Estoril',
     'Casa Pia': 'Casa Pia'
     }

for ano in anos:

    df = pd.read_csv(f'fbref/dataset_{ano}.csv')
    fd = pd.read_csv(f'football-data/{ano}.csv')

    df['home'] = df['home'].replace(conversao)
    df['away'] = df['away'].replace(conversao)
     
    fd = fd[['HomeTeam','AwayTeam','HS','AS','HST','AST','B365H','B365D','B365A','HTHG','HTAG']]
    
    new_df = pd.merge(df, fd,  how='left', left_on=['home','away'], right_on = ['HomeTeam','AwayTeam'])
    new_df.drop(['HomeTeam', 'AwayTeam'], inplace=True, axis=1)
    
    new_df.to_csv(f'merged/merged_{ano}.csv',index=False)
    
df1 = pd.read_csv('merged/merged_201819.csv')
df2 = pd.read_csv('merged/merged_201920.csv')
df3 = pd.read_csv('merged/merged_202021.csv')
df4 = pd.read_csv('merged/merged_202122.csv')
df5 = pd.read_csv('merged/merged_202223.csv')

df1['season'] = 2019
df2['season'] = 2020
df3['season'] = 2021
df4['season'] = 2022
df5['season'] = 2023

df6 = pd.concat([df1,df2,df3,df4,df5])

df6.to_csv('merged_treinofinaltudo.csv', index=False)
    
'''
##### Descobrir as diferenças nos nomes das equipas entre ambos os datasets

a = [x for x in list(dict(zip(df['home'],fd['HomeTeam'])).keys()) if x not in list(conversao.keys())]
print(a)
'''
