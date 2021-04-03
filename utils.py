import json, sys, requests, random
import os.path
from bs4 import BeautifulSoup

from LogPython import LogManager
from constants import default_config, config_name, answers_save_name, headers

def get_config_titles(filename : str) -> dict:
    config_content = str()
    
    with open(filename, "r", encoding = "utf-8") as config:
        for row in config.readlines():
            config_content += row

    try:
        return json.loads(config_content)
    except:
        return None

config_titles = get_config_titles(config_name)

def holes_checker():
    try:
        for elem in config_titles:
            if not config_titles[elem] and elem != "SHORT" and elem != "LONG":
                LogManager.error("Not all required data exists [config.json]")
                sys.exit(0)
                
    except TypeError:
        with open(config_name, "w", encoding = "utf-8") as place:
            json.dump(default_config, place, ensure_ascii = False, indent = 4)

            LogManager.error("Config file is empty or unable to work correctly")
            LogManager.warning("Forced update config.json [to default settings]")

            sys.exit(0)

holes_checker() # check titles and if it`s necessary update json (config.json)

link = config_titles['LINK']
amount = int(config_titles['AMOUNT'])

DATA = requests.get(link).text

def answers_filler(container : list):
    for elem in container: 
        if elem['value'] == "LongAnswer":
            elem['value'] = input(elem['quest'] + ": ")

def quest_handler() -> list:
    """

    :return: questions of google form, variouses of choice, etc.

    """

    answers = list()

    body = DATA[DATA.find("var FB_PUBLIC_LOAD_DATA_ "):]
    body = body[:body.find(',"/forms"')].lstrip("var FB_PUBLIC_LOAD_DATA_ = ").replace("null", "0") + "]"
    body = json.loads(body)

    for element in body[1][1]:
        temp = list()
    
        try:
            for elem in element[4][0][1]:
                temp.append(elem[0])    
        except : pass

        try:
            answers.append({
                'quest' : element[1],
                'id' : str(element[4][0][0]),
                'value' : temp
            })
        except : pass

    additional_inputs = list()

    for elem in answers:
        if not elem['value']:
            elem['value'] = "LongAnswer"
        else:
            additional_inputs.append({
                'id' : elem['id'] + "_sentinel",
                'value' : ""
            })

    for elem in additional_inputs:
        answers.append(elem)

    save_exists = False

    if os.path.exists(answers_save_name):

        while True:
            backup_access = input("Want you use a backup and fill answers faster? [Y/N] : ")

            if backup_access.upper() == "Y":
                save_exists = True
                
                with open(answers_save_name, "r", encoding = "utf-8") as backup:
                    backup_content = str()

                    for row in backup.readlines():
                        backup_content += row

                    answers = json.loads(backup_content)

                    break

            elif backup_access.upper() == "N":
                break

    if not save_exists:
        answers_filler(answers)

        while True:
            save_access = input("Want you save this answers to use later? [Y/N] : ")

            if save_access.upper() == "Y":
                with open(answers_save_name, "w", encoding = "utf-8") as backup:
                    json.dump(answers, backup, ensure_ascii = False, indent = 4)

                    LogManager.info("Success writing [answers_save.json]")
                    break

            elif save_access.upper() == "N":
                break

    for elem in answers:
        elem['id'] = "entry." + elem['id']

    return answers

def requested_data(container : list) -> dict:
    requested = dict()
    
    for elem in container:
        if elem['value'] is list:
            requested[elem['id']] = random.choice(elem['value'])
        else:
            requested[elem['id']] = elem['value']

    soup = BeautifulSoup(DATA, "lxml")

    fvv = soup.find("input", {
        "name" : "fvv"
    }).attrs['value']
               
    draftResponse = soup.find("input", {
        "name" :"draftResponse"
    }).attrs['value']
    
    pageHistory = soup.find("input", {
        "name" : "pageHistory"
    }).attrs['value']
    
    fbzx = soup.find("input", {
        "name" : "fbzx"
    }).attrs['value']

    requested['fvv'] = fvv
    requested['draftResponse'] = draftResponse
    requested['pageHistory'] = pageHistory
    requested['fbzx'] = fbzx

    return requested

def launcher(data_container : dict, thread_number : int):

    for i in range(amount):
        raid_data = requested_data(data_container) 

        r = requests.post(link,
                          data = raid_data,
                          headers = headers,
                          proxies = None)

        LogManager.info(f"{r}///{thread_number + 1}///{i + 1}".rjust(35, "<"))