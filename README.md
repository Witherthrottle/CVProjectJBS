Here is a lean, copy-paste-ready `README.md` containing **only the exact steps** a developer needs to run to get the project up and running. 

```markdown
# Project Setup

### 1. Prerequisites
Install Docker Desktop, Python 3.11+, and Node.js 18+.

### 2. Start Infrastructure
From the project root directory, run:
```bash
docker-compose up -d
```
*Access UIs:*
* Airflow: `http://localhost:8080` (admin / admin)
* MinIO: `http://localhost:9001` (admin / password)
* pgAdmin: `http://localhost:5050` (admin@admin.com / password)
  * *To connect pgAdmin to the DB, use Host: `db`, Port: `5432`, User: `admin`, Pass: `password`*

### 3. Setup Backend
```bash
cd backend
python -m venv venv

# Activate venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate venv (Mac/Linux)
# source venv/bin/activate

pip install -r requirements.txt
```

### 4. Setup Frontend
Open a new terminal window and run:
```bash
cd frontend
npm install
```

### 5. Run the Applications
*Start Backend (from the `backend` folder with venv activated):*
```bash
uvicorn main:app --reload
```

*Start Frontend (from the `frontend` folder):*
```bash
npm run dev
```