from fastapi.testclient import TestClient
import json
import os

from main import app

def test_unauthorized_access():
    print("Testing unauthorized access to /dashboard...")
    with TestClient(app) as client:
        response = client.get("/dashboard")
        assert response.status_code == 401
        print("SUCCESS: 401 Unauthorized as expected.")

def test_login_and_secure_access():
    admin_username = os.getenv("ADMIN_USERNAME", "admin")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")

    print("Testing login with admin user...")
    with TestClient(app) as client:
        response = client.post(
            "/token",
            data={"username": admin_username, "password": admin_password},
        )
        assert response.status_code == 200
        token = response.json()["access_token"]
        print("SUCCESS: Logged in!")

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
