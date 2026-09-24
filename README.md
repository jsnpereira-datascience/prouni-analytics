[![pt-BR](https://img.shields.io/badge/lang-pt--BR-green?style=for-the-badge)](README.md) [![en](https://img.shields.io/badge/lang-en-blue?style=for-the-badge)](README.en.md)

# Análise do Prouni

Decidi criar este repositório para evoluir meus estudos em ciência de dados. Documento este projeto como um trabalho de ciência de dados (nível iniciante), com o objetivo de investigar as tabelas do Prouni, tratar os dados, criar gráficos para análise e escrever as interpretações.

## Arquivos

Os arquivos CSV estão no diretório `data/raw`. Temos 5 arquivos, conforme a seguir:

Arquivo               |  Descrição
-----------------------|------------------------
dados_brasil_uf.csv    | Dados que fornecem estados, siglas e regiões
dados_ies.csv          | Dados que fornecem informações das instituições
dados_municipio.csv    | Dados que fornecem informações dos municípios
dados_prouni.csv       | Dados que fornecem informações dos bolsistas do Prouni
prouni_dicionario.csv  | Dados que fornecem colunas, chaves e valores

## Tratamentos

Tabela de dados do Prouni (dados_prouni.csv):

<ul>
  <li>coluna: id_municipio
    <ul>
      <li>Campo vazio</li>
       <ul>
            <li>Adicionar o id do município da capital, relacionado à coluna sigla_uf (estado)</li>
      </ul>
    </ul>
  </li>
  <li>Colunas: sexo, raca_cor, beneficiario_deficiente, turno_curso, tipo_bolsa, modalidade_ensino
    <ul>
      <li>Configurar os números das chaves da coluna, que serão substituídos pelos valores da tabela do arquivo prouni_dicionario</li>
    </ul>
  </li>
  <li>Colunas: campus, nome_municipio_ies
   <ul>
      <li>Remover as colunas</li>
      <li>Serão integradas à tabela do arquivo dados_ies.csv, que possui as duas colunas</li>
    </ul>
  </li>
  <li>coluna: id_ies
   <ul>
      <li>Será integrada à tabela do arquivo dados_ies.csv</li>
    </ul>
  </li>

  <li>coluna: id_municipio
   <ul>
      <li>Será integrada à tabela do arquivo dados_municipio.csv</li>
    </ul>
  </li>

  <li>coluna: data_nascimento
   <ul>
      <li>converter o tipo do campo deve ser date</li>
    </ul>
  </li>

</ul>

Foram utilizados os dados baixados da base de dados no site a seguir:
Fonte: https://basedosdados.org/dataset/d2200639-0843-4960-99a2-f844df1fa3d1?table=6463b26b-a8dd-4fb5-895c-117f38dd566b
