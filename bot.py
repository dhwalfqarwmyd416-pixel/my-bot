import os
import telebot

TOKEN = "8960355775:AAGKtHXpzb8uZTPT5i5AIXGwwJnzbUydxjA"
CHANNEL_USERNAME = "@Zulfiqar_i_store"

bot = telebot.TeleBot(TOKEN)
DOWNLOAD_FOLDER = "./downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@bot.message_handler(content_types=['video'])
def handle_video(message):
    print("وصل فيديو جديد، جاري التحميل...")
    try:
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        file_path = os.path.join(DOWNLOAD_FOLDER, f"video_{message.video.file_id}.mp4")
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        with open(file_path, 'rb') as video_file:
            bot.send_video(CHANNEL_USERNAME, video_file, caption="تم النشر تلقائياً 🚀")
            
        bot.reply_to(message, "تم حفظ الفيديو ونشره بالقناة تلقائياً!")
    except Exception as e:
        print(f"صار خطأ: {e}")

print("البوت يشتغل الآن...")
bot.infinity_polling()
