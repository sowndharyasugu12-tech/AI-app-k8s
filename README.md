**1. High-Level Flow**
Developer → GitHub → Docker Build → Docker Hub → Kubernetes Cluster → Service → User Access

**2. Application Layer**
Source Code (GitHub)
Application code (likely Python / Streamlit / AI agent based on your previous work)
Contains:
app.py (frontend/UI)
agent logic (AI behavior)
requirements.txt

**3. Container Layer (Docker)**
Docker responsibilities:
Packages:
App code
Runtime (Python/Node/etc.)
Dependencies
Output:
Docker Image (versioned)
Stored in Docker Hub

**4. Kubernetes Layer**
Core Components in your project:
🔹 Deployment
Manages Pods
Handles rolling updates
Ensures replicas are running
🔹 Pods
Runs your AI application container
🔹 Service
Exposes application inside cluster
Likely NodePort / LoadBalancer
🔹 ConfigMap / Secrets (if used)
Config values (API keys, endpoints)

