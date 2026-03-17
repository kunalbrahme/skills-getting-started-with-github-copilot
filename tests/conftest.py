import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball training and matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Tennis lessons and friendly competitions",
        "schedule": "Wednesdays and Saturdays, 4:00 PM - 5:30 PM",
        "max_participants": 10,
        "participants": ["lucy@mergington.edu"]
    },
    "Art Studio": {
        "description": "Painting, drawing, and visual arts exploration",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Club": {
        "description": "Theater performance and acting techniques",
        "schedule": "Thursdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["ava@mergington.edu"]
    },
    "Science Club": {
        "description": "Hands-on experiments and scientific discovery",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Debate Team": {
        "description": "Competitive debate and public speaking skills",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["alexander@mergington.edu"]
    }
}


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update({
        k: {
            "description": v["description"],
            "schedule": v["schedule"],
            "max_participants": v["max_participants"],
            "participants": list(v["participants"])
        }
        for k, v in INITIAL_ACTIVITIES.items()
    })
    yield
    activities.clear()
    activities.update({
        k: {
            "description": v["description"],
            "schedule": v["schedule"],
            "max_participants": v["max_participants"],
            "participants": list(v["participants"])
        }
        for k, v in INITIAL_ACTIVITIES.items()
    })


@pytest.fixture
def client():
    return TestClient(app)
