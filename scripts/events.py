import json
import requests

# TODO: Create logic for oauth authentication when required

past_events_request = requests.get('https://api.meetup.com/pythonbaq/events?&sign=true&photo-host=secure&page=200&fields=featured_photo&desc=true&status=past')
future_events_request = requests.get('https://api.meetup.com/pythonbaq/events?&sign=true&photo-host=secure&page=3&fields=featured_photo')


meetup_responses = json.dumps({
    "past_events": past_events_request.json(),
    "future_events": future_events_request.json()
})

with open("databags/meetup.json", "w") as outfile: 
    outfile.write(meetup_responses) 