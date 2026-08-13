import os
import logging
from threading import Thread
from flask import Flask

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Render Web Service အတွက် Web Server ပြုလုပ်ခြင်း
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running live on Render!"

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port)

def keep_alive():
    server_thread = Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()

# Telegram Bot Token
TOKEN = '8875210015:AAHIrK_F-OA8iCE3lxpp86bn8YL0-DtCcSI'

# /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏠 ဆိုင်တည်နေရာ", callback_data='btn_address')],
        [InlineKeyboardButton("⏰ ဆိုင်ဖွင့်ချိန်", callback_data='btn_hours')],
        [InlineKeyboardButton("🛠 ဝန်ဆောင်မှုများ", callback_data='btn_services')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "✨ <b>𝐾𝑌𝐴𝑊 𝑀𝑂𝑇𝑂𝑅𝐶𝑌𝐶𝐿𝐸 𝑆𝐸𝑅𝑉𝐼𝐶𝐸 မှ ကြိုဆိုပါတယ် </b> ✨\n\n"
        "လူကြီးမင်းတို့၏ ဆိုင်ကယ်များကို စိတ်တိုင်းကျ ဝန်ဆောင်မှုပေးရန် အသင့်ရှိနေပါသည်။\n\n"
        "အချက်အလက်များ သိရှိလိုပါက အောက်ပါ Menu များကို နှိပ်ပါ 👇"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='HTML')

# Button Click Event
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'btn_address':
        info_text = (
            "🏠 <b>ဆိုင်တည်နေရာ</b>\n"
            "မိုးမိတ်မြို့နယ်၊ ကျောက်မောရွာ။\n\n"
            "📞 <b>ဆက်သွယ်ရန်ဖုန်း</b>\n"
            "09695226842\n\n"
            "✈️ <b>Telegram</b>\n"
            "@w_z_k_19"
        )
        await query.message.reply_text(info_text, parse_mode='HTML')

    elif query.data == 'btn_hours':
        hours_text = (
            "⏰ <b>ဆိုင်ဖွင့်ချိန်</b>\n\n"
            "နေ့စဉ် မနက် (၆:၀၀) နာရီ မှ\n"
            "ညနေ (၆:၀၀) နာရီ အထိ\n\n"
            "🗓️ <b>ပိတ်ရက်မရှိ နေ့စဉ် ဖွင့်လှစ်ပါသည်။</b>"
        )
        await query.message.reply_text(hours_text, parse_mode='HTML')

    elif query.data == 'btn_services':
        services_text = (
            "🛠 <b>ကျွန်ုပ်တို့၏ ဝန်ဆောင်မှုများ</b>\n\n"
            "🏍 <b>Super 4</b> နှင့် <b>Heavy Bike</b> အမျိုးမျိုးကို စိတ်တိုင်းကျ ပြုပြင်ပေးခြင်း\n\n"
            "⚙️ <b>EFI စနစ်သုံး</b> ဆိုင်ကယ်များကို နည်းပညာမှန်ကန်စွာ စစ်ဆေးပြုပြင်ပေးခြင်း\n\n"
            "🔧 ဆိုင်ကယ်အပိုပစ္စည်း ရောင်းဝယ်ရေးနှင့် အထွေထွေပြုပြင်ရေး"
        )
        await query.message.reply_text(services_text, parse_mode='HTML')

# Auto Reply Event
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()
    
    if any(k in text for k in ["လိပ်စာ", "နေရာ", "address", "location"]):
        msg = "🏠 <b>ဆိုင်တည်နေရာ</b>\nမိုးမိတ်မြို့နယ်၊ ကျောက်မောရွာ။\n\n📞 <b>ဖုန်း:</b> 09695226842"
        await update.message.reply_text(msg, parse_mode='HTML')
    elif any(k in text for k in ["ဖွင့်ချိန်", "ပိတ်ချိန်", "hours", "time"]):
        msg = "⏰ <b>ဆိုင်ဖွင့်ချိန်</b>\nမနက် ၆:၀၀ မှ ညနေ ၆:၀၀ အထိ (ပိတ်ရက်မရှိ)"
        await update.message.reply_text(msg, parse_mode='HTML')
    elif any(k in text for k in ["ဝန်ဆောင်မှု", "ပြုပြင်", "super4", "efi", "service"]):
        msg = "🛠 <b>ဝန်ဆောင်မှုများ</b>\nSuper 4 နှင့် Heavy Bike များ၊ EFI ဆိုင်ကယ်များ ပြုပြင်ပေးခြင်း။"
        await update.message.reply_text(msg, parse_mode='HTML')
    else:
        await update.message.reply_text("လူကြီးမင်း၏ မက်ဆေ့ခ်ျကို လက်ခံရရှိပါသည်။ မကြာမီ ပြန်လည်ဖြေကြားပေးပါမည်။ 🙏")

if __name__ == '__main__':
    keep_alive()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))

    print("Bot is running perfectly...")
    app.run_polling()
