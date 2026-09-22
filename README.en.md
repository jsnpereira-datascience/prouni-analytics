[![pt-BR](https://img.shields.io/badge/lang-pt--BR-green?style=for-the-badge)](README.md) [![en](https://img.shields.io/badge/lang-en-blue?style=for-the-badge)](README.en.md)

# Prouni Analysis

I decided to create this repository to grow my data science studies. I'm documenting this project as a data science exercise (beginner level) to investigate the Prouni tables, clean the data, create charts for analysis, and write down the interpretations.

## Files

The CSV files are in the `data/raw` directory. There are 5 files, as follows:

File                   |  Description
-----------------------|------------------------
dados_brasil_uf.csv    | Data with states, state codes (UF), and regions
dados_ies.csv          | Data with information about the institutions
dados_municipio.csv    | Data with information about the municipalities
dados_prouni.csv       | Data with information about Prouni scholarship recipients
prouni_dicionario.csv  | Data with columns, keys, and values

## Data Cleaning

Prouni data table (dados_prouni.csv):

<ul>
  <li>column: id_municipio
    <ul>
      <li>Empty field</li>
       <ul>
            <li>Add the id of the capital's municipality, based on the sigla_uf (state) column</li>
      </ul>
    </ul>
  </li>
  <li>Columns: sexo, raca_cor, beneficiario_deficiente, turno_curso, tipo_bolsa, modalidade_ensino
    <ul>
      <li>Set up the key numbers in the column, which will be replaced with the values from the prouni_dicionario table</li>
    </ul>
  </li>
  <li>Columns: campus, nome_municipio_ies
   <ul>
      <li>Remove these columns</li>
      <li>They will be merged into the dados_ies.csv table, which already has both columns</li>
    </ul>
  </li>
  <li>column: id_ies
   <ul>
      <li>Will be merged into the dados_ies.csv table</li>
    </ul>
  </li>

  <li>column: id_municipio
   <ul>
      <li>Will be merged into the dados_municipio.csv table</li>
    </ul>
  </li>

</ul>

The data used was downloaded from the following database website:
Source: https://basedosdados.org/dataset/d2200639-0843-4960-99a2-f844df1fa3d1?table=6463b26b-a8dd-4fb5-895c-117f38dd566b
