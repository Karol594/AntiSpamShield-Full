import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode, Update
from database import setup_database

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "8070356889:AAFDGvBBF4A3jH5IUx20rkFHNsPkI3enh5Q")

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
    """Send welcome message when the /start command is issued."""
    user = update.effective_user
    update.message.reply_text(
        f"Сәлем, {user.first_name}! Мен AntiSpamKarakalpak_Bot боламан. "
        f"Топарларды спам ҳәм жаман мәтинлерден қорғайман."
    )

def help_command(update, context):
    """Send help message when the /help command is issued."""
    help_text = (
        "*AntiSpamKarakalpak_Bot жәрдем*\n\n"
        "/start - Ботты баслаў\n"
        "/help - Жәрдем алыў\n"
        "/settings - Топар сазлаўларын өзгертиў (тек администраторлар)\n"
        "/ban - Пайдаланыўшыны бан қылыў (тек администраторлар)\n"
        "/warn - Пайдаланыўшыға ескертиў бериў (тек администраторлар)\n"
    )
    update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)

def main():
    """Start the bot."""
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    setup_database()

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    logger.info("Bot started successfully!")
    updater.idle()

if __name__ == "__main__":
    main()