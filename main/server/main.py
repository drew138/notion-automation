import os
from api.handler.settings import handler_config
from flask import Flask


def main():

    route = os.getenv("ROUTE", "")

    port = int(os.getenv("PORT", "8080"))

    app = Flask(__name__, template_folder="/app/templates")

    if route not in handler_config:
        raise Exception(f"Unknown route: {route}")

    method, handler = handler_config[route]

    app.route("/", methods=[method])(handler)

    app.run(host="0.0.0.0", port=port, debug=True)


if __name__ == "__main__":
    main()
