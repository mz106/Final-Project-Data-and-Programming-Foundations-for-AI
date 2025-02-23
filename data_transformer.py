import pandas as pd
import numpy as np

from typing import Union, List, Dict, Any, Callable, Optional

class DataTransformer:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def print_df(self):
        print('prind_df in DataTransformer')
        print(self.data_processor.df.head())

    def make_df_copy(self) -> pd.DataFrame:
        df = self.data_processor.df
        
        if df is None:
            print('No data loaded - please load a dataset')
            return None

        df_copy = df.copy(deep=True)
        print('Copy of dataset successfully created')
        return df_copy
        
    def standardize_text(self, df: pd.DataFrame, column_name: str) -> pd.DataFrame:
        if df is None:
            print('No data loaded - please load a dataset')
            return None

        df[column_name] = df[column_name].str.lower().str.replace(r"[^a-zA-Z0-9,\s]", "", regex=True)
        return df

    def fill_missing_values(self, df: pd.DataFrame, column_name: str, data_value: str) -> pd.DataFrame:
        if df is None:
            print('No data loaded - please load a dataset')
            return None

        df[column_name] = df[column_name].fillna(data_value)
        return df

    def split_str(self, df:pd.DataFrame, column_name: str) -> pd.DataFrame:
        if df is None:
            print('No data loaded - please load a dataset')
            return None

        column_name_list = column_name + '_list'
        print("\n🔹 Before Splitting:", df[column_name].head())  # Print before
        df[column_name_list] = df[column_name].str.split(',').apply(lambda x: [i.strip().title() for i in x])
        print("\n✅ After Splitting:", df[column_name_list].head())  # Print after
        return df
    
    def make_group(self, df: pd.DataFrame, column_name: str, secondary_column: str = None) -> pd.Series:
        if df is None:
            print('No data loaded - please load a dataset')
            return None

        if secondary_column:
            cache_key = f"group_{column_name}_{secondary_column}"
        else:
            cache_key = f"group_{column_name}"

        if cache_key in self.data_processor.cache_map:
            print(f"✅ Returning cached grouped data for column '{column_name}'")
            return self.data_processor.cache_map[cache_key]

        df_exploded = df.explode(column_name)

        if secondary_column:
            grouped = df_exploded.groupby([column_name, secondary_column]).size().unstack(fill_value=0)
        else:
            grouped = df_exploded.groupby(column_name).size().sort_values(ascending=False)
        
        self.data_processor.cache_map[cache_key] = grouped
        self.data_processor._save_cache()

        print(f"✅ Computed and cached grouped data for column '{column_name}'")

        return grouped

        
        