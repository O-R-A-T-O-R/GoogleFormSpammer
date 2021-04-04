from utils import holes_checker, quest_handler, launch

holes_checker() # check titles and if it`s necessary update json (config.json)

quest_body = quest_handler() # grouping data about google form using only a link

launch(quest_body) # start raid

# P.S link must consist /formResponse, with other link script can`t work correctly
# about 83 responses / minute (one Thread) -> 83 * Thread amount  r/m