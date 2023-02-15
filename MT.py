# main command and bot creation

import telebot
from decouple import config


BOT_TOKEN = config('sec')
greatings=["hi","hello","welcome"]
help=['مساعده','مساعدة']
men=['صيانة','صيانه']
one=['1']
tw=['2']
thr=['3']
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
        bot.send_message(message.chat.id,"اهلا بك في المتمكن للاجهزة الكهربائية\n\nالرجاء كيف يمكنني مساعدتك؟\n\nلصيانة ارسل...(صيانة)\n\nللمساعدة ارسل...(مساعدة) \n\n\n")


# answering every message not just commands
def isMSg(message):
    return True

@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split()
    if words [0].lower() in help :
       a= bot.reply_to(message,"تواصل مع قسم الصيانة\n0564523223")


    elif words[0].lower() in men:
        bot.reply_to(message,'الله يسعدك و حياك الله انا تحت خدمتك..\n\n\nارجو منك الاختيار من القائمة\nلحجز طلب جديد(1)\nللاستفسار عن طلب سابق(2)\nلالغاء طلب(3)')
    elif words[0].lower() in one:
        bot.reply_to(message,"الرجاءارسال المعلومات التاليه\n\n\nالاسم:\nالعنوان(ارسال الموقع):\nتفاصيل طلب الصيانة:\nرقم الجوال:\n")
    elif words[0].lower() in greatings:
        bot.reply_to(message,"Hi my name is Almotmken.\n")
    elif words[0].lower()in tw:
        bot.reply_to(message,"الرجاء التواصل مع مشرف الصيانة\nعلى الرقم 0564523223")

    elif words[0].lower() in thr:
        bot.reply_to(message,"الرجاء ارسال رقم الطلب")
    else:
        bot.reply_to(message,"Sorry I don't understand!! please agine")


bot.polling()