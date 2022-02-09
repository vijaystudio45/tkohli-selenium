def hello(k):
	import requests
	r = requests.post('https://dev-app.sndright.com/api/conversation_api/delete_message_merge', data ={"org_id":3,"api_key":"hello","msg_merge_id":1})
	print(r.json())
print(hello('join'))
