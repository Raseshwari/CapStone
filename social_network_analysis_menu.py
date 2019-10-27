from algorithms_main import *
from format_input_file import create_output_csv_file


def social_network_analysis_functions():
    while True:
        print("***********Algorithm Sub-Menu**************\n"
              "1. Work handover between team resources\n"
              "2. Subcontracting Metric (How many times is work of one individual interleaved by work of other individual)\n"
              "3. Working Together Metric (How many times two individuals work together for resolving an issue)\n"
              "4. Similar Activities Metric (How much similar is the work pattern between two individuals) \n"
              "5. Go back to main menu\n"
              "6. Exit")
        selected_option = input()
        if selected_option == '5':
            break
        if(selected_option) == '6':
            exit()
        social_network_analysis_menu(selected_option)


def social_network_analysis_menu(selected_option):
    if selected_option == '1':
        work_handover()
    elif selected_option == '2':
        subcontracting_metric()
    elif selected_option == '3':
        working_together_metric()
    elif selected_option == '4':
        similar_activities_metric()
    else:
        print("Invalid choice")
