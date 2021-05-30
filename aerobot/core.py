from aerobot.controller import Controller
from aerobot.bot import Bot
import time
import configparser

def parse(msg):
    args = msg.split()
    if args[0] == "/schedule":
        return schedule(args[1:])
    else:
        return 'INVALID COMMAND!'

def schedule(args):
    if (len(args) != 3 or not args[1].isnumeric() or not args[2].isnumeric()):
        return "Incorrect usage!\n/schedule <name> <on-time> <off-time>"
    try:
        controller.set_schedule(args[0], int(args[1]), int(args[2]))
        return "Set new schedule!"
    except AttributeError as err:
        return str(err)

config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())

bot = Bot(config['telegram api']['token'],config['telegram api']['url'],config['telegram api']['whitelisted'].split())

controller = Controller(config['gpio output'])
print(controller.outputs)

while 1:
    bot.getMessages(parse)
    time.sleep(1)