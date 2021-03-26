tm = '2020-11-13T01:39:13.607'

from datetime import datetime
import arrow
# Getting the current date
# and time
now = datetime.utcnow()
print(arrow.get(tm).to('local').format())