#creates model/dialogue file useful for online training

from __future__ import absolute_import 
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent # used to train the model
from rasa_core.policies.keras_policy import KerasPolicy # models itself to be used to train the model
from rasa_core.policies.memoization import MemoizationPolicy # models itself to be used yo train the model

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	
	training_data_file = './data/stories.md'
	model_path = './models/dialogue'
	
	agent = Agent('food_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])#keras policy is a lstm so we can add parameters if we want or remove layers. rasa has already kept some defaults
	
	agent.train(
			training_data_file, #stories data
			augmentation_factor = 50, # rasa creates fake stories from the stories we have given and we specify how many should be created
			max_history = 2,# number of states our data file should remember
			epochs = 7,
			batch_size = 5,
			validation_split = 0.2)# % of how much should be used to test the model
agent.persist(model_path)
