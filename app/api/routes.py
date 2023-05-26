from flask import jsonify, Blueprint
from flask_login import current_user

from app import limiter
from app.models import Entry
from app.decorators import restrict_access

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/entries", methods=["GET"])
@limiter.limit("100/day", override_defaults=True)
def get_entries():
    # Get the user's entries and sort them by date
    entries = (
        Entry.query.filter_by(user_id=current_user.id, active_record=True)
        .order_by(Entry.date)
        .all()
    )

    # Convert entries to a list of dictionaries
    entries_data = []
    for entry in entries:
        entry_data = {
            "id": entry.id,
            "date": entry.date.isoformat(),
            "time_of_day": entry.time_of_day,
            "mood": entry.mood,
            "status": entry.status,
            "weight": entry.weight,
            "measurement_waist": entry.measurement_waist,
            "keto": entry.keto,
        }
        entries_data.append(entry_data)

    return jsonify(entries_data)