import os

import datetime
from datetime import datetime

filename = 'data/day03_messages.log'

with open(filename,) as fh:
    for line in fh:
        if 'initiated' in line:
            # print(datetime)
            print(datetime.strptime(line, "INFO %Y-%m-%d %H:%M:%S"))
        else:
            continue
