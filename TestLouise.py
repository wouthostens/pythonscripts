import datetime
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = ''
user_id = ''  # Replace with the target user's ID

def send_pil_pil_pil(update: CallbackContext):
    context = update.context
    context.bot.send_message(chat_id=user_id, text="pil pil pil")
    print("message sended")

def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    # Schedule the job to run every day at a specific time (in this case, 12:00 PM)
    dp.add_handler(CommandHandler("send_pil_pil_pil", send_pil_pil_pil))
    updater.job_queue.run_daily(send_pil_pil_pil, time=datetime.time(hour=12, minute=0))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
