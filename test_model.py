from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import numpy as np

def food_bot(serve_forever=True):
	interpreter =RasaNLUInterpreter('./models/nlu/default/foodnlu')
	agent=Agent.load('./models/dialogue', interpreter=interpreter)
    if serve_forever:#for the console to be running indefinitely 
		agent.handle_channel(ConsoleInputChannel())
	return agent

food_bot()
