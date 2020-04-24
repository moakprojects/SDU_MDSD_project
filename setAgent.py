import os
import dialogflow_v2 as dialogflow
			
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dial-py.service.json'

client = dialogflow.AgentsClient()

agent = dialogflow.types.Agent(
	parent='projects/dialogflow-python',
	display_name='HotelReservation',
	default_language_code='en',
	time_zone='Europe/Copenhagen'
)

response = client.set_agent(agent=agent)

client = dialogflow.IntentsClient()
parent = client.project_agent_path('dialogflow-python')

training_phrases_parts = ['My name is Akos', 'I'm Peter']
message_texts = ['Thank you!']

parameters = 

training_phrases = []
for training_phrases_part in training_phrases_parts:
	part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part)
	training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
	training_phrases.append(training_phrase)
	
text = dialogflow.types.Intent.Message.Text(text=message_texts)
message = dialogflow.types.Intent.Message(text=text)

intent = dialogflow.types.Intent(
        display_name='NameRecognition',
        training_phrases=training_phrases,
        messages=[message])
        
response = client.create_intent(parent, intent)
client = dialogflow.IntentsClient()
parent = client.project_agent_path('dialogflow-python')

training_phrases_parts = ['at 6 o'clock pm', 'from 8:00', 'at noon']
message_texts = ['We've set it']

parameters = 

training_phrases = []
for training_phrases_part in training_phrases_parts:
	part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part)
	training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
	training_phrases.append(training_phrase)
	
text = dialogflow.types.Intent.Message.Text(text=message_texts)
message = dialogflow.types.Intent.Message(text=text)

intent = dialogflow.types.Intent(
        display_name='TimeRecognition',
        training_phrases=training_phrases,
        messages=[message])
        
response = client.create_intent(parent, intent)

