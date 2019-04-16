from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/foodnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-599302602865-594203559474-609169059527-db393bce86f200034dac8957f65af700', #app verification token
							'xoxb-599302602865-599320895393-SDG7jVIUslGVqL5SQeXToNTa', # bot verification token
							'mzTduztYUuilNqflxzfNMBNy', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5002, '/', input_channel))