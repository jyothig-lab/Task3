PROJECT STRUCTURE

schoolbus-address-change/
│
├── .github/
│   └── workflows/
│       └── docker-ci-cd.yml
│
├── docker-compose.yml
├── .env
│
├── app/backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── nginx/frontend
│   ├── nginx.conf
│   └── index.html
│
└── mysql/
    └── init.sql


WORKFLOW EXECUTION

Git Push
   │
   ▼
GitHub Actions Triggered
   │
   ▼
Checkout Code
   │
   ▼
Login to Docker Hub
   │
   ▼
Build Docker Image
   │
   ▼
Tag Image
   │
   ▼
Push to Docker Hub
   │
   ▼
(Optional)
Deploy to AWS EC2

Expected Output :--------------

After pushing code to the main branch:

✅ GitHub Actions workflow starts automatically.
✅ Docker image is built.
✅ Image is tagged with the GitHub run number (e.g., 1, 2, 3).
✅ Image is also tagged as latest.
✅ Both tags are pushed to Docker Hub.

This implementation satisfies the task requirements of:

✅ Automatic build on every GitHub push
✅ Docker image creation
✅ Automatic push to Docker Hub
✅ Image versioning using the workflow run number
