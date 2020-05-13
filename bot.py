from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)
english_bot = ChatBot("ChatterBot", storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("ChatterBotCorpusTrainer")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    usertext = request.args.get('mag')
    return str(english_bot.get_response(usertext))


if __name__('__main__'):
    app.run()
