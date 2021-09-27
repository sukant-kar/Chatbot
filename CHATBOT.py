python -m chatterbot --version
pip install chatterbot --upgrade
pip install chatterbot
from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer
conversation = [
"Hello",
"Hi there!",
"How are you doing?",
"I'm doing great.",
"That is good to hear",
"Thank you.",
"You're welcome."
]
trainer = ListTrainer(chatbot)
trainer.train(conversation)
response = chatbot.get_response("Good morning!")
print(response)
pip install chatterbot
from chatterbot import ChatBot
bot = ChatBot('Norman')
bot = ChatBot(
'Norman',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3'
)
bot = ChatBot(
'Norman',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
'chatterbot.logic.MathematicalEvaluation',
'chatterbot.logic.TimeLogicAdapter'
],
database_uri='sqlite:///database.sqlite3'
)
while True:
try:
bot_input = bot.get_response(input())
print(bot_input)
except(KeyboardInterrupt, EOFError, SystemExit):
breakfrom chatterbot.trainers import ListTrainer
trainer = ListTrainer(bot)
trainer.train([
'How are you?',
'I am good.',
'That is good to hear.',
'Thank you',
'You are welcome.',
])from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')
trainer = ListTrainer(chatbot)trainer.train([
"Hi, can I help you?",
"Sure, I'd like to book a flight to Iceland.",
"Your flight has been booked."
])
# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')
print(response)from chatterbot import ChatBot
# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)
# Create a new instance of a ChatBot
bot = ChatBot(
'Terminal',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
'chatterbot.logic.MathematicalEvaluation',
'chatterbot.logic.TimeLogicAdapter',
'chatterbot.logic.BestMatch'
],
database_uri='sqlite:///database.sqlite3'
)
print('Type something to begin...')
# The following loop will execute each time the user enters input
while True:
try:
user_input = input()
bot_response = bot.get_response(user_input)
print(bot_response)
# Press ctrl-c or ctrl-d on the keyboard to exit
except (KeyboardInterrupt, EOFError, SystemExit):
break
storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
from chatterbot import ChatBot
# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)
# Create a new ChatBot instance
bot = ChatBot(
'Terminal',
storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
logic_adapters=[
'chatterbot.logic.BestMatch'
],
database_uri='mongodb://localhost:27017/chatterbot-database'
)
print('Type something to begin...')
while True:
try:
user_input = input()
bot_response = bot.get_response(user_input)
print(bot_response)
# Press ctrl-c or ctrl-d on the keyboard to exit
except (KeyboardInterrupt, EOFError, SystemExit):
breakfrom chatterbot import ChatBot
bot = ChatBot(
'Math & Time Bot',
logic_adapters=[
'chatterbot.logic.MathematicalEvaluation',
'chatterbot.logic.TimeLogicAdapter'
]
)
# Print an example of getting one math based response
response = bot.get_response('What is 4 + 9?')
print(response)
# Print an example of getting one time based response
response = bot.get_response('What time is it?')
print(response)from chatterbot import ChatBot
# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)
# Create a new instance of a ChatBot
bot = ChatBot(
'SQLMemoryTerminal',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri=None,
logic_adapters=[
'chatterbot.logic.MathematicalEvaluation',
'chatterbot.logic.TimeLogicAdapter',
'chatterbot.logic.BestMatch'
]
)
# Get a few responses from the bot
bot.get_response('What time is it?')
bot.get_response('What is 7 plus 7?')chatbot = ChatBot("Johnny Five", read_only=True)
chatbot = ChatBot('Training Example')
from chatbot import chatbot
from chatterbot.trainers import ListTrainer
trainer = ListTrainer(chatbot)
trainer.train([
"Hi there!",
"Hello",
])
trainer.train([
"Greetings!",
"Hello",
])trainer.train([
"How are you?",
"I am good.",
"That is good to hear.",
"Thank you",
"You are welcome.",
])chatbot = ChatBot('Training Example')
from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
"chatterbot.corpus.english"
)trainer.train(
"chatterbot.corpus.english.greetings",
"chatterbot.corpus.english.conversations"
)trainer.train(
"./data/greetings_corpus/custom.corpus.json","./data/my_corpus/"
)
chatbot = ChatBot(
'Bob the Bot',
preprocessors=[
'chatterbot.preprocessors.clean_whitespace'
]
)from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
chatbot = ChatBot(
# ...
response_selection_method=get_most_frequent_response
)
response = self.select_response(
input_statement,
list_of_response_options,
self.chatbot.storage
)
from chatterbot.logic import LogicAdapter
class MyLogicAdapter(LogicAdapter):
def __init__(self, chatbot, **kwargs):
super().__init__(chatbot, **kwargs)
def can_process(self, statement):
return Truedef process(self, input_statement, additional_response_selection_parameters):
import random
# Randomly select a confidence between 0 and 1
confidence = random.uniform(0, 1)
# For this example, we will just return the input as output
selected_statement = input_statement
selected_statement.confidence = confidence
return selected_statementChatBot(
# ...
logic_adapters=[
{
'import_path': 'cool_adapter.MyLogicAdapter'
}
]
)def can_process(self, statement):
if statement.text.startswith('Hey Mike'):
return True
else:
return Falsedef can_process(self, statement):
"""
Return true if the input statement contains
'what' and 'is' and 'temperature'.
"""
words = ['what', 'is', 'temperature']
if all(x in statement.text.split() for x in words):
return True
else:
return False
def process(self, input_statement, additional_response_selection_parameters):
from chatterbot.conversation import Statement
import requests
# Make a request to the temperature API
response = requests.get('https://api.temperature.com/current?units=celsius')
data = response.json()
# Let's base the confidence value on if the request was successful
if response.status_code == 200:
confidence = 1
else:
confidence = 0
temperature = data.get('temperature', 'unavailable')
response_statement = Statement(text='The current temperature is {}'.
˓→format(temperature))
return confidence, response_statementclass MyLogicAdapter(LogicAdapter):
def __init__(self, chatbot, **kwargs):
super().__init__(chatbot, **kwargs)
self.api_key = kwargs.get('secret_key')
chatbot = ChatBot(
# ...
secret_key='************************'
)
chatbot = ChatBot(
"My ChatterBot",
logic_adapters=[
"chatterbot.logic.BestMatch"
]
)chatbot = ChatBot(
"My ChatterBot",
logic_adapters=[
{
"import_path": "chatterbot.logic.BestMatch",
"statement_comparison_function": chatterbot.comparisons.
˓→LevenshteinDistance,
"response_selection_method": chatterbot.response_selection.get_first_
˓→response
}
]
)
from chatterbot import ChatBot
# Create a new instance of a ChatBot
bot = ChatBot(
'Exact Response Example Bot',
storage_adapter='chatterbot.storage.SQLStorageAdapter',logic_adapters=[
{
'import_path': 'chatterbot.logic.BestMatch'
},
{
'import_path': 'chatterbot.logic.SpecificResponseAdapter',
'input_text': 'Help me!',
'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
}
]
)
# Get a response given the specific input
response = bot.get_response('Help me!')
print(response)from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create a new instance of a ChatBot
bot = ChatBot(
'Example Bot',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
{
'import_path': 'chatterbot.logic.BestMatch',
'default_response': 'I am sorry, but I do not understand.',
'maximum_similarity_threshold': 0.90
}
]
)
trainer = ListTrainer(bot)
# Train the chat bot with a few responses
trainer.train([
'How can I help you?',
'I want to create a chat bot',
'Have you read the documentation?',
'No, I have not',
'This should help get you started: http://chatterbot.rtfd.org/en/latest/
˓→quickstart.html'
])
# Get a response for some unexpected input
response = bot.get_response('How do I make an omelette?')
print(response)def test_search_text_results_after_training(self):
"""
ChatterBot should return close matches to an input
string when filtering using the search_text parameter.
"""
self.chatbot.storage.create_many([
Statement('Example A for search.'),
Statement('Another example.'),
Statement('Example B for search.'),
Statement(text='Another statement.'),
])
results = list(self.chatbot.storage.filter(
search_text=self.chatbot.storage.tagger.get_text_index_string(
'Example A for search.'
)
))
self.assertEqual(len(results), 1)
self.assertEqual('Example A for search.', results[0].text)import logging
from chatterbot import languages
from chatterbot.tagging import PosLemmaTagger
class StorageAdapter(object):
"""
This is an abstract class that represents the interface
that all storage adapters should implement.
"""
def __init__(self, *args, **kwargs):
"""
Initialize common attributes shared by all storage adapters.
:param str tagger_language: The language that the tagger uses to remove
˓→stopwords.
"""
self.logger = kwargs.get('logger', logging.getLogger(__name__))
Tagger = kwargs.get('tagger', PosLemmaTagger)
self.tagger = Tagger(language=kwargs.get(
'tagger_language', languages.ENG
))
def get_model(self, model_name):
"""
Return the model class for a given model name.
model_name is case insensitive.
"""
get_model_method = getattr(self, 'get_%s_model' % (
model_name.lower(),
))
return get_model_method()
def get_object(self, object_name):
"""
Return the class for a given object name.
object_name is case insensitive.
"""
get_model_method = getattr(self, 'get_%s_object' % (
object_name.lower(),
))
return get_model_method()
def get_statement_object(self):
from chatterbot.conversation import Statement
StatementModel = self.get_model('statement')
Statement.statement_field_names.extend(
StatementModel.extra_statement_field_names)
return Statement
def count(self):
"""
Return the number of entries in the database.
"""
raise self.AdapterMethodNotImplementedError(
'The `count` method is not implemented by this adapter.'
)
def remove(self, statement_text):
"""
Removes the statement that matches the input text.
Removes any responses from statements where the response text matches
the input text.
"""
raise self.AdapterMethodNotImplementedError(
'The `remove` method is not implemented by this adapter.'
)
def filter(self, **kwargs):
"""
Returns a list of objects from the database.
The kwargs parameter can contain any number
of attributes. Only objects which contain
all listed attributes and in which all values
match for all listed attributes will be returned.
:param page_size: The maximum number of records to load into
memory at once when returning results.
Defaults to 1000
:param order_by: The field name that should be used to determine
the order that results are returned in.
Defaults to None
:param tags: A list of tags. When specified, the results will only
include statements that have a tag in the provided list.
Defaults to [] (empty list)
:param exclude_text: If the ``text`` of a statement is an exact match
for the value of this parameter the statement will not be
included in the result set.
Defaults to None
:param exclude_text_words: If the ``text`` of a statement contains a
word from this list then the statement will not be included in
the result set.
Defaults to [] (empty list)
:param persona_not_startswith: If the ``persona`` field of a
statement starts with the value specified by this parameter,
then the statement will not be returned in the result set.
Defaults to None:param search_text_contains: If the ``search_text`` field of a
statement contains a word that is in the string provided to
this parameter, then the statement will be included in the
result set.
Defaults to None
"""
raise self.AdapterMethodNotImplementedError(
'The `filter` method is not implemented by this adapter.'
)
def create(self, **kwargs):
"""
Creates a new statement matching the keyword arguments specified.
Returns the created statement.
"""
raise self.AdapterMethodNotImplementedError(
'The `create` method is not implemented by this adapter.'
)
def create_many(self, statements):
"""
Creates multiple statement entries.
"""
raise self.AdapterMethodNotImplementedError(
'The `create_many` method is not implemented by this adapter.'
)
def update(self, statement):
"""
Modifies an entry in the database.
Creates an entry if one does not exist.
"""
raise self.AdapterMethodNotImplementedError(
'The `update` method is not implemented by this adapter.'
)
def get_random(self):
"""
Returns a random statement from the database.
"""
raise self.AdapterMethodNotImplementedError(
'The `get_random` method is not implemented by this adapter.'
)
def drop(self):
"""
Drop the database attached to a given adapter.
"""
raise self.AdapterMethodNotImplementedError(
'The `drop` method is not implemented by this adapter.'
)
class EmptyDatabaseException(Exception):
def __init__(self, message=None):
default = 'The database currently contains no entries. At least one entry
˓→is expected. You may need to train your chat bot to populate your database.'super().__init__(message or default)
class AdapterMethodNotImplementedError(NotImplementedError):
"""
An exception to be raised when a storage adapter method has not been
˓→implemented.
Typically this indicates that the method should be implement in a subclass.
"""
pass
chatbot = ChatBot(
"My ChatterBot",
storage_adapter="chatterbot.storage.SQLStorageAdapter"
)
chatbot = ChatBot(
"My ChatterBot",
filters=[filters.get_recent_repeated_responses]
)
ChatBot(
'Northumberland',
storage_adapter='my.storage.AdapterClass',
logic_adapters=[
'my.logic.AdapterClass1',
'my.logic.AdapterClass2'
],
logger=custom_logger
)ChatBot(
'Leander Jenkins',
storage_adapter={
'import_path': 'my.storage.AdapterClass',
'database_uri': 'protocol://my-database'
},
logic_adapters=[
{
'import_path': 'my.logic.AdapterClass1',
'statement_comparison_function': chatterbot.comparisons.
˓→LevenshteinDistance
'response_selection_method': chatterbot.response_selection.get_first_
˓→response
},
{
'import_path': 'my.logic.AdapterClass2',
'statement_comparison_function': my_custom_comparison_function
'response_selection_method': my_custom_selection_method
}
]
)import logging
logging.basicConfig(level=logging.INFO)
ChatBot(
# ...
)import logging
custom_logger = logging.getLogger(__name__)
ChatBot(
# ...
logger=custom_logger
)def post(self, request, *args, **kwargs):
"""
Return a response to the statement in the posted data.
* The JSON data should contain a 'text' attribute.
"""
input_data = json.loads(request.body.decode('utf-8'))
if 'text' not in input_data:
return JsonResponse({
'text': [
'The attribute "text" is required.'
]
}, status=400)
response = self.chatterbot.get_response(input_data)response_data = response.serialize()
return JsonResponse(response_data, status=200)def comparison_function(statement, other_statement):
# Your comparison logic
# Return yourcalculated value here
return 0.0from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
chatbot = ChatBot(
# ...
statement_comparison_function=LevenshteinDistance
)chatbot = ChatBot('Export Example Bot')
chatbot.trainer.export_for_training('./export.yml')from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''
chatbot = ChatBot('Export Example Bot')
# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
# Now we can export the data to a file
trainer.export_for_training('./my_export.json')CHATTERBOT = {
'name': 'Tech Support Bot',
'logic_adapters': [
'chatterbot.logic.MathematicalEvaluation',
'chatterbot.logic.TimeLogicAdapter',
'chatterbot.logic.BestMatch'
]
}{"text": "My input statement"}
class ChatterBotApiView(View):
"""
Provide an API endpoint to interact with ChatterBot.
"""
chatterbot = ChatBot(**settings.CHATTERBOT)
def post(self, request, *args, **kwargs):
"""
Return a response to the statement in the posted data.
* The JSON data should contain a 'text' attribute.
"""
input_data = json.loads(request.body.decode('utf-8'))
if 'text' not in input_data:
return JsonResponse({
'text': [
'The attribute "text" is required.'
]
}, status=400)
response = self.chatterbot.get_response(input_data)
response_data = response.serialize()
return JsonResponse(response_data, status=200)
def get(self, request, *args, **kwargs):
"""
Return data corresponding to the current conversation.
"""
return JsonResponse({
'name': self.chatterbot.name
})pip install django chatterbot
INSTALLED_APPS = (
# ...
'chatterbot.ext.django_chatterbot',
)def test_get_response_unicode(self):
"""
Test the case that a unicode string is passed in.
"""
response = self.chatbot.get_response(u'')
self.assertGreater(len(response.text), 0)
