import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

def format_date_column(data):
    existing_col = list(data);
    new_created_col = [];
    for i in existing_col:
        temp_list = str(i).split('.')
        temp_str = temp_list[0]
        new_created_col.append(temp_str)
    return new_created_col

def create_output_csv_file():
    print("Kindly enter the name of the file to be formatted")
    filename = str(input())

    try:
        # read the input csv file given by user in pandas dataframe format
        data = pd.read_csv(filename)
        data['created'] = format_date_column(data['created'])
        data['updated'] = format_date_column(data['updated'])
        print(data['updated'])

        # fetch required columns from the dataframe
        activity = data['summary'];
        resource = data['reporter'];
        caseConceptName = data['status.description']
        caseCreator = data['creator']
        conceptName = data['status.name']
        orgResource = data['assignee']
        time = data['updated']

        # declare an empty timeStamp list
        timeStamp = [];

        # for every date value in time column, convert the epoch date to human readable format and append it to timeStamp list
        for date in time:
            createdTime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
            timeStamp.append(str(createdTime));

        # convert the timeStamp list to pandas Series format
        timeStampSeries = pd.Series(timeStamp);

        # create the new data frane using all the series
        new_data_frame = pd.DataFrame(
            {'resource': resource, 'case:concept:name': caseConceptName, 'case:creator': caseCreator,
             'concept:name': conceptName, 'org:resource': orgResource, 'time:timestamp': timeStampSeries})

        # sort the generated dataframe according to time column in ascending order
        new_data_frame.sort_values(by='time:timestamp', inplace=True, ascending=False)

        new_data_frame.to_csv("output.csv", index=False)

        print("Formatted csv created with name: output.csv")
    except FileNotFoundError:
        print("Please check your file name")


