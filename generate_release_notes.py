import os
import json
from jira import JIRA
import sys

def get_completed_tickets(jira, sprint_name):
    jql_query = f'project = YourProjectKey AND labels = {sprint_name} AND (status = Done OR status = Closed)'
    issues = jira.search_issues(jql_query)
    
    completed_tickets = []
    for issue in issues:
        ticket_info = {
            'key': issue.key,
            'summary': issue.fields.summary,
            'type': issue.fields.issuetype.name,
            'assignee': issue.fields.assignee.displayName if issue.fields.assignee else 'Unassigned'
        }
        completed_tickets.append(ticket_info)
    
    return completed_tickets

def generate_release_notes(sprint_name):
    try:
        jira_token = os.environ.get('JIRA_API_TOKEN')
        jira_domain = os.environ.get('JIRA_DOMAIN')

        if not jira_token or not jira_domain:
            raise ValueError("JIRA_API_TOKEN or JIRA_DOMAIN environment variables are not set")

        print(f"Connecting to Jira domain: {jira_domain}")
        jira = JIRA(server=f"https://{jira_domain}", token_auth=jira_token)
        
        print(f"Fetching tickets for sprint: {sprint_name}")
        tickets = get_completed_tickets(jira, sprint_name)
        
        release_notes = {
            "sprint_name": sprint_name,
            "tickets": tickets
        }
        
        with open('release_notes.json', 'w') as f:
            json.dump(release_notes, f, indent=2)
        
        print(f"Release notes generated and saved to release_notes.json")
    except Exception as e:
        print(f"Error generating release notes: {str(e)}")
        sys.exit(1)  # Exit with an error code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_release_notes.py <sprint_name>")
        sys.exit(1)
    
    sprint_name = sys.argv[1]
    generate_release_notes(sprint_name)
