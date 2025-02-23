import pandas as pd
import numpy as np
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

from typing import Union, List, Dict, Any, Callable, Optional

class DataVisualizer:
    def __init__(self, save_path: str) -> None:
        self.save_path: str = save_path

    def load_data(data: Union[pd.DataFrame, pd.Series]) -> pd.DataFrame:
        data = data

    def convert_series_to_df(self, data: pd.Series, columns: List[str]) -> pd.DataFrame:
        print(f'The columns list: {columns}')
        data = data.reset_index()
        
        if columns is None:
            columns = ["Index", "Value"] 
            
        data.columns = columns
        print(f'Data on convert after adding columns: {data}')
        return data

    def plot_any(
        self,
        data: Union[pd.Series, pd.DataFrame],
        plot_func: Callable[..., Any],
        x: Optional[str] = None,
        y: Optional[str] = None,
        x_label: Optional[str] = None,
        y_label: Optional[str] = None,
        title: Optional[str] = None,
        columns: Optional[list] = None,
        figure_size: Optional[list] = None,
        **kwargs
    ) -> None:
        
        if isinstance(data, pd.Series):
            data = self.convert_series_to_df(data, columns)
            print("✅ This is a Series")

        if figure_size:
            plt.figure(figsize=(figure_size[0], figure_size[1]))
        else:
            plt.figure(figsize=(10, 6))

        if x and y:
            plot_func(data=data, x=x, y=y,palette='Blues_r', **kwargs)
        elif x:
            plot_func(data=data, x=x, palette='Blues_r', **kwargs)
        elif y:
            plot_func(data=data, y=y, palette='Blues_r', **kwargs)
        else:
            plot_func(data=data, palette='Blues_r', **kwargs)

        if title:
            plt.title(title)
        if x_label:
            plt.xlabel(x_label)
        if y_label:
            plt.ylabel(y_label)

        plt.show()





        