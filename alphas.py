'''
This file collection of alphas.

'''


def alpha_1(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_zscore(ts_ffill(data), N), vm)))


def alpha_2(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_delta(ts_ffill(data), N), vm)))


def alpha_3(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_avdiff(ts_ffill(data), N), vm)))


def alpha_4(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_scale(ts_ffill(data), N), vm)))


def alpha_5(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_zscore(ts_ffill(data), N), vm)))


def alpha_6(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_delta(ts_ffill(market_rank(data)), N), vm)))


def alpha_7(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_avdiff(ts_ffill(market_rank(data)), N), vm)))


def alpha_8(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_scale(ts_ffill(market_rank(data)), N), vm)))


def alpha_9(data, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_zscore(ts_ffill(data), N), vm)))


def alpha_10(data, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_delta(ts_ffill(data), N), vm)))


def alpha_11(data, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_avdiff(ts_ffill(data), N), vm)))


def alpha_12(data, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_scale(ts_ffill(data), N), vm)))


def alpha_13(data, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_zscore(ts_ffill(data), N), vm)))


def alpha_14(data, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_delta(ts_ffill(market_rank(data)), N), vm)))


def alpha_15(data, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_avdiff(ts_ffill(market_rank(data)), N), vm)))


def alpha_16(data, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_scale(ts_ffill(market_rank(data)), N), vm)))


def alpha_17(data):
    '''Alpha'''
    return market_normalize(market_zscore(validate(data, vm)))


def alpha_18(data):
    '''Alpha'''
    return market_normalize(market_rank(validate(data, vm))-0.5)


def alpha_19(data1, data2):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_ffill(market_rank(data1) - market_rank(data2)), vm)))


def alpha_20(data1, data2):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_ffill(market_zscore(data1) - market_zscore(data2)), vm)))


def alpha_21(data1, data2, N=65):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_zscore(ts_ffill(data1), N) - ts_zscore(ts_ffill(data2), N), vm)))


def alpha_22(data1, data2, N=252):
    '''Alpha'''
    return market_normalize(market_neutralize(validate(ts_zscore(ts_ffill(data1), N) - ts_zscore(ts_ffill(data2), N), vm)))
