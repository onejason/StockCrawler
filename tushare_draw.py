import matplotlib.pyplot as plt
import tushare as ts
import pandas as pd

fig = plt.gcf()
df=ts.get_hist_data('600415',start='2015-04-01',end='2015-06-18')
with pd.plot_params.use('x_compat', True):
    df.high.plot(color='r',figsize=(10,4),grid='on')
    df.low.plot(color='b',figsize=(10,4),grid='on')
    fig.savefig('/Users/Jason/graph.png')