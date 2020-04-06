'''
This file contains collection of matrix operators.
Each operator is a function that gets one or two dataframes with data,
transforms it and returns new dataframe.

Dataframes with data should have following structure:
    columns - Ticker ids,
    rows - Dates, first row - earliest date
Values in dataframe could be float, int, bool; np.nan is also allowed.

There  are three groups of operators: Cross-sectional, Time-series and Others.
Cross-sectional operators for each date transform row using only data from
current row.
Time-series operators applied some rolling window function. Order of dates
in dataframe must be ascending to avoid forward looking bias.
Others operators change each cell in dataframe independently.

'''
import numpy as np
import pandas as pd

# CROSS SECTIONAL OPERATORS


def market_rank(input_df):
    '''Return dataframe cross-sectionally (by rows) ranked from 0.0 to 1.0'''
    ranked_ = input_df.rank(ascending=True, axis=1) - 1
    return ranked_.divide(ranked_.max(axis=1), axis=0)


def market_neutralize(input_df):
    '''Return cross-sectional neutral (by rows) dataframe'''
    return input_df.sub(input_df.mean(axis=1, skipna=True), axis=0)


def market_zscore(input_df):
    '''Return cross-sectional (by rows) z-score of dataframe'''
    mean_ = input_df.mean(axis=1, skipna=True)
    std_ = input_df.std(axis=1, skipna=True)
    return input_df.sub(mean_, axis=0).div(std_, axis=0)


def market_normalize(input_df):
    '''Return dataframe such as sum of absolute values of rows equal 1'''
    return input_df.divide(input_df.abs().sum(axis=1), axis=0)


# TIME SERIES OPERATORS


def ts_ffill(input_df):
    '''Return forward-filled dataframe'''
    return input_df.fillna(method='ffill')


def ts_delta(input_df, window=252):
    '''Return time-series (by columns) delta of datarame'''
    return input_df.sub(input_df.shift(window))


def ts_zscore(input_df, window=252):
    '''Return time-series (by columns) z-score of datarame'''
    mean_ = input_df.rolling(window=window, min_periods=4).mean()
    std_ = input_df.rolling(window=window, min_periods=4).std()
    zscore_ = input_df.sub(mean_).divide(std_)
    return zscore_.replace([np.inf, -np.inf], np.nan)


def ts_avdiff(input_df, window=252):
    '''Return dataframe minus time-series (by columns) mean of datarame'''
    mean_ = input_df.rolling(window=window, min_periods=4).mean()
    return input_df.sub(mean_)


def ts_max(input_df, window=252):
    '''Return time-series (by columns) max of datarame'''
    return input_df.rolling(window=window, min_periods=1).max()


def ts_min(input_df, window=252):
    '''Return time-series (by columns) min of datarame'''
    return input_df.rolling(window=window, min_periods=1).min()


def ts_mean(input_df, window=252):
    '''Return time-series (by columns) mean of datarame'''
    return input_df.rolling(window=window, min_periods=1).mean()


def ts_scale(input_df, window=252):
    '''Return time-series (by columns) scaled from 0.0 to 1.0 datarame'''
    max_ = ts_max(input_df, window)
    min_ = ts_min(input_df, window)
    return input_df.sub(min_).div(max_.sub(min_))


def ts_std(input_df, window=252):
    '''Return time-series (by columns) standart deviation of datarame'''
    return input_df.rolling(window=window, min_periods=1).std()


def ts_rank(input_df, window=252):
    '''Return time-series (by columns) rank of datarame'''
    def col_rank(col_x):
        '''Return ranked pd.series'''
        x_rank = pd.Series(col_x).rank(ascending=True) - 1
        return x_rank.iloc[-1] / x_rank.max()

    __ = input_df.rolling(window=window, min_periods=1, axis=0).apply(col_rank)
    return __


# OTHERS


def signed_power(input_df, power=2):
    '''Return powered dataframe with respect to sign'''
    return np.sign(input_df) * abs(input_df).pow(power)


def validate(input_df, valid_matrix):
    '''Replace infs, NaNs to zeros, then multily to valid matrix'''
    __ = input_df.replace([np.inf, -np.inf, np.nan, None], 0)
    return __.mul(valid_matrix)
