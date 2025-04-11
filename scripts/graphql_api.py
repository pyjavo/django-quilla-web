import jwt
import requests
import os
from lektor.utils import slugify


# Load environment variables
CLIENT_ID = os.getenv("MEETUP_CLIENT_ID")
AUTHORIZED_MEMBER_ID = os.getenv("MEETUP_MEMBER_ID")
SIGNING_KEY_ID = os.getenv("MEETUP_SIGNING_KEY_ID")
MEETUP_API_URL = "https://api.meetup.com/gql-ext"
GROUP_URLNAME = os.getenv("MEETUP_GROUP_URLNAME")
PRIVATE_KEY = os.getenv("MEETUP_PRIVATE_KEY")

# Generate JWT Token
payload = {
    "iss": CLIENT_ID,
    "sub": AUTHORIZED_MEMBER_ID,
    "aud": "api.meetup.com",
    "exp": 120
}

jwt_token = jwt.encode(
    payload,
    PRIVATE_KEY,
    algorithm="RS256",
    headers={"kid": SIGNING_KEY_ID}
)

# GraphQL Query to Fetch Events
query = """
    query {
        groupByUrlname(urlname: "%s") {
            events(status: PAST, sort: DESC) {
            edges {
                node {
                    id
                    title
                    dateTime
                    eventUrl
                    description
                    featuredEventPhoto {
                        standardUrl
                    }
                    venues {
                        name
                        address
                    }
                }
                }
            }
        }
    }
""" % GROUP_URLNAME

# Send Request to Meetup API
headers = {"Authorization": f"Bearer {jwt_token}"}
response = requests.post(MEETUP_API_URL, json={"query": query}, headers=headers)
data = response.json()

# Print Fetched Event Data (Instead of Writing to Files)
for event in data["data"]["groupByUrlname"]["events"]["edges"]:
    event_data = event["node"]
    slug = f"{event_data['dateTime'][:10]}-{slugify(event_data['title'])}"
    print(f"https://pybaq.co/eventos/{slug}")
    print(f"Slug: {slug}")
    print(f"Event ID: {event_data['id']}")
    print(f"Titulo: {event_data['title']}")
    print(f"Fecha: {event_data['dateTime']}")
    print(f"URL: {event_data['eventUrl']}")
    print(f"Imagen: {event_data['featuredEventPhoto']}")
    print(f"Descripción: {event_data['description']}")
    print(f"Lugar: {event_data['venues']}")
    print("-" * 40)  # Separator for readability

print("Test run completed! ✅")