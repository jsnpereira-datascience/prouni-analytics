
def tratar_dicionario_colunas(data,dicionario):
    for coluna, dados in dicionario.groupby('nome_coluna'):
        de_para = dict(zip(dados["chave"], dados["valor"]))
        data[coluna] = data[coluna].astype("int64").map(de_para)
    return data;