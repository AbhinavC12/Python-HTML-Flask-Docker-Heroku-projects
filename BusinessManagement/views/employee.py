from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = "SELECT e.id as id, e.first_name, e.last_name, e.email, e.company_id, c.name as company_name FROM IS601_MP2_Employees e LEFT JOIN IS601_MP2_Companies c ON e.company_id = c.id WHERE 1=1"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn = request.args.get('first_name')
    ln = request.args.get('last_name')
    email = request.args.get('email')
    company = request.args.get('company')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')
    # TODO search-3 append like filter for first_name if provided
    if fn:
        query += " AND e.first_name like %s"
        args.append(f"%{fn}%")
    # TODO search-4 append like filter for last_name if provided
    if ln:
        query += " AND e.last_name like %s"
        args.append(f"%{ln}%")
    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND e.email like %s"
        args.append(f"%{email}%")
    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND e.company_id = %s"
        args.append(int(company))
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        company = request.form.get("company")
        print(company)
        email = request.form.get("email")
        if first_name == "":
            flash("Enter first name", 'warning')
            return redirect(request.url)
        if last_name == "":
            flash("Enter last name", 'warning')
            return redirect(request.url)
        if email == "":
            flash("Enter email", 'warning')
            return redirect(request.url)
        
        try:
            result = DB.insertOne("""INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(company_name)s)""",
                        #ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1)""",
            {'first_name':first_name, 'last_name':last_name, 'email':email, 'company_name':company})
            # <-- TODO add-6 add query and add arguments
            if result.status:
                flash("Created Employee Record", "success")
        except Exception as e:
            # TODO add-7 make message user friendly
            flash(str(e), "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    print(id)
    if True: # TODO update this for TODO edit-1
        print("True if")
        if request.method == "POST":
            print("POST if")
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.get.args("first_name")
            print(first_name)
            last_name = request.get.args("last_name")
            company_id = request.get.args("company_id")
            email = request.get.args("email")
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == "":
                flash("First name is required", 'warning')
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == "":
                flash("Last name is required", 'warning')
            # TODO edit-4 company may be None
            # TODO edit-5 email is required (flash proper error message)
            if email == "":
                flash("Email is required", 'warning')
            data = [first_name, last_name, company_id, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                result = DB.update("""
                UPDATE IS601_MP2_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s 
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash(e, "danger")
        try:
            print("try")
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            result = DB.selectOne("SELECT e.first_name, e.last_name, e.email, e.company_id c.name FROM IS601_MP2_Employees e LEFT JOIN IS601_MP2_Companies c ON e.company_id = c.id WHERE e.id =%s", id)
            print(result)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row = row)

@employee.route("/delete", methods=["GET"])
def delete():
    id = request.args.get('id')
    args = {**request.args}
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    if id:
        result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id = %s", id)
        del args['id']
        if result:
            flash("Deleted successfully")
    return redirect(url_for("employee.search", **args))
    pass