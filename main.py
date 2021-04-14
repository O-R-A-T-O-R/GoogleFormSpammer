from utils import quest_handler, launch

quest_body = quest_handler() # grouping data about google form using only a link

launch(quest_body) # start raid

# about 83 responses / minute (one Thread) -> 83 * Thread amount  r/m