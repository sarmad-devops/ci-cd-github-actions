# ⚙️ CI/CD Pipeline — GitHub Actions + Docker + DockerHub

Automated CI/CD pipeline that tests, builds, and pushes a Docker image to DockerHub on every push to main branch.

---

## 🔄 Pipeline Flow
Code Push to GitHub
│
▼
┌───────────────┐
│  Run Tests    │ ← pytest
└──────┬────────┘
│ Pass ✅
▼
┌───────────────┐
│ Docker Build  │ ← Multi-stage
│   & Push      │ ← DockerHub
└──────┬────────┘
│
▼
┌───────────────┐
│ Security Scan │ ← Trivy
└───────────────┘
---

## ✅ Pipeline Features

- Automated testing before every build
- Multi-stage Docker image build
- Auto push to DockerHub on main branch
- Image tagged with both `latest` and commit SHA
- Trivy security vulnerability scan
- Pipeline fails if tests fail — no bad code gets deployed

---

## 📁 Project Structure
ci-cd-github-actions/
├── app/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Dependencies
│   ├── Dockerfile          # Multi-stage build
│   └── test_app.py         # Pytest test cases
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions pipeline
└── README.md

---

## 🐳 Docker Image
```bash
docker pull sarmad122/ci-cd-app:latest
docker run -p 5000:5000 sarmad122/ci-cd-app:latest
```

---

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Welcome message |
| `/health` | Health check status |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| GitHub Actions | CI/CD automation |
| Python Flask | Web application |
| Pytest | Automated testing |
| Docker | Containerization |
| DockerHub | Image registry |
| Trivy | Security scanning |