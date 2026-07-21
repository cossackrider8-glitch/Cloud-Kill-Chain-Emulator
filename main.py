#!/usr/bin/env python3
# main.py - SUSANOO Cloud Kill-Chain Emulator

import sys
import json
import time
import boto3
from botocore.exceptions import ClientError
from config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    TARGET_S3_BUCKET,
    TARGET_IAM_ROLE,
    DRY_RUN
)
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

# --- SUSANOO BANNER (Deep Blue / Royal Purple) ---
def print_banner():
    banner = f"""
{Fore.BLUE}{Style.BRIGHT}
    ███████╗██╗   ██╗███████╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ 
    ██╔════╝██║   ██║██╔════╝██╔══██╗████╗  ██║██╔═══██╗██╔═══██╗
    ███████╗██║   ██║███████╗███████║██╔██╗ ██║██║   ██║██║   ██║
    ╚════██║██║   ██║╚════██║██╔══██║██║╚██╗██║██║   ██║██║   ██║
    ███████║╚██████╔╝███████║██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝
    ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
{Fore.CYAN}
        [ CLOUD KILL-CHAIN EMULATOR v1.0 ]
{Fore.BLUE}
        >> AWS Attack Simulator - For Authorized Testing Only <<
{Fore.MAGENTA}
        Crafted by: Obito Uchiha [ h4ck3r ]  |  SUSANOO Protocol
{Fore.RESET}
    """
    print(banner)

# --- AWS Connection Check ---
def connect_aws():
    print(f"\n{Fore.CYAN}[+] Connecting to AWS ({AWS_REGION})...{Fore.RESET}")
    try:
        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        return session
    except Exception as e:
        print(f"{Fore.RED}[!] AWS Connection Failed: {e}{Fore.RESET}")
        sys.exit(1)

# --- PHASE 1: S3 Bucket Enumeration ---
def s3_enumeration(session):
    print(f"\n{Fore.YELLOW}[+] PHASE 1: S3 Bucket Enumeration{Fore.RESET}")
    s3 = session.client('s3')
    
    try:
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response.get('Buckets', [])]
        print(f"{Fore.GREEN}[+] Found {len(buckets)} buckets.{Fore.RESET}")
        
        # Check if target bucket exists
        if TARGET_S3_BUCKET in buckets:
            print(f"{Fore.GREEN}[+] Target bucket '{TARGET_S3_BUCKET}' found!{Fore.RESET}")
            # Try to list objects in target bucket
            if not DRY_RUN:
                try:
                    objects = s3.list_objects_v2(Bucket=TARGET_S3_BUCKET, MaxKeys=10)
                    if 'Contents' in objects:
                        print(f"{Fore.GREEN}[+] Found {len(objects['Contents'])} objects in bucket.{Fore.RESET}")
                        for obj in objects['Contents']:
                            print(f"  - {obj['Key']} ({obj['Size']} bytes)")
                    else:
                        print(f"{Fore.YELLOW}[!] Bucket is empty or no access.{Fore.RESET}")
                except ClientError as e:
                    print(f"{Fore.RED}[!] Cannot access bucket: {e}{Fore.RESET}")
            else:
                print(f"{Fore.YELLOW}[!] DRY RUN: Would have accessed bucket {TARGET_S3_BUCKET}{Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}[!] Target bucket '{TARGET_S3_BUCKET}' not found.{Fore.RESET}")
            
    except ClientError as e:
        print(f"{Fore.RED}[!] S3 Enumeration Failed: {e}{Fore.RESET}")

# --- PHASE 2: IAM Privilege Escalation ---
def iam_privilege_escalation(session):
    print(f"\n{Fore.YELLOW}[+] PHASE 2: IAM Privilege Escalation{Fore.RESET}")
    iam = session.client('iam')
    
    try:
        # List current user/role
        user = iam.get_user()
        username = user['User']['UserName']
        print(f"{Fore.GREEN}[+] Current User: {username}{Fore.RESET}")
        
        # Try to assume target role
        if not DRY_RUN:
            sts = session.client('sts')
            try:
                response = sts.assume_role(
                    RoleArn=TARGET_IAM_ROLE,
                    RoleSessionName="SUSANOO-Session"
                )
                print(f"{Fore.GREEN}[+] Successfully assumed role: {TARGET_IAM_ROLE}{Fore.RESET}")
                print(f"{Fore.GREEN}[+] Temporary credentials obtained.{Fore.RESET}")
            except ClientError as e:
                print(f"{Fore.RED}[!] Role assumption failed: {e}{Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}[!] DRY RUN: Would have assumed role {TARGET_IAM_ROLE}{Fore.RESET}")
            
    except ClientError as e:
        print(f"{Fore.RED}[!] IAM Enumeration Failed: {e}{Fore.RESET}")

# --- PHASE 3: Container Breakout (ECS/EKS) ---
def container_breakout(session):
    print(f"\n{Fore.YELLOW}[+] PHASE 3: Container Breakout Simulation{Fore.RESET}")
    
    if not DRY_RUN:
        ecs = session.client('ecs')
        try:
            # List ECS clusters
            clusters = ecs.list_clusters()
            if clusters['clusterArns']:
                print(f"{Fore.GREEN}[+] Found {len(clusters['clusterArns'])} ECS clusters.{Fore.RESET}")
                for cluster in clusters['clusterArns'][:3]:
                    print(f"  - {cluster}")
            else:
                print(f"{Fore.YELLOW}[!] No ECS clusters found.{Fore.RESET}")
        except ClientError as e:
            print(f"{Fore.YELLOW}[!] ECS access limited: {e}{Fore.RESET}")
    else:
        print(f"{Fore.YELLOW}[!] DRY RUN: Would have enumerated ECS containers.{Fore.RESET}")
    
    print(f"{Fore.MAGENTA}[*] Container Breakout simulation complete.{Fore.RESET}")

# --- MAIN EXECUTION ---
def main():
    # Print SUSANOO Banner
    print_banner()
    
    # Check AWS Credentials
    if "YOUR_ACCESS_KEY_HERE" in AWS_ACCESS_KEY_ID:
        print(f"{Fore.RED}[!] ERROR: Please set AWS credentials in config.py!{Fore.RESET}")
        sys.exit(1)
    
    print(f"\n{Fore.CYAN}[+] SUSANOO Cloud Kill-Chain Emulator Initialized.{Fore.RESET}")
    print(f"{Fore.CYAN}[+] Target S3 Bucket: {TARGET_S3_BUCKET}{Fore.RESET}")
    print(f"{Fore.CYAN}[+] Target IAM Role: {TARGET_IAM_ROLE}{Fore.RESET}")
    print(f"{Fore.YELLOW}[!] DRY RUN Mode: {'ON' if DRY_RUN else 'OFF'}{Fore.RESET}")
    print(f"{Fore.YELLOW}[!] Set DRY_RUN = False in config.py for real execution.{Fore.RESET}")
    
    # Connect to AWS
    session = connect_aws()
    
    # Execute Attack Chain
    print(f"\n{Fore.BLUE}{'='*60}{Fore.RESET}")
    print(f"{Fore.BLUE}        SUSANOO KILL-CHAIN EXECUTION{Fore.RESET}")
    print(f"{Fore.BLUE}{'='*60}{Fore.RESET}")
    
    s3_enumeration(session)
    iam_privilege_escalation(session)
    container_breakout(session)
    
    print(f"\n{Fore.GREEN}{'='*60}{Fore.RESET}")
    print(f"{Fore.GREEN}[+] SUSANOO Kill-Chain Emulation Complete!{Fore.RESET}")
    print(f"{Fore.GREEN}{'='*60}{Fore.RESET}")
    print(f"\n{Fore.MAGENTA}[!] Remember: This tool is for authorized testing only.{Fore.RESET}")

if __name__ == "__main__":
    main()
