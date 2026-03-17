"""Tests for the activity management API using AAA pattern."""

def test_get_activities_returns_all(client):
    # Arrange: client fixture is ready

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_signup_adds_participant(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]

    activities_response = client.get("/activities")
    assert student_email in activities_response.json()[activity_name]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_activity_not_found_returns_404(client):
    # Arrange
    activity_name = "Fake Club"
    student_email = "test@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_full_activity_returns_400(client):
    # Arrange
    activity_name = "Tennis Club"
    for i in range(9):
        client.post(f"/activities/{activity_name}/signup", params={"email": f"dummy{i}@mergington.edu"})

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": "overflow@mergington.edu"})

    # Assert
    assert response.status_code == 400
    assert "Activity is full" in response.json()["detail"]


def test_delete_signup_removes_participant(client):
    # Arrange
    activity_name = "Programming Class"
    student_email = "emma@mergington.edu"
    # ensure present first
    before = client.get("/activities").json()
    assert student_email in before[activity_name]["participants"]

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 200
    assert "Removed" in response.json()["message"]

    after = client.get("/activities").json()
    assert student_email not in after[activity_name]["participants"]


def test_delete_nonexistent_participant_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "nobody@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 404
    assert "not signed up" in response.json()["detail"]


def test_delete_activity_not_found_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Club"
    student_email = "test@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
