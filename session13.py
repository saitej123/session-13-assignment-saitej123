import sys
import random
from datetime import datetime
from collections import namedtuple, Counter
import csv
import re
import math
from tabulate import tabulate

# Traffic violation records NamedTuple
records = namedtuple('records', ['Summons_Number', 'Plate_Id', 'Registration_State', 'Plate_Type',
                     'Issue_Date', 'Violation_Code', 'Vehicle_Body_Type', 'Vehicle_Make', 'Violation_Description'])


# Goal 1
def records_generator(file_name):
    '''
    Generator for traffic violations named tuple
    '''

    with open(file_name) as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        next(data)
        for row in data:
            summons_number = int(row[0])
            plate_id = row[1]
            # Registration_State '99', '999' are invalid so replaced with blank
            if row[2] == '99':
                registration_state = ''
            else:
                registration_state = row[2]

            if row[3] == '999':
                plate_type = ''
            else:
                plate_type = row[3]

            if '/' in row[4]:
                issue_date = datetime.strptime(row[4].strip(), '%m/%d/%Y')
            elif '-' in row[4]:
                issue_date = datetime.strptime(row[4].strip(), '%m-%d-%Y')

            violation_code = int(row[5])
            vehicle_body_type = row[6]
            vehicle_make = row[7]
            violation_description = row[8]
            yield records(summons_number, plate_id, registration_state, plate_type, issue_date, violation_code, vehicle_body_type, vehicle_make, violation_description)


def fetch_records(file_name):
    '''
    returns list of NamedTuple for traffic violations
    '''
    return [record for record in records_generator(file_name)]


# Goal 2

def vehicle_make_information(records):
    ''' 
    Generator for Vehicle Make from given records
    '''
    for record in records:
        yield record.Vehicle_Make
        
        
def vehicle_make_violations(records):
    '''
    Generator for traffic violations by Vehicle Make
    '''
    vehicle_make_list = [
        vehicle_make for vehicle_make in vehicle_make_information(records)]
    violation_by_vehicle_make = Counter(vehicle_make_list)
    for make, violations in violation_by_vehicle_make.most_common():
        yield [make, violations]
        

def show_violations(records):
    '''
    Prints Vehicle Make and Traffic Violations in tabular format
    '''
    print(tabulate(list(vehicle_make_violations(records)), headers=["Make", "Violation"]))
        

