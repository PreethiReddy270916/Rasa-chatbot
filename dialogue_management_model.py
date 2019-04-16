from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter#to parse incoming messages and extract info

#logger = logging.getLogger(__name__)

def train_dialogue(domain_file='food_domain.yml',model_path='./models/dialogue',training_data_file='./data/stories.md'):
	agent=Agent(domain_file, policies= [MemoizationPolicy(),KerasPolicy()])
	agent.train(
		training_data_file,max_history=3,epochs=86,batch_size=10,validation_split=0.5,augmentation_factor=50)
	agent.persist(model_path)
	return agent

train_dialogue()



