from flask import Flask, render_template, redirect 
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .models import db
from flask_migrate import Migrate

#boilerplate
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

#example blueprints 
#app.register_blueprint(jokes_routes)
#app.register_blueprint(users_routes, url_prefix="/users")

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

#start here ...
