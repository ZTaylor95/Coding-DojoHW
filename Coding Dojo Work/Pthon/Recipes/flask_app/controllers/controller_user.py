from flask_app import app
from flask import flash, render_template, redirect, session, request
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def display_login():
    return render_template('login.html' )

@app.route('/user/registration', methods = ['POST'] )
def process_registration():
    if User.validate_registration(request.form) == False:
        return redirect('/')
    user_exists = User.get_one_to_validate_email(request.form)
    if user_exists != None:
        flash("This email already exists!", "error_registration_email")
        return redirect('/')


    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form['password'])
    }


    user_id = User.create(data)
    
    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id

    return redirect('/recipes')


@app.route('/user/login', methods=['POST'])
def process_login():
    current_user = User.get_one_to_validate_email(request.form)

    if current_user != None:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Invalid Log-in", "error_login_credentials")
            return redirect('/')

        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['user_id'] = current_user.id


        return redirect('/recipes')    
    else:
        flash("invalid credentials", "error_login_credentials")
        return redirect('/')

@app.route('/user/logout')
def process_logout():
    session.clear()
    return redirect('/')


















# @app.route('/user/new')
# def user_new():
#     return render_template('user_new.html')

# @app.route('/user/create', methods=['POST'])
# def create():
#     return redirect('/')

# @app.route('/user/<int:id>')
# def user_show(id):
#     return render_template('user_show.html')

# @app.route('/user/<int:id>/edit')
# def user_edit(id):
#     return render_template('user_edit.html')

# @app.route('/user/<int:id>/update', methods=['Post'])
# def user_update(id):
#     return redirect('/')

# @app.route('/user/<int:id>/delete')
# def user_delete(id):
#     return redirect('/')


# table_name/<int:id>/action