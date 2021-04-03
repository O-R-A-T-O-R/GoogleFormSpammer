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
