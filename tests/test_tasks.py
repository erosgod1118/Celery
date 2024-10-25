import json

from tasks import create_task
from unittest.mock import patch

def test_create_task():
    assert create_task.run(1)
    assert create_task.run(2)
    assert create_task.run(3)

@patch("tasks.create_task.run")
def test_mock_create_task(mock_run):
    assert mock_run(2)
    mock_run.assert_called_once_with(2)

    assert mock_run(55)
    assert create_task.run.call_count == 2

    assert create_task.run(30)
    assert create_task.run.call_count == 3

# Integration test
def test_create_task_status(test_app):
    response = test_app.post(
        "/tasks",
        data=json.dumps({"type": 1})
    )
    content = response.json()
    task_id = content["task_id"]
    assert task_id

    response = test_app.get(f"tasks/{task_id}")
    content = response.json()
    assert content == {"task_id": task_id, "task_status": "PENDING", "task_result": None}
    assert response.status_code == 200

    while content["task_status"] == "PENDING":
        response = test_app.get(f"tasks/{task_id}")
        content = response.json()
    assert content == {"task_id": task_id, "task_status": "SUCCESS", "task_result": True}