import os
import json
from jira import JIRA
import sys

def generate_release_notes(sprint_name):
    try:
        print("Starting generate_release_notes function")
        
        jira_token = os.environ.get('JIRA_API_TOKEN')
        jira_domain = os.environ.get('JIRA_DOMAIN')

        print(f"JIRA_API_TOKEN exists: {bool(jira_token)}")
        print(f"JIRA_DOMAIN exists: {bool(jira_domain)}")

        if not jira_token or not jira_domain:
            raise ValueError("JIRA_API_TOKEN or JIRA_DOMAIN environment variables are not set")

        print(f"Connecting to Jira domain: {jira_domain}")
        jira = JIRA(server=f"https://{jira_domain}", token_auth=jira_token)
        
        print(f"Fetching tickets for sprint: {sprint_name}")
        # Rest of your function...

    except Exception as e:
        print(f"Error generating release notes: {str(e)}")
        print("Environment variables:")
        for key, value in os.environ.items():
            print(f"{key}: {'*' * len(value)}")  # Print asterisks instead of actual value for security
        sys.exit(1)  # Exit with an error code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_release_notes.py <sprint_name>")
        sys.exit(1)
    
    sprint_name = sys.argv[1]
    generate_release_notes(sprint_name)
