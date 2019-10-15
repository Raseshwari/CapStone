from pm4py.algo.conformance.tokenreplay import factory as token_replay #lib to perform token_replay and verify conformance
from pm4py.evaluation.replay_fitness import factory as replay_fitness_factory #lib to evaluate the log and trace fitness
from pm4py.objects.log.adapters.pandas import csv_import_adapter #lib to import csv file
from pm4py.objects.conversion.log import factory as conversion_factory #lib to convert csv to xes
from pm4py.objects.log.exporter.xes import factory as xes_exporter #lib to export the converted xes log
from pm4py.algo.discovery.alpha import factory as alpha_miner #lib to run alpha_miner on the xes log
from pm4py.visualization.petrinet import factory as pn_vis_factory #lib to visualize the process diagram generated from petrinets
from pm4py.algo.discovery.simple.model.log import factory as simple_algorithm #lib to run simple algorithm
from pm4py.algo.conformance.tokenreplay import factory as token_replay #lib to perform token_replay and verify conformance
from pm4py.evaluation.replay_fitness import factory as replay_fitness_factory #lib to evaluate the log and trace fitness
from pm4py.objects.petri.check_soundness import check_wfnet
from pm4py.objects.petri.check_soundness import check_petri_wfnet_and_soundness
from pm4py.objects.petri import utils
from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.algo.discovery.heuristics import factory as heuristics_miner
from pm4py.visualization.heuristics_net import factory as hn_vis_factory
from pm4py.algo.discovery.heuristics import factory as heuristics_miner
import pandas as pd

# function to generate dataframe from input csv file
def generate_dataframe(filename):
    try:
        # import csv into pandas dataframe by specifying the sep - seperator
        dataframe = csv_import_adapter.import_dataframe_from_path(filename, sep=",")
        return dataframe
    except FileNotFoundError:
        print("Invalid file name")
        exit()

# function to generate xes file from dataframe
def generate_xes_from_dataframe(dataframe):
    try:
        # convert the csv imported in dataframe to xes log
        xes_log = conversion_factory.apply(dataframe)
        return xes_log
    except Error:
        print("Invalid input")

def generate_alpha_net(xes_log):
    try:
        alpha_net, initial_marking, final_marking = alpha_miner.apply(xes_log)
        return {'alpha_net' : alpha_net,
                'initial_marking': initial_marking,
                'final_marking': final_marking}
    except AttributeError:
        print("Please check input values")

# function to generate inductive net, initial and final marking using inductive miner algorithm
def generate_inductive_miner_net(xes_log):
    try:
        inductive_net, initial_marking, final_marking = inductive_miner.apply(xes_log)
        return {'inductive_net': inductive_net,
            'initial_marking': initial_marking,
            'final_marking' : final_marking}
    except AttributeError:
        print("Please check input values")

def generate_simple_net(xes_log):
    try:
        simple_net, initial_marking, final_marking = simple_algorithm.apply(xes_log, classic_output=True,parameters={"max_no_variants": 20})
        return {'simple_net': simple_net,
                'initial_marking': initial_marking,
                'final_marking': final_marking}
    except AttributeError:
        print("Please check your input values")

def generate_heuristics_miner_net(xes_log):
    try:
        heu_net = heuristics_miner.apply_heu(xes_log)
        gviz = hn_vis_factory.apply(heu_net)
        hn_vis_factory.view(gviz)
        return {'heu_net': heu_net}
    except AttributeError:
        print("Please check your input values")

def generate_heuristics_petri_net(xes_log):
    try:
        heu_net, im, fm = heuristics_miner.apply(xes_log)
        return {'heu_net': heu_net,
            'initial_marking': im,
            'final_marking': fm}
    except AttributeError:
        print("Please check your input values")

def save_xes_to_disk(dataframe):
    xes_log = generate_xes_from_dataframe(dataframe)
    # export xes log file
    xes_exporter.export_log(xes_log, "exportedLog.xes")
    print("exported XES log file: exportedLog.xes")

# function to generate petri net from the input params - net, initial, final marking and xes log
def generate_petri_net_visual(net, initial_marking, final_marking, xes_log):
    try:
        # visualizing the petri net using graphviz library, by passing net initial and final marking and viewing it
        parameters = {"format": "png"}
        gviz = pn_vis_factory.apply(net, initial_marking, final_marking,
                                parameters=parameters, variant="frequency", log=xes_log)
        pn_vis_factory.view(gviz)
        print("By what name do you want to save the petri net image?")
        filename = str(input())
        pn_vis_factory.save(gviz, filename+".png")
    except TypeError:
        print("Please check input values")

def generate_replay_result(xes_test_log, petri_net_train, initial_marking, final_marking):
    try:
        # apply token replay to the net, initial and final marking
        replay_result = token_replay.apply(xes_test_log, petri_net_train, initial_marking, final_marking)
        print("replay result: "+ str(replay_result) +"\n")

        # verify log fitness
        log_fitness = replay_fitness_factory.evaluate(replay_result, variant="token_replay")
        print("log_fitness"+str(log_fitness)+"\n")
    except TypeError:
        print("Please check input values")