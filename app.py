from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_babel import Babel, _
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, UserNeed, Identity, AnonymousIdentity, identity_changed

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Tartaruga123@'
app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

def get_locale():
    lang = request.args.get('lang')
    if lang and lang in ['en', 'es', 'pt_BR']:
        resp = make_response(redirect(request.referrer or url_for('index')))
        resp.set_cookie('language', lang)
        return lang

    lang = request.cookies.get('language')
    if lang and lang in ['en', 'es', 'pt_BR']:
        return lang

    return request.accept_languages.best_match(['en', 'es', 'pt_BR'])

babel = Babel(app, locale_selector=get_locale)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

principals = Principal(app)
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

users = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'user': {'password': 'userpass', 'role': 'user'}
}

class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    user_data = users.get(user_id)
    if user_data:
        return User(user_id, user_data['role'])
    return None


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if current_user.is_authenticated:
        identity.provides.add(UserNeed(current_user.id))
        identity.provides.add(RoleNeed(current_user.role))

@app.context_processor
def inject_locale():
    return {'get_locale': get_locale}

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/change_language/<language>')
def change_language(language):
    if language not in ['en', 'es', 'pt_BR']:
        language = 'en'
    resp = make_response(redirect(request.referrer or url_for('index')))
    resp.set_cookie('language', language)
    return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.get(username)

        if user and user["password"] == password:
            user_obj = User(username, user["role"])
            login_user(user_obj)
            identity_changed.send(app, identity=Identity(user_obj.id))
            return redirect(url_for("index"))
        return _("Credenciais inválidas. Por favor, tente novamente.")
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return render_template('admin.html')

@app.route('/user')
@login_required
@user_permission.require(http_exception=403)
def user_dashboard():
    return render_template('user.html')

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.route('/users')
@login_required
def users_list():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    users_data = [{'id': i, 'name': f'User {i}'} for i in range(1, 30)]  # Simulando 100 usuários
    total = len(users_data)
    total_pages = (total + per_page - 1) // per_page
    users_paginated = users_data[(page - 1) * per_page: page * per_page]
    return render_template('user.html', users=users_paginated, page=page, total_pages=total_pages)

