from flask import (
    Blueprint,
    Response,
    jsonify,
    render_template
)

from src.utils.controller_utils import (
    get_host_info,
    cut_json,
    merge_dicts
)
from src.pokeneas.pokenea import Pokenea
from src.pokeneas.pokeneas import get_random_pokenea


controller_bp = Blueprint("controller", __name__)

@controller_bp.route("/pokenea", methods=["GET"])
def get_pokenea() -> Response:
    host_info:dict = get_host_info()
    pokenea: Pokenea = get_random_pokenea()
    response: dict = merge_dicts(
        host_info,
        cut_json(pokenea.json(), "name", "ability", "height")
    ) 
    return jsonify(response), 200

@controller_bp.route("/phrase", methods = ["GET"])
def get_phrase() -> Response:
    host_info: dict = get_host_info()
    pokenea: Pokenea = get_random_pokenea()
    response: dict = merge_dicts(
        host_info,
        cut_json(pokenea.json(), "name", "image", "philosophical_frase")
    )
    return render_template("template.html", data=response)