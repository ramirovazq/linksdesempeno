from collections import OrderedDict
from limesurveyrc2api.exceptions import LimeSurveyError
from limesurveyrc2api.limesurvey import LimeSurvey


url = "http://localhost:443"
username = "userxxxxx"
password = "*********"

lime = LimeSurvey(url=url, username=username)
lime.open(password=password)

la_session_key = lime.session_key

idtoactivate = "111111"
idtoactivate = "222222"


method = "activate_survey"
params = OrderedDict([
    ("sSessionKey", la_session_key),
    ("iSurveyID", idtoactivate),
])
response = lime.query(method=method, params=params)
response_type = type(response)

if response_type is dict and "status" in response:
    status = response["status"]
    error_messages = [
        "Error: Invalid survey ID",
        "Invalid survey ID",
        "No token table",
        "No permission"
    ]
    for message in error_messages:
        if status == message:
            lime.close()
            raise LimeSurveyError(method, status)

lime.close()
