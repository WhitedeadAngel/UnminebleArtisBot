from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "DEIN_BOT_TOKEN"

COINS = [
    "BTC",
    "BNB",
    "XRP",
    "LINK",
    "KAS"
]

current_coin = 0


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Willkommen beim UnmineableArtiBot!\n\n"
        "Befehle:\n"
        "/today - Aktueller Coin\n"
        "/next - Nächster Coin\n"
        "/coins - Alle Coins"
    )


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🟢 Aktueller Coin:\n{COINS[current_coin]}"
    )


async def next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    next_coin = (current_coin + 1) % len(COINS)
    await update.message.reply_text(
        f"➡️ Nächster Coin:\n{COINS[next_coin]}"
    )


async def coins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📋 Coin-Rotation:\n\n"
    for coin in COINS:
        text += f"• {coin}\n"

    await update.message.reply_text(text)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("today", today))
app.add_handler(CommandHandler("next", next))
app.add_handler(CommandHandler("coins", coins))

app.run_polling()
