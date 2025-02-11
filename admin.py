from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Course, Chapter, Lecture, Note

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        return redirect(url_for('home'))
    courses = Course.query.all()
    return render_template('admin_dashboard.html', courses=courses)

@admin_bp.route('/add_course', methods=['POST'])
@login_required
def add_course():
    title = request.form.get('title')
    description = request.form.get('description')
    new_course = Course(title=title, description=description)
    db.session.add(new_course)
    db.session.commit()
    return redirect(url_for('admin.dashboard'))
