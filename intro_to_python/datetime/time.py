from datetime import datetime, timedelta, timezone
import pytz
from calendar import calendar


today = datetime.now()
print(f"today is {today}")

two_years_from_today = today + timedelta(days=760)
print(f" in two years it will be {two_years_from_today}")

# display calendar
year=2023
# print(calendar(year))

# Timezone
# imprime la date dans un fuseau horaire prédefini

utc_dt = datetime.now(timezone.utc)
paris = pytz.timezone("Europe/Paris")
london = pytz.timezone("Europe/London")

print(f"Paris time: {utc_dt.astimezone(paris).isoformat()}")
print(f"London time: {utc_dt.astimezone(london).isoformat()}")