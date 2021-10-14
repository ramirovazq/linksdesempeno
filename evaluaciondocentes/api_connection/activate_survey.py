from limesurveyrc2api.limesurvey import LimeSurvey

url = "http://localhost"

username = "userxxxxx"
password = "*********"

# Open a session.
api = LimeSurvey(url=url, username=username)
api.open(password=password)

idtoactivate = "146211"


result = api.survey.activate_survey(idtoactivate)
print(result)

# Close the session.
api.close()