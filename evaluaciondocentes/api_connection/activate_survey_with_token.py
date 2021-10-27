from limesurveyrc2api.limesurvey import LimeSurvey
from collections import OrderedDict

url = "http://localhost"

username = "userxxxxx"
password = "*********"

# Open a session.
api = LimeSurvey(url=url, username=username)
api.open(password=password)

survey_id_tobeactivated = "2323232323"
attributefields = []

method = "activate_tokens"
params = OrderedDict([
    ("sSessionKey", api.session_key),
    ("iSurveyID", survey_id_tobeactivated),
    ("aAttributeFields", attributefields),
])
response = api.query(method=method, params=params)
response_type = type(response)

print(response_type)
print(response)








# Close the session.
api.close()