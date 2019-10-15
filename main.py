from py_jira import py_jira_functions
from simple_analysis_menu import simple_analysis_functions
from detailed_analysis_menu import detailed_analysis_functions

# main menu to display the 4 core functionalities
def menu(selected_option):
    if selected_option == '1':
        py_jira_functions()
    if selected_option == '2':
        simple_analysis_functions()
    if selected_option == '3':
        detailed_analysis_functions()
    elif selected_option == '5':
        exit()
    else:
        print('Please enter a valid option')

def main():
    while True:
        print("****************Welcome to Process Engg Tool**********************\n")
        print("Please select the operation you would like to perform\n")
        print("*********Main Menu**************\n"
              "1. JIRA operations\n"
              "2. Simple Analysis\n"
              "3: Detailed Analysis (Option to choose algorithm)\n"
              "4. Social Network Analysis\n"
              "5. Exit")
        selected_option = input()
        if selected_option == '4':
            break
        menu(selected_option)

if __name__ == "__main__":
    main()