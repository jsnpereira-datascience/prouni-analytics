from sklearn.impute import KNNImputer
import pandas as pd

def clean_empty_data(data):
    if data.isna().any(axis=1).sum() > 0:
          data = data.dropna()
    return data

def check_data_duplicated(data):
      return data[data.duplicated(keep=False)].sort_values(by=list(data.columns))

def remove_data_duplicated(data):
      if data.duplicated().sum() > 0:
        data = data.drop_duplicates()
      return data

def join_data(data_left, data_right, columns_join,columns_drop=[], join_type = 'left'):
      left, right = next(iter(columns_join.items()))
      data_joined = data_left.merge(data_right,left_on=left, right_on=right, how=join_type)
      count = len(columns_drop)
      if count > 0:
            data_joined = data_joined.drop(columns=columns_drop)
      return data_joined

def media_by_group(data, groupby,media, filtro= None):
      base = data if filtro is None else data[filtro]
      return base.groupby(groupby)[media].mean().reset_index()

def sum_by_group(data, groupby,media, filtro= None):
      base = data if filtro is None else data[filtro]
      return base.groupby(groupby)[media].sum().reset_index()

def correct_data_imputer(data,columns,neighbors=2):
     imputer = KNNImputer(n_neighbors=neighbors)
     data_fix = pd.DataFrame(
            imputer.fit_transform(data[columns]),
            columns=columns, 
            index= data.index)
     data[columns] = data_fix
     return data