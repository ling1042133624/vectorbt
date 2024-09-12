import vectorbt as vbt
# %%
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import pytz
from dateutil.parser import parse
import ipywidgets as widgets
from copy import deepcopy
from tqdm import tqdm
import imageio
from IPython import display
import plotly.graph_objects as go
import itertools
import dateparser
import gc

# %%
# Enter your parameters here
seed = 42
symbol = 'BTC-USD'
metric = 'total_return'

start_date = datetime(2018, 1, 1, tzinfo=pytz.utc)  # time period for analysis, must be timezone-aware
end_date = datetime(2020, 1, 1, tzinfo=pytz.utc)
time_buffer = timedelta(days=100)  # buffer before to pre-calculate SMA/EMA, best to set to max window
freq = '1D'

vbt.settings.portfolio['init_cash'] = 100.  # 100$
vbt.settings.portfolio['fees'] = 0.0025  # 0.25%
vbt.settings.portfolio['slippage'] = 0.0025  # 0.25%
# %%
# Download data with time buffer
cols = ['Open', 'High', 'Low', 'Close', 'Volume']
ohlcv_wbuf = vbt.YFData.download(symbol, start=start_date - time_buffer, end=end_date).get(cols)

ohlcv_wbuf = ohlcv_wbuf.astype(np.float64)

print(ohlcv_wbuf.shape)
print(ohlcv_wbuf.columns)
# %%
# Create a copy of data without time buffer
wobuf_mask = (ohlcv_wbuf.index >= start_date) & (ohlcv_wbuf.index <= end_date)  # mask without buffer

ohlcv = ohlcv_wbuf.loc[wobuf_mask, :]

print(111111111,ohlcv.shape)
# %%
# Plot the OHLC data
# ohlcv_wbuf.vbt.ohlcv.plot().show_svg()
# ohlcv_wbuf.vbt.ohlcv.plot().show_svg()
ohlcv_wbuf.vbt.ohlcv.plot().show()