from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from command import *
# from log import *
# import datetime


app = ApplicationBuilder().token("5913695353:AAFUR4TxoYT6ROkk5K9h8B7whUa3OqfNiBQ").build()

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("echo", echo_command))
app.add_handler(CommandHandler("sum", sum_command))
# app.add_handler(CommandHandler("time", time_command))
# app.add_handler(CommandHandler("help", help_command))

print("ok")

app.run_polling()