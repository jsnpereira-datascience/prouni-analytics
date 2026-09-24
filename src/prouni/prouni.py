
def process_column_dictionary(data,dicionario):
    for coluna, dados in dicionario.groupby('nome_coluna'):
        de_para = dict(zip(dados["chave"], dados["valor"]))
        data[coluna] = data[coluna].astype("int64").map(de_para)
    return data;

def get_state_capital(data):
    return data[ data['capital_uf'] == 1 ]

def process_city_missing(data, city_states):
    missing = data[data['id_municipio'].isna()]

    missing['id_municipio'] = missing['sigla_uf'].map(
        city_states.set_index('sigla_uf')['id_municipio']
    )

    data.loc[missing.index, 'id_municipio'] = missing['id_municipio']

    return data

