from __future__ import unicode_literals
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig # to load rasa configuration files
from rasa_nlu.model import Trainer #Trainer will do the training
from rasa_nlu.model import Metadata, Interpreter


def train_nlu(data,config,model_dir):
	training_data=load_data(data)
	trainer=Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory=trainer.persist(model_dir, fixed_model_name='foodnlu')
def run_nlu():
	interpreter=Interpreter.load('./models/nlu/default/foodnlu', RasaNLUConfig('config_spacy.json'))
	print(interpreter.parse(u"i would like to have a burger"))


train_nlu('./data/data.json','config_spacy.json','./models/nlu')

run_nlu()
 





