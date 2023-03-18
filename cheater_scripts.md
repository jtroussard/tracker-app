# App
## Running App Local Development
```bash
python run.py
```
# Database
## Running database from python shell
```python
from weight_tracker import app
from weight_tracker import db
from weight_tracker.models import User, TrackerEntry
app.app_context().push()
db.create_all()
user_1 = User(username='bobby', email='c@demo.com', password='password')
user_2 = User(username='clio', email='c1@demo.com', password='password')
user_3 = User(username='chicken', email='c2@demo.com', password='password')
db.session.add(user_1)
db.session.add(user_2)
db.session.add(user_3)
db.session.commit()
from datetime import datetime, timedelta
now = datetime.now()
later_1 = now + timedelta(hours=1, minutes=30)
later_2 = now + timedelta(hours=2, minutes=30)
later_3 = now + timedelta(hours=3, minutes=30)
entry_1 = TrackerEntry(date=now, time_of_day="Morning", mood="good", status="normal", weight=270.0, measurement_waist=46, keto=1, user_id=user_1.id)
entry_2 = TrackerEntry(date=later_1, time_of_day="Morning", mood="good", status="normal", weight=170.0, measurement_waist=46, keto=1, user_id=user_2.id)
entry_3 = TrackerEntry(date=later_2, time_of_day="Morning", mood="good", status="normal", weight=271.0, measurement_waist=46, keto=1, user_id=user_1.id)
entry_4 = TrackerEntry(date=later_3, time_of_day="Morning", mood="good", status="normal", weight=269.0, measurement_waist=46, keto=1, user_id=user_1.id)
db.session.add(entry_1)
db.session.add(entry_2)
db.session.add(entry_3)
db.session.add(entry_4)
db.session.commit()
User.query.all()
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