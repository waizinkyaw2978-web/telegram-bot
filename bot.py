import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = '8263405681:AAH7pXk2RqkDQuiVlZ91z-AnOSOdTIizy9g'


# /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📍 ဆိုင်လိပ်စာနှင့် ဆက်သွယ်ရန်", callback_data='btn_address')],
        [InlineKeyboardButton("🛠 ဝန်ဆောင်မှုများ", callback_data='btn_services')],
        [InlineKeyboardButton("🕐 ဖွင့်ချိန်/ပိတ်ချိန်", callback_data='btn_hours')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "╔══════════════════════╗\n"
        "   🏍 KYAW MOTORCYCLE\n"
        "          SERVICE\n"
        "╚══════════════════════╝\n\n"
        "မင်္ဂလာပါ 🙏 ကြိုဆိုပါတယ်ခင်ဗျာ\n\n"
        "ကျွန်ုပ်တို့ ဆိုင်မှ လူကြီးမင်းတို့၏\n"
        "ဆိုင်ကယ်များကို စိတ်တိုင်းကျ\n"
        "ဝန်ဆောင်မှုပေးလျက်ရှိပါသည်။\n\n"
        "▼ အောက်ပါ Menu မှ ရွေးချယ်ပါ ▼"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)


# Button Click Event
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    try:
        await query.answer()
    except Exception:
        pass

    if query.data == 'btn_address':
        info_text = 
        
            "┌─────────────────────┐\n"
            "│  📍 ဆိုင်တည်နေရာ        │\n"
            "├─────────────────────┤\n"
            "│                                          │\n"
            "│  🏠 မိုးမိတ်မြို့နယ်             │\n"
            "│       ကျောက်မောရွာ          │\n"
            "│                                          │\n"
            "│  📞 09 695 226 842          │\n"
            "│                                          │\n"
            "│  ✈️ @w_z_k_19                 │\n"
            "│                                          │\n"
            
