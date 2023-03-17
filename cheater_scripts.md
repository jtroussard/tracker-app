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