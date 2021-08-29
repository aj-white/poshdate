from datetime import datetime
from datetime import date
from typing import Union


def from_datetime(date_obj: Union[datetime, date]) -> str:
    date_ = int(date_obj.strftime("%d"))
    
    check_date = date_ if (date_ < 20) else (date_ % 10)
    if check_date == 1:
        suffix = "st"
    elif check_date == 2:
        suffix = "nd"
    elif check_date == 3:
        suffix = "rd"
    else:
        suffix = "th"
    
    return f"{date_}{suffix} {date_obj:%B %Y}"