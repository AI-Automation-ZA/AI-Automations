---
description: How to launch the CRM Tool (Backend and Frontend)
---

Follow these steps to get the CRM system up and running on your local machine.

### Prerequisites
- Node.js (v24+) installed
- Python (3.13+) installed

### Step 1: Launch the Backend (API)
1. Open a new terminal.
2. Navigate to the backend directory:
   ```powershell
   cd "d:\Github Repos\AI-Automations\CRM Tool\backend"
   ```
3. Activate the Python virtual environment:
   ```powershell
   .\venv\Scripts\activate
   ```
4. Start the FastAPI server:
   ```powershell
   uvicorn main:app --reload
   ```
   > [!NOTE]
   > The API will be available at `http://localhost:8000`. You can view the interactive documentation at `http://localhost:8000/docs`.

### Step 2: Launch the Frontend (Web Interface)
1. Open a second terminal.
2. Navigate to the frontend directory:
   ```powershell
   cd "d:\Github Repos\AI-Automations\CRM Tool\frontend"
   ```
3. Start the Next.js development server:
   ```powershell
   npm run dev
   ```
4. Open your browser and navigate to `http://localhost:3000`.

### Step 3: Login to the System
Use the following fictitious credentials to access the CRM:
- **Username**: `admin`
- **Password**: `admin123`

---
### Troubleshooting
- **API Errors**: Ensure the backend server is running before attempting to log in.
- **Node Modules**: If the frontend fails to start, run `npm install` in the `frontend` directory.
