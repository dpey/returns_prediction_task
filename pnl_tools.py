'''
Tools for PnL vizualization and statistics

'''

import matplotlib.pyplot as plt
import pandas as pd


def pnl_sharpe(df_pnl):
    '''Return annualized Sharpe ratio'''
    return df_pnl.mean() / df_pnl.std() * (252 ** 0.5)


def pnl_drawdown(df_pnl):
    '''Return absolute value of maximum drawdown'''
    drawdown = (df_pnl.cumsum() - df_pnl.cumsum().cummax()).min()
    return -drawdown


def pnl_positive_days(df_pnl):
    '''Return share of positive returns'''
    return (df_pnl > 0).sum() / len(df_pnl)


def plot_pnl(df_pnl, os_start=''):
    '''Print PnL plot'''
    if os_start:
        is_sharpe = pnl_sharpe(df_pnl[df_pnl.index < os_start])
        os_sharpe = pnl_sharpe(df_pnl[df_pnl.index >= os_start])
        _ = plt.gca()
        df_pnl[df_pnl.index].cumsum().plot(color='g')
        df_pnl[df_pnl.index < os_start].cumsum().plot(color='b')
        pd.Series().reindex_like(df_pnl).plot()
        plt.legend(['OS', 'IS'])
        plt.title(f'IS_Sharpe = {is_sharpe:3.2f}, OS_Sharpe = {os_sharpe:3.2f}')
        plt.show()
        return
    is_sharpe = pnl_sharpe(df_pnl)
    df_pnl.cumsum().plot(color='b')
    plt.title(f'Total_Sharpe = {is_sharpe:3.2f}')
    plt.show()
    return

def show_stats(df_pnl, os_start=''):
    '''Return dataframe with pnl statistics'''
    if os_start:
        is_start = df_pnl.index[0]
        os_end = df_pnl.index[-1]
        is_sharpe = pnl_sharpe(df_pnl[df_pnl.index < os_start])
        os_sharpe = pnl_sharpe(df_pnl[df_pnl.index >= os_start])
        is_drawdown = pnl_drawdown(df_pnl[df_pnl.index < os_start])
        os_drawdown = pnl_drawdown(df_pnl[df_pnl.index >= os_start])
        is_positive_days = pnl_positive_days(
            df_pnl[df_pnl.index < os_start])
        os_positive_days = pnl_positive_days(
            df_pnl[df_pnl.index >= os_start])
        stats_df = pd.DataFrame({'Period': ['IS', 'OS'],
                                 'Start': [is_start, os_start],
                                 'End': [os_start, os_end],
                                 'Sharpe': [is_sharpe, os_sharpe],
                                 'Drawdown, %': [is_drawdown*100, os_drawdown*100],
                                 'Positive days, %': [is_positive_days*100, os_positive_days*100]
                                 })
        return stats_df
    is_start = df_pnl.index[0]
    is_end = df_pnl.index[-1]
    is_sharpe = pnl_sharpe(df_pnl)
    is_drawdown = pnl_drawdown(df_pnl)
    os_drawdown = pnl_drawdown(df_pnl)
    is_positive_days = pnl_positive_days(df_pnl)
    os_positive_days = pnl_positive_days(df_pnl)
    stats_df = pd.DataFrame({'Period': ['Total'],
                             'Start': [is_start],
                             'End': [is_end],
                             'Sharpe': [is_sharpe],
                             'Drawdown, %': [is_drawdown*100],
                             'Positive days, %': [is_positive_days*100]
                             })
    return stats_df
