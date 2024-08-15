import os
import json
from jira import JIRA
import sys
from requests.exceptions import RequestException

def generate_release_notes(sprint_name):
    try:
        print("Starting generate_release_notes function")
        
        jira_token = os.environ.get('JIRA_API_TOKEN')
        jira_domain = os.environ.get('JIRA_DOMAIN')
        jira_email = os.environ.get('JIRA_EMAIL')  # Add this line

        print(f"JIRA_API_TOKEN exists: {bool(jira_token)}")
        print(f"JIRA_DOMAIN exists: {bool(jira_domain)}")
        print(f"JIRA_EMAIL exists: {bool(jira_email)}")  # Add this line

        if not jira_token or not jira_domain or not jira_email:  # Modified this line
            raise ValueError("JIRA_API_TOKEN, JIRA_DOMAIN, or JIRA_EMAIL environment variables are not set")

        jira_url = f"https://{jira_domain}"
        print(f"Connecting to Jira URL: {jira_url}")
        
        # Modified authentication method
        jira = JIRA(server=jira_url, basic_auth=(jira_email, jira_token))
        
        print("Testing connection...")
        jira.server_info()  # This will raise an exception if connection fails
        print("Successfully connected to Jira")
        
        print(f"Fetching tickets for sprint: {sprint_name}")
        
        # Rest of your function...

    except RequestException as e:
        print(f"Error connecting to Jira: {str(e)}")
        print(f"Response status code: {e.response.status_code}")
        print(f"Response headers: {e.response.headers}")
        print(f"Response text: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"Error generating release notes: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_release_notes.py <sprint_name>")
        sys.exit(1)
    
    sprint_name = sys.argv[1]
    generate_release_notes(sprint_name)
