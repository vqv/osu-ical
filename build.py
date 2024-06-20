# %%
from datetime import datetime

import requests
from ics import Calendar, Event
from pytz import timezone

CALENDAR_URL = "https://registrar.osu.edu/umbraco/api/calendar/getentries"


def get_calendar(years_past=5, years_future=5, filters=None):
    today = datetime.today()
    start = datetime(today.year - years_past, 1, 1)
    end = datetime(today.year + years_future, 12, 31)

    payload = {
        "start": start,
        "end": end,
        "selected": None,
        "filters": filters,
    }
    r = requests.get(CALENDAR_URL, params=payload)
    return r.json()


def make_calendar(entries):
    cal = Calendar()

    for e in entries:
        date = datetime.fromisoformat(e["DateTime"])
        x = e["Title"].split(" - ")
        event = Event(
            name=x[0].title(),
            begin=date.astimezone(timezone("US/Eastern")),
            description=x[1].capitalize() if len(x) > 1 else None,
        )
        event.make_all_day()
        cal.events.add(event)

    return cal


if __name__ == "__main__":
    data = get_calendar(filters="Academic Calendar")
    entries = [x for x in data["Entries"] if x["Type"] == ["Academic Calendar"]]
    entries.sort(key=lambda x: x["DateTime"])
    cal = make_calendar(entries)

    with open("build/academic.ics", "w") as f:
        f.write(cal.serialize())
