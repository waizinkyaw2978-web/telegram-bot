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
        info_text = (
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
            "└─────────────────────┘\n\n"
            "💬 တိုက်ရိုက် ဆက်သွယ်လိုပါက\n"
            "     DM ပို့ပေးပါခင်ဗျာ 🙏"
        )
        await query.message.reply_text(info_text)

    elif query.data == 'btn_services':
        services_text = (
            "┌─────────────────────┐\n"
            "│  🛠 ဝန်ဆောင်မှုများ        │\n"
            "├─────────────────────┤\n"
            "│                                          │\n"
            "│  🔧 EFI ဆိုင်ကယ်             │\n"
            "│      ပြုပြင်ရေး                     │\n"
            "│  ─────────────────  │\n"
            "│  EFI စနစ်သုံး ဆိုင်ကယ်    │\n"
            "│  များကို နည်းပညာ              │\n"
            "│  မှန်ကန်စွာ စစ်ဆေး           │\n"
            "│  ပြုပြင်ပေးခြင်း                  │\n"
            "│                                          │\n"
            "│  🏍 ဆိုင်ကယ် အမျိုးမျိုး  │\n"
            "│      ပြုပြင်/ရောင်းဝယ်ရေး │\n"
            "│  ─────────────────  │\n"
            "│  ဆိုင်ကယ်အမျိုးမျိုး         │\n"
            "│  လက်ခံပြုပြင်ပေးခြင်းနှင့် │\n"
            "│  အရောင်းအဝယ်                 │\n"
            "│  ပြုလုပ်ပေးခြင်း                 │\n"
            "│                                          │\n"
            "│  ⚙️ အပိုပစ္စည်း                  │\n"
            "│      ရောင်းဝယ်ရေး             │\n"
            "│  ─────────────────  │\n"
            "│  အရည်အသွေးမြင့်             │\n"
            "│  ဆိုင်ကယ် အပိုပစ္စည်း      │\n"
            "│  များကို ဈေးနှုန်းမှန်ကန်   │\n"
            "│  စွာ ရောင်းချပေးခြင်း        │\n"
            "│                                          │\n"
            "└─────────────────────┘"
        )
        await query.message.reply_text(services_text)

    elif query.data == 'btn_hours':
        hours_text = (
            "┌─────────────────────┐\n"
            "│  🕐 ဖွင့်ချိန် / ပိတ်ချိန်      │\n"
            "├─────────────────────┤\n"
            "│                                          │\n"
            "│  📅 တနင်္လာ ~ စနေ           │\n"
            "│  ⏰ မနက် 8:00 ~ ည 6:00  │\n"
            "│                                          │\n"
            "│  📅 တနင်္ဂနွေ                     │\n"
            "│  🔴 ပိတ်ရက်                       │\n"
            "│                                          │\n"
            "└─────────────────────┘\n\n"
            "⚡ အရေးပေါ်ဆိုရင် ဖုန်းဆက်ပါ\n"
            "📞 09 695 226 842"
        )
        await query.message.reply_text(hours_text)


# Auto Reply Event
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if any(k in text for k in ["လိပ်စာ", "ဘယ်မှာ", "နေရာ", "ဖုန်း", "ဆက်သွယ်", "address", "phone", "location"]):
        info_text = (
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
            "└─────────────────────┘\n\n"
            "💬 တိုက်ရိုက် ဆက်သွယ်လိုပါက\n"
            "     DM ပို့ပေးပါခင်ဗျာ 🙏"
        )
        await update.message.reply_text(info_text)

    elif any(k in text for k in ["ဝန်ဆောင်မှု", "ပြုပြင်", "ရောင်း", "စျေး", "service", "efi", "အပိုပစ္စည်း"]):
        services_text = (
            "┌─────────────────────┐\n"
            "│  🛠 ဝန်ဆောင်မှုများ        │\n"
            "├─────────────────────┤\n"
            "│                                          │\n"
            "│  🔧 EFI ဆိုင်ကယ် ပြုပြင်ရေး\n"
            "│  🏍 ဆိုင်ကယ် ရောင်းဝယ်ရေး\n"
            "│  ⚙️ အပိုပစ္စည်း ရောင်းချရေး\n"
            "│                                          │\n"
            "└─────────────────────┘\n\n"
            "📩 အသေးစိတ် သိလိုပါက DM ပို့ပါ"
        )
        await update.message.reply_text(services_text)

    elif any(k in text for k in ["ဖွင့်ချိန်", "ပိတ်ချိန်", "ဘယ်အချိန်", "ဘယ်ချိန်"]):
        hours_text = (
            "🕐 တနင်္လာ ~ စနေ\n"
            "⏰ မနက် 8:00 ~ ည 6:00\n\n"
            "🔴 တနင်္ဂနွေ ပိတ်ရက်\n\n"
            "⚡ အရေးပေါ် - 📞 09 695 226 842"
        )
        await update.message.reply_text(hours_text)

    else:
        default_text = (
            "╔══════════════════════╗\n"
            "  🏍 KYAW MOTORCYCLE\n"
            "         SERVICE\n"
            "╚══════════════════════╝\n\n"
            "📩 မက်ဆေ့ခ်ျ လက်ခံရရှိပါပြီ\n\n"
            "မကြာမီ ပြန်လည်ဆက်သွယ်\n"
            "ပေးပါမည်ခင်ဗျာ 🙏\n\n"
            "⚡ အမြန်ဆက်သွယ်လိုပါက\n"
            "📞 09 695 226 842"
        )
        await update.message.reply_text(default_text)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).read_timeout(30).write_timeout(30).connect_timeout(30).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("KYAW MOTORCYCLE SERVICE Bot is running...")
    app.run_polling()
