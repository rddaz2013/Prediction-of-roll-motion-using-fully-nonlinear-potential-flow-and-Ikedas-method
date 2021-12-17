import pandas as pd
import numpy as np

def load():
    
    return pd.read_csv(
        '../../data/processed/roll decay KVLCC2/model_test_parameters.csv',
        index_col=0,
    )

df_rolldecays = load()