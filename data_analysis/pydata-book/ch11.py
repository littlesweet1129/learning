#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 22:51:42 2018

@author: Teresa
"""

from datetime import datetime
now = datetime.now()
now
now.year, now.month, now.day, now.hour, now.minute, now.second
delta = datetime(2011, 1, 7)-datetime(2008, 6, 24, 8, 15)
delta
delta.days
delta.seconds
from datetime import timedelta
start = datetime(2011, 1, 7)
start+timedelta(12, 2*60*60)
start-2*timedelta(12)
stamp = datetime(2011,1,3)
str(stamp)
stamp.strftime('%Y-%m-%d')
value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')
datestrs = ['7/6/2011', '8/6/2011']
[datetime.strptime(x, '%m/%d/%Y') for x in datestrs]
from dateutil.parser import parse # auto installe with pandas, pd.read_csv parse_dates=True uses parse
type(parse('2011-01-03'))
parse('Jan 31, 1997 10:45 PM')
parse('6/12/2011', dayfirst=True)
parse('6/12/2011')
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
pd.to_datetime(datestrs)
idx = pd.to_datetime(datestrs+[None])
idx[2]
pd.isnull(idx)
idx.isnull()
type(idx)
from datetime import datetime
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
dates
ts = pd.Series(np.random.randn(6), index=dates) # datetime objects have been put into DatetimeIndex
ts.index
ts+ts[::2]
ts.index.dtype
ts.index[0] 
# scalar values from a DatetimeIndex are pandas Timestamp object
# a Timestamp can be substituted anywhere you would use a datetime object
stamp = ts.index[2]
ts[stamp]
ts['1/10/2011'] # as a convenience, you can also pass a string that is interpretable as s date
ts['20110110']
longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('1/1/2000', periods=1000))
longer_ts.index
longer_ts['2001']
longer_ts['2001-05']
ts[datetime(2011, 1, 7):]
ts
ts['1/6/2011':'1/11/2011'] # you can pass a string date, datetime or timestamp
ts.truncate(after='1/9/2011')
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4),
                       index=dates,
                       columns=['Colorado', 'Texas', 'New York', 'Ohio'])
long_df.head()
long_df.loc['5-2001', 'Ohio']
long_df['Ohio']
long_df['5-2001':'6-2001']
long_df.iloc[1,1]

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000','1/2/2000', '1/3/2000'])
dates
dup_ts = pd.Series(np.arange(5), index=dates)
dup_ts
dup_ts.index.is_unique
dup_ts['1/3/2000']
dup_ts['1/2/2000']
grouped = dup_ts.groupby(level=0)
grouped.mean()
grouped.count()
ts
resampler = ts.resample('D')
resampler
index = pd.date_range('2012-04-01', '2012-06-01')
index
pd.date_range(start='2012-04-01', periods=20)
pd.date_range(end='2012-06-01', periods=20)
pd.date_range('2000-01-01', '2000-12-01', freq='BM')
pd.date_range('2012-05-02 12:56:31', periods=5) # date_range by default preserves the time
pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True) # normalized to midnight
from pandas.tseries.offsets import Hour, Minute
hour=Hour()
hour
four_hours = Hour(4)
four_hours
pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h')
# in most applications, you dont need to explicitly create one of these objects, instead
# useing a string alias like 'H' or '4H'
Hour(2)+Minute(30)
pd.date_range('2000-01-01', periods=10, freq='1h30min')
rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')
rng
ts = pd.Series(np.random.randn(4),
             index=pd.date_range('1/1/2000', periods=4, freq='M'))
ts
ts.shift(2)
ts.shift(-2)
ts.pct_change()
ts/ts.shift(1)-1
ts.shift(2, freq='M') # shift index by two periods, data stays the same
ts.shift(3, freq='D')
ts.shift(1,freq='90T') # T stands for minutes
from pandas.tseries.offsets import Day, MonthEnd
now=datetime(2011,11,17)
now+3*Day()
now+timedelta(3)
now+MonthEnd()
now+MonthEnd(2)
offset = MonthEnd()
offset.rollforward(now)
offset.rollback(now)
ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts.groupby(offset.rollforward).mean() # pass a function to groupby to groupby the value of the function return
ts.resample('M').mean()
import pytz
pytz.common_timezones[-5:]
tz = pytz.timezone('America/New_York')
tz
# pandas wraps pytz's functionality
rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
print(ts.index.tz)
# by default, time series in pandas are time zone naive
pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='UTC')
ts
ts_utc = ts.tz_localize('UTC')
ts_utc
ts_utc.index
ts.index
ts_utc.tz_convert('America/New_York')
# if DST transition in the America/New_York time zone is a concern
ts_eastern = ts.tz_localize('America/New_York')
ts_eastern.tz_convert('UTC')
ts_eastern.tz_convert('Europe/Berlin')
ts.index.tz_localize('Asia/Shanghai')
stamp = pd.Timestamp('2011-03-12 04:00')
stamp_utc=stamp.tz_localize('utc')
stamp_utc.tz
stamp_utc.tz_convert('America/New_York')
stamp_moscow = pd.Timestamp('2011-03-12 04:00', tz='Europe/Moscow')
stamp_moscow
stamp_utc.value
stamp_utc.tz_convert('America/New_York').value
# time zone aware Timestamp object internally stores a UTC timestamp value which is invariant between time zone conversions
from pandas.tseries.offsets import Hour
stamp = pd.Timestamp('2012-03-12 01:30', tz='US/Eastern')
stamp
stamp+Hour()
# 90 min before transitioning out of DST
stamp = pd.Timestamp('2012-11-04 00:30', tz='US/Eastern')
stamp
stamp+Hour(2)
rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts1 = ts[:7].tz_localize('Europe/London')
ts2 = ts1[2:].tz_convert('Europe/Moscow')
ts1
ts2
result = ts1+ts2
result.index # if two time series with different time zones are combined, the result will be UTC
p = pd.Period(2007, freq='A-DEC')
p
p+5
pd.Period('2014', freq='A-DEC') - p
rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
rng
pd.Series(np.random.randn(6), index=rng)
values = ['2001Q3', '2002Q2', '2003Q1']
index=pd.PeriodIndex(values, freq='Q-DEC')
index
p = pd.Period('2007', freq='A-DEC')
p
p.asfreq('M', how='start')
p.asfreq('M', how='end')
p = pd.Period('2007', freq='A-JUN')
p
p.asfreq('M', 'start')
p.asfreq('M', 'end')
p = pd.Period('Aug-2007', 'M')
p
p.asfreq('A-JUN')
rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts.asfreq('M', how='start')
ts.asfreq('B', how='end')
p = pd.Period('2012Q4', freq='Q-JAN')
p
p.asfreq('D', 'start')
p.asfreq('D', 'end')
p4pm = (p.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
p4pm
p4pm.to_timestamp()
rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
ts = pd.Series(np.arange(len(rng)), index=rng)
ts.index.asfreq('D', 'end')
ts
new_rng = (rng.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
ts.index = new_rng.to_timestamp()
ts
rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
ts
pts = ts.to_period()
pts
rng = pd.date_range('1/29/2000', periods=6, freq='D')
ts2 = pd.Series(np.random.randn(6), index=rng)
ts2
ts2.to_period('M')
pts = ts2.to_period()
pts.index
pts.to_timestamp(how='end').index
data = pd.read_csv('../examples/macrodata.csv')
data.head()
data.year
data.quarter
index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='Q-DEC')
index
data.index=index
data.infl
data.head()
rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts.resample('M').mean().index
ts.resample('M', kind='period').mean().index # resample is the groupby for timeseries in index
rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(12), index=rng)
ts 
ts.resample('5min', closed='right').sum()
ts.resample('5min', closed='right', label='right').sum()
ts.resample('5min', closed='right', label='right', loffset='-1s').sum()
ts.resample('5min', closed='right', label='right').sum().shift(-1, freq='s')
ts.resample('5min').ohlc() #open, high, low, close
frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2000', periods=2,freq='W-WED'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame
df_daily = frame.resample('D').asfreq()
df_daily
df_daily.ffill()
frame.resample('D').ffill()
frame.resample('D').ffill(limit=2)
frame.resample('W-THU').ffill()
frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range('1-2000', '12-2001',freq='M'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame[:5]
annual_frame = frame.resample('A-DEC').mean()
annual_frame
annual_frame.resample('Q-DEC').asfreq()
annual_frame.resample('Q-DEC').ffill()
annual_frame.resample('Q-DEC', convention='end').ffill()
annual_frame.resample('Q-JAN').ffill()

close_px_all = pd.read_csv('../examples/stock_px_2.csv', parse_dates=True, index_col=0)
close_px_all.head()
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px.index
close_px.resample('B').asfreq().index
close_px.resample('B').asfreq().ffill()
close_px.AAPL.plot()
close_px.AAPL.rolling(250).mean().plot() # 250 day rolling window, rolling behaves like groupby
app_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
app_std250.tail()
app_std250.plot()
expanding_mean = app_std250.expanding().mean()
expanding_mean.plot()
close_px.rolling(60).mean().plot(logy=True)
close_px.rolling('20D').mean()

import matplotlib.pyplot as plt
appl_px = close_px.AAPL['2006':'2007']
ma60 = appl_px.rolling(30, min_periods=20).mean()
ewma60 = appl_px.ewm(span=30).mean() # ewm exponentially weighted moving average functions like groupby, resample, rolling
ma60.plot(style='k--', label='Simple MA')
ewma60.plot(style='k-',label='EW MA')
plt.legend()

spx_px = close_px_all['SPX']
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()
returns.head()
corr = returns.AAPL.rolling(125, min_periods=100).corr(spx_rets) # rolling correlation
corr.plot()
returns.rolling(125, min_periods=100).corr(spx_rets).plot()

from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()
