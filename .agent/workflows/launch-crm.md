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

### Step 0: Configure Environment (Optional but Recommended)
1. In the `backend` folder, copy `.env.example` to `.env`.
   - Update `ADMIN_USERNAME` and `ADMIN_PASSWORD` if you'd like to change defaults.
2. In the `frontend` folder, copy `.env.example` to `.env.local`.

### Step 3: Login to the System
Use the credentials you configured in your `.env` file (or the system defaults if no `.env` exists).

---
### Troubleshooting
- **API Errors**: Ensure the backend server is running before attempting to log in.
- **Node Modules**: If the frontend fails to start, run `npm install` in the `frontend` directory.
- **Security Check**: Never commit your `.env` files to git. They are already in `.gitignore` by default.
