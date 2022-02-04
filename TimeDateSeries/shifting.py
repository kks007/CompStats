import numpy as np 
import pandas as pd 
from pandas import Series 
from datetime import datetime
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)

offset = MonthEnd()

ts = Series(np.random.randn(20),index=pd.date_range('1/15/2000', periods=20, freq='4d'))
print(ts)
print(ts.groupby(offset.rollforward).mean())
