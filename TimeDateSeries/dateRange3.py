from pandas import Series 
import pandas as pd 
import numpy as np
from datetime import datetime

dates= [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
ts= Series(np.random.randn(6), index=dates)
print(ts)

