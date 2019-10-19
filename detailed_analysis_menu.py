from algorithms_main import *
from format_input_file import create_output_csv_file


def detailed_analysis_functions():
    while True:
        print("***********Algorithm Sub-Menu**************\n"
              "1. Save XES log to local disk\n"
              "2. View Petri Net\n"
              "3. View replay result and log fitness score\n"
              "4. Go back to main menu\n"
              "5. Exit")
        selected_option = input()
        if selected_option == '4':
            break
        if(selected_option) == '5':
            exit()
        detailed_analysis_menu(selected_option)


def detailed_analysis_menu(selected_option):
    print(selected_option)
    if selected_option == '1':
        save_xes_log_disk()
    elif selected_option == '2':
        display_petri_net()
    elif selected_option == '3':
        display_replay_log_fitness()
    else:
        print("Invalid choice")
