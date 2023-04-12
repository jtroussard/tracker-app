# App
## Running App Local Development
```bash
python run.py
```
# Database
## Checking users live
>>> from run import app
>>> from weight_tracker.src import db
>>> from weight_tracker.src.models import User, Entry
>>> app.app_context().push()
>>> User.query.all()

## Running database from python shell
```python
from weight_tracker.src import app
from weight_tracker.src import db
from weight_tracker.src.models import User, Entry
app.app_context().push()
db.drop_all()
db.create_all()

# insert statements
db.session.add(User(id='1', username='bobby', email='c@demo.com', image_file='default.jpg', password='password', active_record=True))
db.session.add(User(id='2', username='clio', email='c1@demo.com', image_file='default.jpg', password='password', active_record=True))
db.session.add(User(id='3', username='chicken', email='c2@demo.com', image_file='default.jpg', password='password', active_record=True))
db.session.add(User(id='4', username='cat', email='cat@cat.com', image_file='default.jpg', password='$2b$12$2GC6zwJ51fUWB4KhKQ3dLOXZRdYbjttbJYG8qmjPuHblVMCoxTtGO', active_record=True))
db.session.add(User(id='5', username='clio2', email='clio@clio.com', image_file='default.jpg', password='$2b$12$LrR2SSCdAcgtQe0h6BVrC.vreC5Xs9okTS3/VAaGNS1uWmKU0gWxq', active_record=True))
db.session.add(User(id='6', username='chickenbutt', email='chick@chick.com', image_file='default.jpg', password='$2b$12$uCgW0C0XsCT2BXC5R0VYq.rbXEg2dwQWPncmTiRTiVPhb3NFW97xy', active_record=True))

# commit the changes to the database
db.session.commit()

from datetime import datetime

entry_1 = Entry(
    id=1,
    date=datetime.now(),
    time_of_day='Morning',
    mood='good',
    status='normal',
    weight=270.0,
    measurement_waist=46.0,
    keto=1,
    user_id=1,
    active_record=1
)

# Entry 2
entry_2 = Entry(
    id=2,
    date=datetime.now(),
    time_of_day='Morning',
    mood='good',
    status='normal',
    weight=170.0,
    measurement_waist=46.0,
    keto=1,
    user_id=2,
    active_record=1
)

# Entry 3
entry_3 = Entry(
    id=3,
    date=datetime.now(),
    time_of_day='Morning',
    mood='good',
    status='normal',
    weight=271.0,
    measurement_waist=46.0,
    keto=1,
    user_id=1,
    active_record=1
)

# Entry 4
entry_4 = Entry(
    id=4,
    date=datetime.now(),
    time_of_day='Morning',
    mood='good',
    status='normal',
    weight=269.0,
    measurement_waist=46.0,
    keto=1,
    user_id=1,
    active_record=1
)

# Entry 5
entry_5 = Entry(
    id=5,
    date=datetime(2023, 3, 18),
    time_of_day='night',
    mood='good',
    status='normal',
    weight=10.0,
    measurement_waist=1.0,
    keto=1,
    user_id=3,
    active_record=1
)

# Entry 6
entry_6 = Entry(
    id=6,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=312.9,
    measurement_waist=10.0,
    keto=10,
    user_id=4,
    active_record=0
)

# Entry 7
entry_7 = Entry(
    id=7,
    date=datetime(2023, 3, 18),
    time_of_day='night',
    mood='average',
    status='sick',
    weight=11.0,
    measurement_waist=11.0,
    keto=11,
    user_id=4,
    active_record=0
)

# Entry 8
entry_8 = Entry(
    id=8,
    date=datetime(2023, 3, 15),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=30.0,
    measurement_waist=4.0,
    keto=4,
    user_id=4,
    active_record=0
)

entry_9 = Entry(
    id=9,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=23.0,
    measurement_waist=232.0,
    keto=3,
    user_id=4,
    active_record=0
)

entry_10 = Entry(
    id=10,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='average',
    status='injured',
    weight=222.0,
    measurement_waist=2.0,
    keto=2,
    user_id=4,
    active_record=1
)

entry_11 = Entry(
    id=11,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=999.0,
    measurement_waist=999.0,
    keto=999,
    user_id=4,
    active_record=0
)

entry_12 = Entry(
    id=12,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=1.0,
    measurement_waist=1.0,
    keto=1,
    user_id=5,
    active_record=1
)

entry_13 = Entry(
    id=13,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=2.0,
    measurement_waist=2.0,
    keto=2,
    user_id=5,
    active_record=1
)

entry_14 = Entry(
    id=14,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=3.0,
    measurement_waist=3.0,
    keto=3,
    user_id=5,
    active_record=1
)

entry_15 = Entry(
    id=15,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=4.0,
    measurement_waist=4.0,
    keto=4,
    user_id=5,
    active_record=1
)

entry_16 = Entry(
    id=16,
    date=datetime(2023, 3, 18),
    time_of_day='day',
    mood='good',
    status='normal',
    weight=5.0,
    measurement_waist=5.0,
    keto=5,
    user_id=5,
    active_record=1
)

some_entries = [
entry_1,
entry_2,
entry_3,
entry_4,
entry_5,
entry_6,
entry_7,
entry_8,
entry_9,
entry_10,
entry_11,
entry_12,
entry_13,
entry_14,
entry_15,
entry_16
]

for e in some_entries:
    db.session.add(e)
db.session.commit()
User.query.all()
Entry.query.all()
```

# Linter
## Running linter manually from command line
Get into project root and run
*For full project*
```bash
pylint weight_tracker
```
*For individual files*
```bash
pylint weight_tracker/models.py
```