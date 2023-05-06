"""
This is a Flask blueprint module that contains routes related to entries
functionality.

Routes:
/get_entry: Renders single entry page. Has edit and delete buttons.
/update_entry: Renders update single entry page.
/delete_entry: Deletes single entry by way of soft deletion.
/entry_index: Renders all user entries and add entry form.
"""
from flask import render_template, redirect, url_for, flash, abort, request, Blueprint
from flask_login import login_required, current_user
from app.src import db
from app.src.entries.forms import EntryForm
from app.src.models import Entry

entries = Blueprint("entries", __name__)


@entries.route("/entry/<int:entry_id>", methods=["GET"])
@login_required
def get_entry(entry_id):
    """Renders single entry page."""
    entry = Entry.query.filter_by(id=entry_id, active_record=True).first_or_404()
    if entry.author != current_user:
        abort(403)
    return render_template("entry.html", entry=entry)


@entries.route("/entry/<int:entry_id>/update", methods=["GET", "PUT", "POST"])
@login_required
def update_entry(entry_id):
    """Updates an entry. Redirects to single entry page."""
    entry = Entry.query.filter_by(id=entry_id, active_record=True).first_or_404()
    if entry.author != current_user:
        abort(403)
    form = EntryForm(obj=entry)
    print(f"request method is {request.method} entry {entry} form {form}")
    if request.method == "POST":
        print("log this: Request method is POST")
        if form.validate_on_submit():
            print("log this: Form validated successfully")
            form.populate_obj(entry)
            db.session.commit()
            flash("Your entry has been updated!", "success")
            return redirect(url_for("entries.entry_index"))
        # else:
        #     print("Form did not validate")
        #     print(f"{form.errors}")
    return render_template("entry_edit.html", form=form, entry=entry)


@entries.route("/entry/<int:entry_id>", methods=["POST"])
@login_required
def delete_entry(entry_id):
    """Deletes an entry from the database by way of soft deletion. Sets
    active record flag to False.
    """
    entry = Entry.query.filter_by(id=entry_id, active_record=True).first_or_404()
    if entry.author != current_user:
        abort(403)
    else:
        entry.active_record = False
        db.session.commit()
        flash("Your entry has been deleted!", "success")
    return redirect(url_for("entries.entry_index"))


@entries.route("/entry_index", methods=["GET", "POST"])
@login_required
def entry_index():
    """
    The function get_entry() is called when the user visits the /entry route.
    :return: The entry page is being returned.
    """
    if current_user.is_authenticated:
        user_entries = Entry.query.filter_by(
            user_id=current_user.id, active_record=True
        ).all()
        form = EntryForm()
        if form.validate_on_submit():
            entry = Entry(
                date=form.date.data,
                time_of_day=form.time_of_day.data,
                mood=form.mood.data,
                status=form.status.data,
                weight=form.weight.data,
                measurement_waist=form.measurement_waist.data,
                keto=form.keto.data,
                user_id=current_user.id,
            )
            db.session.add(entry)
            db.session.commit()
            flash(f"You have submitted entry: {entry}", "success")
            return redirect(url_for("entries.entry_index"))
        return render_template(
            "entry_index.html",
            active_page="entry",
            entries=user_entries,
            form=form,
        )
    return redirect(url_for("main.home"))
