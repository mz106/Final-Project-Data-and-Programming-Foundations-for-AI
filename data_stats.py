import pandas as pd
import numpy as np

from scipy.stats import pearsonr, chi2_contingency
from typing import Union, List, Dict, Any, Callable, Optional

class DataStats:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def run_chi2_contingency(self, data):
        chi2_stat, p_value, dof, expected = chi2_contingency(data)

        stats = {
            'chi2_stat': chi2_stat,
            'p_value': p_value,
            'dof': dof,
            'expected': expected
        }

        return stats
    