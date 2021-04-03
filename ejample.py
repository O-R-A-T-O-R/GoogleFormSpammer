# ------- ejample of single-threaded raid -------

from utils import holes_checker, quest_handler, launcher

holes_checker() # check titles and if it`s necessary update json (config.json)

quest_body = quest_handler() # grouping data about google form using only a link

launcher(quest_body, 1) # start raid to google form using quest_body (data about questions) and created with it response_data (answers on questions)

# ------- ejample of multi-threaded raid -------

import threading

thread_amount = 15 # quantity of threads you want to start

_ = list()

for i in range(thread_amount):
    thr = threading.Thread(target = launcher, args = (quest_body, i), daemon = True) # create raid Thread

    thr.start() # start daemon raid Thread
    _.append(thr)

[t.join() for t in _]

# GoogleFormSpammer.git
# Production by HidBell organization

# *Use python3 instead python, if you have not only Python3.*

# *$ python main.py --help* <-------- to get help table

# Instruction to start raiding:

# *$ python main.py --link set* <------- set raid link
# *$ python main.py --link get* <------- show raid link
# *$ python main.py --resp set_input* <- auto set all short questions in google_form
# *$ python main.py --resp get_unput* <- show all short questions and all choices of answer
# *$ python main.py --_input set* <----- set all long answers of questions

# Additional Instruction about *--_input set*:

# name ----------- to set random name
# surname -------- to set random surname
# fio ------------ to set random "surname name second_name"
# fi ------------- to set random "surname name"
# gen ------------ to set random gender word
# default -------- to set sentence with 100 random words