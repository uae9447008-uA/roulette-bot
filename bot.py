from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from collections import Counter

BOT_TOKEN = "8964099452:AAFoGE9KDxhSylwYY8xBqZ46LfYnqg6bMWk"

async def start(update, context):
    await update.message.reply_text("🎰 أرسل أرقام الروليت")

async def analyze(update, context):
    try:
        nums = [int(x) for x in update.message.text.split()]
        nums = [n for n in nums if 0 <= n <= 36]

        count = Counter(nums)

        msg = "🔥 أكثر الأرقام:\n"

        for n, c in count.most_common(5):
            msg += f"{n} = {c} مرات\n"

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("❌ أرسل أرقام فقط")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze))

app.run_polling()
