from flask import jsonify, make_response
from task.work.update_assigned_issues_database import (
    UpdateAssignedIssuesDatabaseTask,
)


def index():
    task = UpdateAssignedIssuesDatabaseTask()
    task.run()
    return make_response(jsonify({"message": "Done"}), 201)
