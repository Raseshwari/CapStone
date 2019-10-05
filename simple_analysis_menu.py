from algorithms_main import *
from format_input_file import create_output_csv_file

# display the Simple Analysis option's sub-menu
def simple_analysis_functions():
    while True:
        print("**********Simple Analysis Sub-Menu***********\n"
        "1. Create input file\n"
        "2. View and Save Petri Net\n"
        "3. Return back to Main Menu\n"
        "4. Exit\n");

        selected_option = input()
        if selected_option == '3':
            break
        if selected_option == '4':
            exit()
        simple_analysis_menu(selected_option)

def simple_analysis_menu(selected_option):
    if selected_option == '1':
        create_output_csv_file()
    elif selected_option == '2':
        display_petri_net_simple()
    else:
        print("Invalid choice")
    
