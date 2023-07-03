import requests

ENDPOINT = "https://todo.pixegami.io"

#get the response
global response
response = requests.get(ENDPOINT)

def test_verify_status_code():
    #response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_verify_body_message():
    body = response.json()
    assert body['message'] == 'Hello World from Todo API'

def test_verify_header_content():
    header = response.headers
    assert header['Content-Length'] == '39'
    assert header['Content-Type'] == 'application/json'
    assert header['Vary'] == 'Origin'
    assert header['x-amzn-remapped-content-length'] == '39'
    assert header['X-Cache'] == 'Miss from cloudfront'

# def test_can_create_task():
#     payload = {
#         "content":"my test content",
#         "user_id":"test user",
#         "task_id": "test_task_id",
#         "is_done": False,
#     }
#     create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
#     assert  create_task_response.status_code == 200
#
#     data = create_task_response.json()
#     print(data)
#
#     task_id = data["task"]["task_id"]
#     get_task_response = requests.get(ENDPOINT + "/get-task/{task_id}")
#
#     assert get_task_response.status_code == 200
#
#     get_task_data = get_task_response.json()
#     assert get_task_data["content"] == payload["content"]
#     assert get_task_data["user_id"] == payload["user_id"]
