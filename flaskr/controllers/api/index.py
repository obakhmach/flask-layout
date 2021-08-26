from flask import (
    jsonify, Blueprint, current_app
)


NAME = 'index'

bp = Blueprint(NAME, __name__)


@bp.route("/")
@bp.route("/version")
def version():
    return jsonify({
    	"info": {"version": current_app.config.get("APP_VERSION")}
    	})
    