from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_unauthorized_access():
    print("Testing unauthorized access to /dashboard...")
    response = client.get("/dashboard")
    assert response.status_code == 401
    print("SUCCESS: 401 Unauthorized as expected.")

def test_login_and_secure_access():
    print("Testing login with admin user...")
    response = client.post(
        "/token",
        data={"username": "admin", "password": "admin123"},
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    print("SUCCESS: Logined in!")

    headers = {"Authorization": f"Bearer {token}"}
    
    print("Testing /dashboard with token...")
    response = client.get("/dashboard", headers=headers)
    assert response.status_code == 200
    print(f"SUCCESS: Dashboard stats: {json.dumps(response.json(), indent=2)}")

    print("Testing /accounts with token...")
    response = client.get("/accounts?limit=5", headers=headers)
    assert response.status_code == 200
    print(f"SUCCESS: Received {len(response.json())} accounts.")

    print("Testing /pipeline with token...")
    response = client.get("/pipeline?limit=5", headers=headers)
    assert response.status_code == 200
    print(f"SUCCESS: Received {len(response.json())} pipeline items.")

if __name__ == "__main__":
    try:
        test_unauthorized_access()
        test_login_and_secure_access()
        print("\nALL VERIFICATION TESTS PASSED!")
    except Exception as e:
        print(f"\nVERIFICATION FAILED: {e}")
        import traceback
        traceback.print_exc()
