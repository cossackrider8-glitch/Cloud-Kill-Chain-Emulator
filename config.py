# config.py - SUSANOO Cloud Kill-Chain Configuration

# ==============================================
# 1. AWS CREDENTIALS (Get from AWS Console)
# ==============================================
# Go to: AWS Console → IAM → Users → Create User
# Attach policy: "AdministratorAccess" (for testing only)
# Download the CSV file with Access Key & Secret

AWS_ACCESS_KEY_ID = "AKIA...YOUR_ACCESS_KEY_HERE..."
AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_KEY_HERE..."
AWS_REGION = "us-east-1"   # Change to your region

# ==============================================
# 2. TARGET SETTINGS (What to attack)
# ==============================================
# This is the S3 bucket we will try to enumerate/access
TARGET_S3_BUCKET = "your-target-bucket-name"

# This is the IAM role we will try to assume (privilege escalation)
TARGET_IAM_ROLE = "arn:aws:iam::123456789012:role/AdminRole"

# ==============================================
# 3. SAFETY SETTINGS (Prevent accidental real damage)
# ==============================================
# Set to True to simulate attacks without actually executing them
DRY_RUN = True   # CHANGE TO False for real execution (BE CAREFUL!)
