from functools import wraps
from app.routes import current_user, redirect, url_for

def login_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapped