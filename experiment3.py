import datetime
import pytz

Time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
Time=Time.strftime('%h/%d/%Y  %H:%M')


print()