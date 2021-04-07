from utils import quest_handler, launch

quest_body = quest_handler() # grouping data about google form using only a link

launch(quest_body) # start raid

# P.S link must consist /formResponse, with other link script can`t work correctly
# about 83 responses / minute (one Thread) -> 83 * Thread amount  r/m