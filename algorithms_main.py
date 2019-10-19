from algorithm_utils import *

#function to save xes log to disk
#input: formatted csv file
def save_xes_log_disk():
    print("Enter the csv file name to convert to XES")
    filename = str(input())
    dataframe = generate_dataframe(filename)
    save_xes_to_disk(dataframe)

#function to apply alpha miner algorithm
def apply_alpha_net_algorithm():
    try:
        print("Enter your train file name")
        train_file = str(input())
        train_dataframe = generate_dataframe(train_file)
        train_xes_log = generate_xes_from_dataframe(train_dataframe)
        train_alpha_net = generate_alpha_net(train_xes_log)

        print("Enter your test file name")
        test_file = str(input())
        test_dataframe = generate_dataframe(test_file)
        test_xes_log = generate_xes_from_dataframe(test_dataframe)
        test_alpha_net = generate_alpha_net(test_xes_log)

        print("**********Train - Alpha Algo Results\n"
            "train_alpha_net: " + str(train_alpha_net.get('alpha_net')) + "\n"
                                                                            "train_initial_marking: " + str(
            train_alpha_net.get('initial_marking')) + "\n"
                                                    "train_final_marking: " + str(train_alpha_net.get('final_marking')))

        print("**********Test - Alpha Algo Results\n"
            "test_alpha_net: " + str(test_alpha_net.get('alpha_net')) + "\n"
                                                                        "test_initial_marking: " + str(
            test_alpha_net.get('initial_marking')) + "\n"
                                                    "test_final_marking: " + str(test_alpha_net.get('final_marking')))
    except Error:
        print("Please enter valid file name")

# function to apply inductive miner algorithm
def apply_inductive_miner_algorithm():
    try:
        print("Enter your train file name")
        train_file = str(input())
        train_dataframe = generate_dataframe(train_file)
        train_xes_log = generate_xes_from_dataframe(train_dataframe)
        train_inductive_net = generate_inductive_miner_net(train_xes_log)

        print("Enter your test file name")
        test_file = str(input())
        test_dataframe = generate_dataframe(test_file)
        test_xes_log = generate_xes_from_dataframe(test_dataframe)
        test_inductive_net = generate_inductive_miner_net(test_xes_log)

        print("**********Train - Inductive Algo Results\n"
          "train_inductive_net: " + str(train_inductive_net.get('inductive_net')) + "\n"
                                                                        "train_initial_marking: " + str(
        train_inductive_net.get('initial_marking')) + "\n"
                                                  "train_final_marking: " + str(train_inductive_net.get('final_marking')))

        print("**********Test - Inductive Algo Results\n"
          "test_inductive_net: " + str(test_inductive_net.get('inductive_net')) + "\n"
                                                                      "test_initial_marking: " + str(
        test_inductive_net.get('initial_marking')) + "\n"
                                                 "test_final_marking: " + str(test_inductive_net.get('final_marking')))
    except Error:
        print("Please enter valid file name")


# function to display and save petri net using the simple analysis option in main menu
def display_petri_net_simple():
    try:
        print("Enter your file name")
        temp = input()
        file = str(temp)
        dataframe = generate_dataframe(file)
        xes_log = generate_xes_from_dataframe(dataframe)

        details = generate_inductive_miner_net(xes_log)
        generate_petri_net_visual(details.get('inductive_net'), details.get('initial_marking'),
                                  details.get('final_marking'),xes_log)
    except TypeError:
        print("Please enter valid file name")

def display_petri_net():
    try:
        print("Enter your file name")
        file = str(input())
        dataframe = generate_dataframe(file)
        xes_log = generate_xes_from_dataframe(dataframe)

        print('Enter algorithm to apply\n'
              '1. Alpha \n'
              '2. Inductive Miner\n'
              '3. Simple\n'
              '4. Heuristics Miner')
        algo_option = input()
        if algo_option == '1':
            details = generate_alpha_net(xes_log)
            generate_petri_net_visual(details.get('alpha_net'), details.get('initial_marking'),
                                      details.get('final_marking'), xes_log)
        elif algo_option == '2':
            details = generate_inductive_miner_net(xes_log)
            generate_petri_net_visual(details.get('inductive_net'), details.get('initial_marking'),
                                    details.get('final_marking'),xes_log)
        elif algo_option == '3':
            details = generate_simple_net(xes_log)
            generate_petri_net_visual(details.get('simple_net'), details.get('initial_marking'),
                                    details.get('final_marking'), xes_log)
        elif algo_option == '4':
            details = generate_heuristics_petri_net(xes_log)
            generate_petri_net_visual(details.get('heu_net'), details.get('initial_marking'),
                                    details.get('final_marking'), xes_log)
        else:
            print("Selected option invalid")
    except TypeError:
        print("Please enter valid file name")


def display_replay_log_fitness():
    try:
        print("Enter your train file name")
        train_file = str(input())

        print("Enter test file name")
        test_file = str(input())
        test_dataframe = generate_dataframe(test_file)
        train_dataframe = generate_dataframe(train_file)

        xes_test_log = generate_xes_from_dataframe(test_dataframe)
        xes_train_log = generate_xes_from_dataframe(train_dataframe)

        print("Select algorithm to apply to net\n"
              "1. Alpha \n"
              "2. Inductive Miner\n"
              "3. Simple\n")
        algo_option = input()
        if algo_option == '1':
            details = generate_alpha_net(xes_train_log)
            generate_replay_result(xes_test_log, details.get('alpha_net'), details.get('initial_marking'),
                                   details.get('final_marking'))
        elif algo_option == '2':
            details = generate_inductive_miner_net(xes_train_log)
            generate_replay_result(xes_test_log, details.get('inductive_net'), details.get('initial_marking'),
                                   details.get('final_marking'))
        elif algo_option == '3':
            details = generate_simple_net(xes_train_log)
            generate_replay_result(xes_test_log, details.get('simple_net'), details.get('initial_marking'),
                                   details.get('final_marking'))
        else:
            print("Selected option invalid")
    except TypeError:
        print("Please enter valid file name")

###########################################Social Network Analysis#############################################
def work_handover():
    try:
        print("Kindly enter the name of your formatted file\n"
          "Note: please include .csv file extension and make sure that input file has no blank rows or columns")
        filename = str(input())
        dataframe = csv_import_adapter.import_dataframe_from_path(filename, sep=",")
        from pm4py.objects.conversion.log import factory as conversion_factory  # lib to convert csv to xes
        log = conversion_factory.apply(dataframe)
        from pm4py.algo.enhancement.sna import factory as sna_factory
        hw_values = sna_factory.apply(log, variant="handover")
        from pm4py.visualization.sna import factory as sna_vis_factory
        gviz_hw_py = sna_vis_factory.apply(hw_values, variant="pyvis")
        sna_vis_factory.view(gviz_hw_py, variant="pyvis")
    except FileNotFoundError:
        print("Please check your file name")

def subcontracting_metric():
    print("Kindly enter the name of your formatted file\n"
          "Note: please include .csv file extension and make sure that input file has no blank rows or columns")
    filename = str(input())

    try:
        dataframe = csv_import_adapter.import_dataframe_from_path(filename, sep=",")
        from pm4py.objects.conversion.log import factory as conversion_factory  # lib to convert csv to xes
        log = conversion_factory.apply(dataframe)

        from pm4py.algo.enhancement.sna import factory as sna_factory
        sub_values = sna_factory.apply(log, variant="subcontracting")
        from pm4py.visualization.sna import factory as sna_vis_factory
        gviz_sub_py = sna_vis_factory.apply(sub_values, variant="pyvis")
        sna_vis_factory.view(gviz_sub_py, variant="pyvis")
    except FileNotFoundError:
        print("Please check your file name")


def working_together_metric():
    print("Kindly enter the name of your formatted file\n"
          "Note: please include .csv file extension and make sure that input file has no blank rows or columns")
    filename = str(input())

    try:
        dataframe = csv_import_adapter.import_dataframe_from_path(filename, sep=",")
        from pm4py.objects.conversion.log import factory as conversion_factory  # lib to convert csv to xes
        log = conversion_factory.apply(dataframe)

        from pm4py.algo.enhancement.sna import factory as sna_factory
        wt_values = sna_factory.apply(log, variant="working_together")
        from pm4py.visualization.sna import factory as sna_vis_factory
        gviz_sub_py = sna_vis_factory.apply(wt_values, variant="pyvis")
        sna_vis_factory.view(gviz_sub_py, variant="pyvis")
    except FileNotFoundError:
        print("Please check your file name")

def similar_activities_metric():
    print("Kindly enter the name of your formatted file\n"
          "Note: please include .csv file extension and make sure that input file has no blank rows or columns")
    filename = str(input())

    try:
        dataframe = csv_import_adapter.import_dataframe_from_path(filename, sep=",")
        from pm4py.objects.conversion.log import factory as conversion_factory  # lib to convert csv to xes
        log = conversion_factory.apply(dataframe)

        from pm4py.algo.enhancement.sna import factory as sna_factory
        ja_values = sna_factory.apply(log, variant="jointactivities")
        from pm4py.visualization.sna import factory as sna_vis_factory
        gviz_ja_py = sna_vis_factory.apply(ja_values, variant="pyvis")
        sna_vis_factory.view(gviz_ja_py, variant="pyvis")
    except FileNotFoundError:
        print("Please check your file name")