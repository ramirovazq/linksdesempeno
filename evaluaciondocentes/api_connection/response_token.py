from limesurveyrc2api.limesurvey import LimeSurvey

url='http://localhost'
username='unuser'
password='xxxxx'

token = '11111222'
surveyid = "CCCCCCCC"

# Open a session.
api = LimeSurvey(url=url, username=username)
api.open(password=password)

result = api.token.export_responses_by_token(surveyid, token)
print(result)

# Close the session.
api.close()