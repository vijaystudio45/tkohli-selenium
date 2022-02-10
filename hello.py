import requests
import json
test={"org_id":3,"api_key":"hello","msg_merge_id":1}
r = requests.post('https://dev-app.sndright.com/api/conversation_api/delete_message_merge', data =json.dumps(test))

print(r.json())
