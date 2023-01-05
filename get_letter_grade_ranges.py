#!/usr/bin/env python

"""Get interval ranges for letter grades.

Returns a dataframe with ranges for each letter grade. Takes as input
the highest grade percentage in the class and creates four equal sized
intervals (ABCD) between this value and one half its value.
"""

import pandas as pd
import numpy as np

def get_grade_ranges(max_grade: float) -> pd.DataFrame:
    """Return a Dataframe with ranges for letter grades."""
    df = pd.DataFrame({}, index=list("ABCD"))
    ranges = np.linspace(max_grade, max_grade / 2, 5)
    df['upper'] = ranges[:-1]
    df['lower'] = ranges[1:]
    df['splits'] = [
        np.linspace(df.upper[i], df.lower[i], 4).round(2) 
        for i in df.index
    ]
    return df

if __name__ == "__main__":
    print(get_grade_ranges(0.9895))
