import xml.etree.ElementTree as ET
from datetime import datetime
import os

def get_logpath():
    return checkReportFolder()

def checkReportFolder():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, datetime.now().strftime('YouTube_Automation_Report_%H_%M_%d_%m_%Y'))
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    return final_directory

def parseCapabilities():

    tree = ET.parse('mobileConfig.xml')
    root = tree.getroot()
    cap = []
    for element in root:
        for child in element:
            cap.append(child.text)
    return cap

def parsetestsuits():
    tree = ET.parse('testsuitconfig.xml')
    root = tree.getroot()
    cap = []
    for element in root:
        for child in element:
            cap.append(child.text)
    return cap
