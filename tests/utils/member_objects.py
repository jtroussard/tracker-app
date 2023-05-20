from datetime import datetime, date

from app import bcrypt
from app.models import Member

member_data_0 = Member(
    id=1,
    username="archersterling",
    first_name="Archer",
    middle_name="D",
    last_name="Sterling",
    date_of_birth=date(1990, 1, 1),
    location="New York",
    email="worlds-most-famous-spy@example.com",
    image_file="default.jpg",
    password=bcrypt.generate_password_hash("password123").decode("utf8"),
    joined_date=datetime.utcnow(),
    active_record=True,
    entry=[],
)
