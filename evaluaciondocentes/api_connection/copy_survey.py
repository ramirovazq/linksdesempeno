from limesurveyrc2api.limesurvey import LimeSurvey

url = "http://localhost"

username = "userxxxx"
password = "*********"

# Open a session.
api = LimeSurvey(url=url, username=username)
api.open(password=password)

# Get a list of surveys the admin can see, and print their IDs.
grupo = "GPO Z"
maestro = "MAESTRO ABC"
idtocopy = "111111"
newsurvey_name = f" test {maestro} {grupo}"

result = api.survey.copy_survey(idtocopy, newsurvey_name)
print(result)

# Close the session.
api.close()