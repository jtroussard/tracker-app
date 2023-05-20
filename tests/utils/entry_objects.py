from datetime import datetime

from app import bcrypt
from app.models import Entry

entry_object_0 = Entry(
    id=1,
    date=datetime(2023, 5, 18, 19, 9, 45, 635888),
    time_of_day="day",
    mood="happy",
    status="normal",
    weight=250,
    measurement_waist=45,
    keto=0,
    user_id=1,
    active_record=True,
)

entry_object_1 = Entry(
    id=2,
    date=datetime(2023, 5, 18, 19, 9, 45, 635889),
    time_of_day="night",
    mood="sad",
    status="abnormal",
    weight=200,
    measurement_waist=40,
    keto=1,
    user_id=2,
    active_record=False,
)

# Duplication of entry_pbject_0
entry_object_2 = Entry(
    id=1,
    date=datetime(2023, 5, 18, 19, 9, 45, 635888),
    time_of_day="day",
    mood="happy",
    status="normal",
    weight=250,
    measurement_waist=45,
    keto=0,
    user_id=1,
    active_record=True,
)

entry_object_3 = Entry(
    id=3,
    date=datetime(2023, 5, 18, 19, 9, 45, 635900),
    time_of_day="day",
    mood="happy",
    status="normal",
    weight=250,
    measurement_waist=45,
    keto=0,
    user_id=1,
    active_record=True,
)

entry_object_4 = Entry(
    id=10,
    date=datetime(2023, 5, 16, 19, 9, 45, 635900),
    time_of_day="day",
    mood="happy",
    status="normal",
    weight=189,
    measurement_waist=36,
    keto=12,
    user_id=100,
    active_record=True,
)

no_load_entry_object_0 = Entry(
    id=5,
    date=datetime(2023, 5, 18, 19, 9, 45, 635888),
    time_of_day="day",
    mood="happy",
    status="normal",
    weight=250,
    measurement_waist=45,
    keto=0,
    user_id=1,
    active_record=True,
)

# Duplication of no_load_entry_pbject_0
no_load_entry_object_2 = Entry(
    id=5,
    date=datetime(2023, 5, 18, 19, 9, 45, 635888),
    time_of_day="day",
    mood="happy",
    status="normal",
    weight=250,
    measurement_waist=45,
    keto=0,
    user_id=1,
    active_record=True,
)

no_load_entry_object_3 = Entry(
    id=4,
    date=datetime(2023, 5, 18, 19, 9, 45, 635881),
    time_of_day="day",
    mood="happy",
    status="normal",
    weight=250,
    measurement_waist=45,
    keto=0,
    user_id=1,
    active_record=True,
)
