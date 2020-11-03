import os
import re

import datetime
from datetime import datetime, timedelta
import dateutil.parser as dparser


filename = 'data/day03_messages.log'

with open(filename,) as fh:
    for line in fh:
        if 'initiated' in line:
            #dparser.parse(line)
            match = re.search(r'\d{4}-\d{2}-\d{2}\sT\d{2}:\d{2}:\d{2}', line)
            date = datetime.strptime(match.group(), '%Y-%m-%d %H:%M:%S').date()
        else:
            continue
