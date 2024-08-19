from flask import jsonify, make_response
from task.work.update_reviewer_issues_database import (
    UpdateReviewerIssuesDatabaseTask,
)


def index():
    task = UpdateReviewerIssuesDatabaseTask()
    task.run()
    return make_response(jsonify({"message": "Done"}), 201)
