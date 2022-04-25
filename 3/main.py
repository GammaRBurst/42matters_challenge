# -*- coding: utf-8 -*-
"""Task 3: movies view estimation."""


__version__ = '1.0'
__author__ = 'GammaRayBurst'


import os

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def main() -> None:
    # Import file into Pandas dataframe.
    df = pd.read_csv(
        'https://raw.githubusercontent.com/WittmannF/imdb-tv-ratings/' +
        'master/top-250-movie-ratings.csv',
        index_col=0,
    )

    # Add 'Rating Count' column, filled with NaN.
    df['Rating Count'] = df['Rating Count'].map(
        lambda x: int(x.replace(',', ''))
    )
    df['Views'] = [np.NaN] * len(df)

    # Define views.
    views = {
        'Forrest Gump': 10000000,
        'The Usual Suspects': 7500000,
        'Rear Window': 6000000,
        'North by Northwest': 4000000,
        'The Secret in Their Eyes': 3000000,
        'Spotlight': 1000000,
    }
    # Insert views data where it is known.
    for title, v in views.items():
        row_id = df.query(f'Title == "{title}"').index.tolist()[0]
        df.loc[row_id, 'Views'] = v

    # Linear regression.
    # Independent variables: 'Rating Count', 'Rating', 'Year'
    # Dependent variable: 'Views'
    views_df = df.loc[df.Views.notnull()]
    X = views_df.filter(items=['Rating Count', 'Rating', 'Year']).to_numpy()
    y = views_df.Views.to_numpy()
    regr = LinearRegression()
    regr.fit(X, y)

    # Predict views for all movies.
    df['Predicted Views'] = regr.predict(
        df.filter(items=['Rating Count', 'Rating', 'Year']).to_numpy()
    )
    df['Predicted Views'] = df['Predicted Views'].map(lambda x: round(x))

    # Export result into CSV file.
    if os.path.isdir('result'):
        # Execution in Docker.  The 'result' directory can be set to export
        # the file to the host.
        df.to_csv('result/top-250-movie-ratings-prediction.csv')
    else:
        # Execution in local machine.
        df.to_csv('top-250-movie-ratings-prediction.csv')
    return None


if __name__ == '__main__':
    main()
