from flask import jsonify, Response


def invalid_route() -> Response:
    op = {"error":
              {"msg": "404 error - Route doesnt exist."}
          }
    respmsg = jsonify({'result': op})
    respmsg.status_code = 404
    return respmsg


def unauth() -> Response:
    op = {"error":
              {"msg": "401 Error - The E-Mail or Password provided is not valid."}}

    respmsg = jsonify({'result': op})
    respmsg.status_code = 401
    return respmsg


def forbidden() -> Response:
    op = {"error":
              {"msg": "403 error - Unauthorized Access."}
          }
    respmsg = jsonify({'result': op})
    respmsg.status_code = 403
    return respmsg
