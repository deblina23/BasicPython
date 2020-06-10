#!/usr/bin/env python3
from datetime import datetime
from dateutil import relativedelta
d1=datetime(1985,10,23)
d2=datetime(2020,5,26)
delta=relativedelta.relativedelta(d2,d1)
print(delta.years)
print(delta.months)
15
print(delta.days)