import pandas as pd
import numpy as np
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

from typing import Union, List, Dict, Any, Callable, Optional

class DataProcessor:
    def __init__(self, file_path: str, cache_file: str = 'cache.pkl') -> None:
        self.file_path: str = file_path
        self.df: Optional[pd.DataFrame] = None
        self.cache_file: str = cache_file
        self.cache_map: Dict[str, Any] = self._load_cache()
        
    def _load_cache(self) -> Dict[str, Any]:
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'rb') as file:
                try:
                    return pickle.load(f)
                except Exception:
                    print('Error loading cache file: resetting cache')
                    return {}
        return {}

    def _save_cache(self) -> None:
        with open(self.cache_file, 'wb') as file:
            pickle.dump(self.cache_map, file)

    def load_data(self) -> None:
        if 'data' in self.cache_map:
            self.df = self.cache_map['data']
            print('Data loaded from cahce')
        else:
            try:
                self.df = pd.read_csv('dataset_converted.csv')
                self.cache_map['data'] = self.df
                self._save_cache()
                print('Data loaded and stored in cahce')
            except Exception as ex:
                print(f'Error loading data: {ex}')

    def get_head(self, n: int = 5) -> Optional[pd.DataFrame]:
        if self.df is None:
            print('Data not loaded. Please load the dataset first')
            return None

        cache_key = f'head_{n}'

        if cache_key in self.cache_map:
            print(f'Cached data for df.head({n}) loaded from cache')
            return self.cache_map[cache_key]

        head_df = self.df.head(n)
        self.cache_map[cache_key] = head_df
        self._save_cache()

        print(f'Computed df.head({n}) and cached')
        return head_df