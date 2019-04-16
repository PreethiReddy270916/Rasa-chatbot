# custom actions that the bot needs for rendering relevant responses
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import random
import requests
import json


class ActionOrderFood(Action):
	def name(self):
		return 'action_order_food'

	def run(self, dispatcher, tracker, domain):
		food = tracker.get_slot('food_item')
		TokenNumber=random.randint(10001,90001)
		#price=50# could be retrieved from a db later
		response = """Your food is ordered for you.\n Item_name: {}.\n \n Token number: {}""".format(food, TokenNumber)
		dispatcher.utter_message(response)
		return [SlotSet('food_item',food)]

class ActionShowFood(Action):
	def name(self):
		return 'action_show_food'

	def run(self,dispatcher, tracker, domain):
		url='http://www.mocky.io/v2/5cb0d8af3300004900571f04'
		json_data=requests.get(url).json()
		#print(json_data)
		i=0
		while(i<9):
			json_res=json_data[i]
			item_name=json_res.get("name","")
			item_cost=json_res.get("cost","")
			response="""{}           \t {} """.format(item_name,item_cost)
			dispatcher.utter_message(response)
			i=i+1
        

