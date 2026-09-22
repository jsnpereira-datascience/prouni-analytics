import pandas as pd

def load(file_path, sep=";", encoding="utf-8"):
    df = pd.read_csv(file_path, sep=sep, encoding=encoding)
    return df