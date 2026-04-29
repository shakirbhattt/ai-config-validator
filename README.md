# 🚀 AI Config Validator (Terraform + Kubernetes)

> AI-powered tool to detect misconfigurations in Terraform and Kubernetes and provide actionable recommendations for security, reliability, and cost optimization.

---

## 🧠 Overview

Infrastructure misconfigurations are a leading cause of outages, security issues, and unnecessary cloud costs.

**AI Config Validator** helps DevOps/SRE engineers by:

- 🔍 Detecting misconfigurations automatically  
- 🔐 Highlighting security risks  
- 💰 Suggesting cost optimizations  
- ⚡ Providing AI-powered recommendations  

---

## 🎯 Key Features

- ✅ Terraform validation (security & best practices)  
- ✅ Kubernetes YAML validation  
- 🤖 AI-powered analysis (LLM-based insights)  
- ⚡ Fast static checks + intelligent suggestions  
- 📦 Simple CLI-based workflow  

---

## 🏗️ Architecture

```
Infra Files (Terraform / K8s YAML)
            ↓
     Static Validators
            ↓
       AI Engine
            ↓
   Issues + Suggestions Output
```

---

## 📂 Project Structure

```
ai-config-validator/
├── main.py
├── validators/
│   ├── terraform.py
│   ├── kubernetes.py
│   └── ai.py
├── utils/
│   └── loader.py
├── sample-test-files/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai-config-validator.git
cd ai-config-validator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API key

```bash
export OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

1. Add your Terraform or Kubernetes files into a folder (e.g., `sample/`)
2. Run:

```bash
python main.py
```

---

## 🧪 Example Input

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-app
spec:
  template:
    spec:
      containers:
        - name: app
          image: nginx:latest
```

### Terraform

```hcl
resource "aws_security_group" "bad" {
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

## 📊 Example Output

```
🔍 Checking: deployment.yaml
❌ Deployment: Missing resource limits
❌ Deployment: Using latest tag in image nginx:latest

🤖 AI Suggestions:
- Add CPU/memory limits
- Avoid latest image tag
- Add liveness/readiness probes
```

---

## 🔍 Validation Rules

### Kubernetes
- Missing resource limits  
- Use of `latest` image tag  

### Terraform
- Open security groups (`0.0.0.0/0`)  
- Public exposure risks  
- Weak instance configurations  

---

## 🤖 AI Analysis

Provides:
- Security improvements  
- Cost optimization suggestions  
- Reliability recommendations  
- Best practices  

---

## 🧠 Use Cases

- Pre-commit validation  
- CI/CD checks  
- Infra code reviews  
- Security audits  
- Cost optimization  

---

## ⚠️ Limitations

- Terraform parsing is basic (string-based)  
- Requires OpenAI API key  
- AI output depends on model quality  

---

## 🚀 Roadmap

- [ ] CLI command (`ai-validator scan ./path`)  
- [ ] GitHub Actions integration  
- [ ] Advanced Terraform parsing  
- [ ] Policy engine (OPA)  
- [ ] Severity levels  
- [ ] Helm support  
- [ ] Docker support  

---

## 🤝 Contributing

1. Fork repo  
2. Create branch  
3. Submit PR  

---

## 📜 License

MIT License

---

## 💡 About

Built by a DevOps/SRE engineer to solve real-world infrastructure challenges using automation and AI.

---

## ⭐ Support

If you found this useful, give it a star ⭐
