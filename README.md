<p align="center">
  <img src="susanoo-banner.webp" alt="SUSANOO Cloud Banner" width="800"/>
</p>

# 🔵 Cloud-Kill-Chain-Emulator
### *AWS Attack Simulator — IAM Escalation, S3 Enumeration, Container Breakout*

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AWS](https://img.shields.io/badge/AWS-Boto3-orange)](https://aws.amazon.com/)

---

## 👥 Who Can Use This Tool?

| Role | How They Use It |
| :--- | :--- |
| **🔴 Red Team Operators** | Simulate cloud attacks (S3 enumeration, IAM privilege escalation, container breakout). |
| **🟣 Purple Teamers** | Test cloud detection (GuardDuty, CloudTrail) against real AWS TTPs. |
| **🛡️ Cloud Security Engineers** | Validate IAM policies and S3 permissions. |
| **🎓 Security Students** | Learn AWS attack chains safely in a lab environment. |

> **⚠️ DISCLAIMER:** This tool is for **educational purposes and AUTHORIZED security testing ONLY**. The author is not responsible for any misuse. Use only on AWS accounts you own or have explicit written permission to test.

---

## 🎯 Features

- ✅ **S3 Bucket Enumeration**: Automatically lists all S3 buckets and attempts to access the target bucket.
- ✅ **IAM Privilege Escalation**: Attempts to assume a target IAM role to gain higher privileges.
- ✅ **Container Breakout Simulation**: Enumerates ECS clusters and containers (AWS ECS/EKS).
- ✅ **DRY RUN Mode**: Safety switch — simulate attacks without actually executing them.
- ✅ **SUSANOO Branding**: Professional Deep Blue banner on every run—HR approved.
- ✅ **Zero Cost for Learning**: Use AWS Free Tier to test in a lab environment.

---

## 📦 Installation (On Kali / Attacker Machine)

Open your terminal and run these **exact commands**:

```bash
git clone https://github.com/cossackrider8-glitch/Cloud-Kill-Chain-Emulator.git
cd Cloud-Kill-Chain-Emulator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
(Wait for all packages to install).

🔑 Configuration (AWS Credentials)
Step 1: Open the config file
bash
nano config.py
Step 2: Fill in your AWS credentials
Go to https://console.aws.amazon.com/iam/

Create a user with "AdministratorAccess" policy (for lab testing).

Generate an access key and download the CSV.

Paste the keys in config.py:

python
AWS_ACCESS_KEY_ID = "AKIA...YOUR_ACCESS_KEY_HERE..."
AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_KEY_HERE..."
AWS_REGION = "us-east-1"   # Change to your region
Step 3: Set Target (Optional)
python
TARGET_S3_BUCKET = "your-target-bucket-name"
TARGET_IAM_ROLE = "arn:aws:iam::123456789012:role/AdminRole"
Step 4: Safety Switch (VERY IMPORTANT)
python
DRY_RUN = True   # SET TO False ONLY IN A LAB
DRY_RUN = True → Simulates attacks without actually executing them.

DRY_RUN = False → Executes the actual attacks (use ONLY in your own AWS lab).

Save the file: CTRL + X, then Y, then Enter.

🚀 Usage (How to Run)
bash
python main.py
What happens next:
The Deep Blue SUSANOO banner prints.

It connects to AWS using your credentials.

Phase 1: Lists all S3 buckets and tries to access the target bucket.

Phase 2: Attempts to assume the target IAM role.

Phase 3: Enumerates ECS clusters for container breakout simulation.

Prints a full engagement report.

Example Output:
text
📡 PHASE 1: S3 Bucket Enumeration
[+] Found 12 buckets.
[+] Target bucket 'my-lab-bucket' found!
[+] Found 5 objects in bucket.
  - secret.txt (1024 bytes)
  - config.json (2048 bytes)

📡 PHASE 2: IAM Privilege Escalation
[+] Successfully assumed role: arn:aws:iam::123456789012:role/AdminRole
[+] Temporary credentials obtained.

📡 PHASE 3: Container Breakout Simulation
[+] Found 2 ECS clusters.
  - arn:aws:ecs:us-east-1:123456789012:cluster/default
❓ TROUBLESHOOTING
Problem	Solution
botocore.exceptions.NoCredentialsError	AWS keys missing in config.py.
AccessDenied on S3	IAM user doesn't have s3:ListBuckets permission.
DRY_RUN warnings	Set DRY_RUN = False in config.py to execute real attacks.
ECS enumeration fails	You may not have ECS clusters in your region. Ignore the error.
Virtual environment not activating	Run source venv/bin/activate
🗺️ MITRE ATT&CK Mapping (Industry Standard)
Tactic	Technique ID	Technique Name
Reconnaissance	T1595	Active Scanning (S3 Enumeration)
Privilege Escalation	T1078	Valid Accounts (IAM Role Assumption)
Execution	T1059	Command and Scripting Interpreter
Lateral Movement	T1210	Exploitation of Remote Services (Container Breakout)
Defense Evasion	T1027	Obfuscated Files or Information
📂 Repository Structure
text
Cloud-Kill-Chain-Emulator/
├── main.py              # Main engine (SUSANOO Banner + AWS attacks)
├── config.py            # AWS Credentials + Target Settings
├── requirements.txt     # Python dependencies (boto3, colorama)
├── susanoo-banner.webp  # Deep Blue Banner Image
└── README.md            # This complete manual
⚠️ Final Warning
This tool is for authorized security testing and educational purposes only.
Unauthorized access to AWS accounts is illegal. The creator assumes zero liability for misuse. By using this tool, you agree to use it ethically and legally.

🤝 Contributing
Found a bug or want to add new attack modules (e.g., Lambda, RDS)?
Open an issue or submit a Pull Request.

📜 License

MIT License - Free to use, modify, and distribute. See LICENSE for details.

Star ⭐ this repo if you found it useful! It helps other cybersecurity professionals find it. 🚀
MIT License - Free to use, modify, and distribute. See LICENSE for details.

Star ⭐ this repo if you found it useful! It helps other cybersecurity professionals find it. 🚀
