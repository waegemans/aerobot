from aerobot.bot import Bot
import time
import configparser
import gpiozero

def parse(msg):
    args = msg.split()
    if args[0] == "/blink":
        return blink()
    else:
        return 'INVALID COMMAND!'

def blink():
    relay.blink(1,0,n=1,background=True)
    return "Blinked"


config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())

bot = Bot(config['telegram api']['token'],config['telegram api']['url'],config['telegram api']['whitelisted'].split())

relay = gpiozero.DigitalOutputDevice(18,False)

while 1:
    bot.getMessages(parse)
    time.sleep(1)