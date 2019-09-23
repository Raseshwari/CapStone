from jira import JIRA
import pandas as pd
from format_input_file import create_output_csv_file

def py_jira_menu(selected_option):
    if selected_option == '1':
        view_all_jira_projects()
    elif selected_option == '2':
        generate_csv_from_jira()
    elif selected_option == '3':
        create_output_csv_file()
    elif selected_option == '5':
        exit()

def py_jira_functions():
    while True:
        print("***********JIRA Sub-Menu**************\n"
              "1. View all JIRA projects\n"
              "2. Generate csv file of JIRA project\n"
              "3. Format generated JIRA csv\n"
              "4. Return to the previous menu\n"
              "5. Exit")
        selected_option = input()
        if selected_option == '4':
            break
        py_jira_menu(selected_option)


def connect_to_jira_server(jira_url):
    # server name to connect to
    options = {
        'server': jira_url
    }
    jira = JIRA(options)
    return jira

def view_all_jira_projects():
    try:
        print("Kindly enter the jira server URL, eg: https://jira.spring.io\n")
        jira_url = str(input())

        jira_server = connect_to_jira_server(jira_url)

        # get list of all the projects on that jira server
        projects = jira_server.projects()
        print(projects)
    except Exception:
        print("Please enter a valid URL")

def generate_csv_from_jira():
    print("Kindly enter the jira server URL, eg: https://jira.spring.io")
    try:
        jira_url = str(input())
        jira_server = connect_to_jira_server(jira_url)

        print("Please specify the project (key) to scrape: ")
        try:
            project_name = str(input())

            # give project key and start and end row values
            issues_in_proj = jira_server.search_issues('project='+project_name, 0, 1000)
            print(type(issues_in_proj))

            # initialize an empty dataframe
            issues = pd.DataFrame()

            # create dictionary of all the issues in the project
            for issue in issues_in_proj:
                d = {'key': issue.key,
                     'assignee': issue.fields.assignee,
                     'creator': issue.fields.creator,
                     'reporter': issue.fields.reporter,
                     'created': issue.fields.created,
                     'components': issue.fields.components,
                     'description': issue.fields.description,
                     'summary': issue.fields.summary,
                     'fixVersions': issue.fields.fixVersions,
                     'subtask': issue.fields.issuetype.subtask,
                     'issuetype': issue.fields.issuetype.name,
                     'resolution': issue.fields.resolution,
                     'resolution.date': issue.fields.resolutiondate,
                     'status.name': issue.fields.status.name,
                     'status.description': issue.fields.status.description,
                     'updated': issue.fields.updated,
                     'versions': issue.fields.versions,
                     'watches': issue.fields.watches.watchCount,
                     }
                print(d)
                issues = issues.append(d, ignore_index=True)
                # write issue dictionary to csv file
                issues.to_csv("issues-" + project_name + ".csv", encoding='utf-8', header=True, index=False)

                print("name of generated csv file: issues-" + project_name + ".csv")
        except Exception:
            print("Project name (key) is invalid")
    except Exception:
        print("Enter valid URL")

