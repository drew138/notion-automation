from flask import jsonify, make_response
from task.finances.append_transactions_database import (
    AppendTransactionsDatabase,
)


def index():
    task = AppendTransactionsDatabase()
    task.run()
    return make_response(jsonify({"message": "Done"}), 201)
