from flask import Blueprint, render_template
from app.models.employee import Employee
from collections import defaultdict

department_bp = Blueprint("department", __name__)

@department_bp.route("/department")
def departmentHome():

    employees = Employee.query.all()

    departments = defaultdict(list)

    for emp in employees:
        departments[emp.department].append(emp)

    return render_template(
        "department.html",
        departments=departments
    )