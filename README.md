
# Inspection System - Environment Setup

This repository contains the foundational setup for a full-stack computer vision inspection system. The actual application code and database schemas will be implemented later. This guide focuses strictly on setting up the development environment, infrastructure, and dependencies.

## Tech Stack

### Infrastructure
* **Database:** PostgreSQL 16
* **Object Store:** MinIO (S3-compatible)
* **Task Queue Broker:** Redis
* **Orchestration:** Apache Airflow 2.x

### Backend & CV
* **API:** FastAPI, Uvicorn
* **ORM/Migrations:** SQLAlchemy 2.x, Alembic
* **CV/ML:** OpenCV, Ultralytics (YOLO), PyTorch, Supervision
* **Task Queue:** Celery
* **Utilities:** python-jose, passlib, minio, pydantic-settings

### Frontend
* **Framework:** React 18 + Vite
* **Styling:** Tailwind CSS v4
* **UI/Data:** shadcn/ui, Recharts, React Query

---

## 🚀 Setup & Installation Guide

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* Python 3.11+
* Node.js 18+ and npm

### 1. Infrastructure Setup (Docker)
Start by spinning up the database, object store, task broker, and orchestrator.

```bash
# From the project root directory
docker-compose up -d
```
*Verify:* Open Docker Desktop to ensure `inspection_db`, `minio`, `inspection_redis`, and `airflow` are running.
* Airflow UI: `http://localhost:8080` (admin / admin)
* MinIO Console: `http://localhost:9001` (admin / password)

---

### 2. Backend Setup (FastAPI + CV)

Navigate to the backend folder and create a Python virtual environment.

```bash
cd backend
python -m venv venv

# Activate the virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate
```

Install backend dependencies. *(Note: If you encounter `cython_sources` errors during this step on Windows, run `python -m pip install --upgrade pip` and `pip install --only-binary :all: pyyaml` first).*

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install PyTorch (CPU version for local dev)
pip install torch torchvision torchaudio

# Install core API, CV, and Celery packages
# Note: Quotes are required in PowerShell to escape brackets!
pip install fastapi "uvicorn[standard]" "sqlalchemy[asyncio]" asyncpg alembic "python-jose[cryptography]" "passlib[bcrypt]" python-multipart minio pydantic-settings pydantic
pip install celery redis opencv-python ultralytics numpy pillow supervision

# Save dependencies to requirements.txt
pip freeze > requirements.txt
```

*(Optional)* Create an `.env` file in the `backend/` directory for future use:
```env
DATABASE_URL=postgresql+asyncpg://admin:password@localhost:5432/inspection_db
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=admin
MINIO_SECRET_KEY=password
MINIO_BUCKET=inspections
JWT_SECRET=super-secret-key-change-in-production
```

---

### 3. Frontend Setup (React + Vite)

Open a **new terminal** and navigate to the root project directory.

```bash
# Scaffold Vite React app
npm create vite@latest frontend -- --template react

cd frontend
npm install
```

Install Tailwind CSS v4 and frontend dependencies:
```bash
# Install Tailwind and Vite plugin
npm install tailwindcss @tailwindcss/vite

# Install UI and data fetching libraries
npm install @tanstack/react-query recharts lucide-react class-variance-authority clsx tailwind-merge tailwindcss-animate
```

Configure `vite.config.js` to use Tailwind:
```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
})
```

Add Tailwind to your CSS (`src/index.css`):
```css
@import "tailwindcss";
```

Start the frontend development server to verify it works:
```bash
npm run dev
```
* Frontend available at: `http://localhost:5173`

---

## Git Setup & Best Practices

Initialize git and ensure virtual environments and node modules are ignored:
```bash
# In the project root
git init
```

Create a `.gitignore` file in the root directory:
```text
# Virtual environments
venv/
env/
.env

# Python cache
__pycache__/
*.pyc

# Node modules
frontend/node_modules/

# IDE folders
.vscode/
.idea/
```

Commit your environment setup:
```bash
git add .
git commit -m "chore: initial environment setup (Docker, Backend, Frontend)"
```

---


```