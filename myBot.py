#!/usr/bin/env python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot(
	'SHIBOT',
	storrage_adapter='chatterbot.storrage.SQLStorageAdapter',
	input_adapter='chatterbot.input.TerminalAdapter',
	output_adapter='chatterbot.output.TerminalAdapter',
	logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
	database='./database.sqlite3')
conversation = [
	"ฮัลโหล",
	"เป็นไงมั่ง",
	"เบื่อจัง",
	"ทำไรอยู่",
]
bot.set_trainer(ListTrainer)
bot.train(conversation)
print ("\nReady!")
while(True):
	try:
		bot_input = bot.get_response(None)
	except(KeyboardInterrupt,EOFError,SystemExit):
		break