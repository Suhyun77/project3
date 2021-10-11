from flask import Blueprint, render_template

bp = Blueprint('user', __name__, url_prefix='/')


@bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')