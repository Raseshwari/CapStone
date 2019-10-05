from algorithm_utils import *

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