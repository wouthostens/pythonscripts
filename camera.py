import aiogram
import time
import os

from picamera import PiCamera
from time import sleep
from subprocess import call

HOME_PATH = os.path.join(os.getenv('HOME'))
API_TOKEN = '5468289271:AAFaxUEw5Bt3-WfO-Pirm8-C3rhhNzPGrt0'

# Handling message from Telegram
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: type.Message):
    
    await message.reply('Hi\n testje tesjtej')


def handleMessage(msg):

    id = msg['chat']['id']
    command = msg['text']

    camera = PiCamera()

    print(f'Command {command} from chat id {id}')

    if command == '/photo':

        print("Taking picture…")

        output = os.path.join(HOME_PATH, 'pic.jpg')

        camera.start_preview()

        camera.capture(output, resize=(640, 480))

        time.sleep(2)

        camera.stop_preview()

        camera.close()

        with open(output, 'rb') as photo:

            bot.sendPhoto(id, photo)
            photo.close()

    elif command == '/video':

        output_h264 = os.path.join(HOME_PATH, 'Desktop', 'prutsen',
                                   f'video {time.strftime("%y%b%d_%H%M%S")}.h264')

        output_mp4 = output_h264.replace('h264', 'mp4')

        camera.resolution = (640, 480)

        camera.framerate = 25

        camera.start_recording(output_h264)

        sleep(10)

        camera.stop_recording()

        camera.close()

        command = ['MP4Box', '-add', output_h264, output_mp4]

        os.remove(output_h264)

        call([command], shell=True)

        with open(output_mp4, 'rb') as video:

            bot.sendVideo(id, video)
            video.close()
    else:

        bot.sendMessage(id, "Command not found..")


bot = telepot.Bot(API_TOKEN)
bot.message_loop(handleMessage)
