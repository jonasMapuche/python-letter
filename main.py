from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Irineu')
bot = ChatBot('Irineu',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Eae',
    'Qual é o seu nome?',
    'Irineu, você não sabe e nem eu',
    'Prazer em te conhecer',
    'Igualmente meu patrão'
])

while True:
    try:
        resposta=bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Irineu: ", resposta)
        else:
            print("Eu nao entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
