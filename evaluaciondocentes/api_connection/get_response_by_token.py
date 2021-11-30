from limesurveyrc2api.limesurvey import LimeSurvey
from collections import OrderedDict

def decode_msg(msg_in_64):
    import base64
    base64_message = msg_in_64
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

url='http://local'
username='bla'
password='hola'

token = 'token'
survey_id = 1111111
document_type="json"

api = LimeSurvey(url=url, username=username)
api.open(password=password)

method = "export_responses_by_token"
params = OrderedDict([
    ("sSessionKey", api.session_key),
    ("iSurveyID", survey_id),
    ("sDocumentType", document_type),
    ("sToken", token)
])

response = api.query(method=method, params=params)
response_type = type(response)

print("type .........")
print(response_type)
print("response .......")
print(response)
if isinstance(response, str):
    response_decode = decode_msg(response)
    print("response decode.......")
    print(response_decode)

'''
<class 'str'>
64-encoded string
eyJyZXNw
'''
api.close()