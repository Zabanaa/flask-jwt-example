from flask import jsonify

class Response(object):

    def basic_auth_error():

        response = jsonify({
            "meta": {
                "type": "error",
                "status": 401
            },
            "body": {
                "message": "Please provide valid credentials"
            }
        })

        response.status_code = 401
        response.headers["WWW-Authenticate"] = "Basic realm=Login Required"
        return response

    def missing_auth_header():

        response = jsonify({
            "meta": {
                "type": "error",
                "status": 401
            },
            "body": {
                "message": "Missing Authorization Header"
            }
        })

        response.status_code = 401
        return response

    def badly_formatted_request():

        response = jsonify({
            "meta": {
                "type": "error",
                "status": 401
            },
            "body": {
                "message": "Bad request. Please check that the headers are formatted properly"
            }
        })

        response.status_code = 400
        return response

    def invalid_json_web_token():

        response = jsonify({
            "meta": {
                "type": "error",
                "status": 401
            },
            "body": {
                "message": "Could not verify token. It's either invalid or expired."
            }
        })

        response.status_code = 400
        return response

