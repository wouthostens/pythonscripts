import RPi.GPIO as GPIO
import time
from telegram.ext import Updater, CommandHandler
from threading import Timer

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our water pump connected to
pump = 26
# Set the GPIO pin to output mode
GPIO.setup(pump, GPIO.OUT, initial=GPIO.LOW)

# Define your Telegram bot token
TOKEN = '5637161607:AAHxKNLV-XgA6t6n5IL9IPv-j2_j2MQEhQY'

repeat_timer = None

def water_pump(update, context):
    print("Turning on water pump")
    GPIO.output(pump, GPIO.HIGH)  # Turn on the water pump
    time.sleep(10)  # Pump water for 10 seconds
    print("Turning off water pump")
    GPIO.output(pump, GPIO.LOW)  # Turn off the water pump
    update.message.reply_text('Watered the plant!')

def repeat(update, context):
    global repeat_timer
    if repeat_timer is not None:
        repeat_timer.cancel()
    days = int(context.args[0].replace('d', ''))
    repeat_timer = Timer(days * 24 * 60 * 60, water_pump, args=[update, context])
    repeat_timer.start()
    update.message.reply_text(f'Set to water every {days} days!')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('water', water_pump))
dispatcher.add_handler(CommandHandler('repeat', repeat))
updater.start_polling()

while True:
    time.sleep(1)