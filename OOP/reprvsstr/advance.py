import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)


print(str(a))
print(repr(a))
