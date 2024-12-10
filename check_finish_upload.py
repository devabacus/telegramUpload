from telethon import TelegramClient, events
import logging
from config import *  # API_ID, API_HASH, BOT_TOKEN должны быть определены в config.py
import os
# Настройка логов
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/bot_log.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Ваш Telegram User ID
YOUR_USER_ID = 748151679  # Замените на ваш User ID

# Инициализация клиента
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Обработчик новых сообщений
@bot.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.file and event.file.name == "list_file.txt":  # Проверяем, загружен ли файл с именем list_file.txt
        # Получаем название группы или топика
        chat = await event.get_chat()
        group_name = chat.title if chat else "Личная переписка"

        # Проверяем, есть ли топик (для супергрупп с обсуждениями)
        topic_id = getattr(event.message, "reply_to_top_msg_id", None)
        topic_info = f"Топик ID: {topic_id}" if topic_id else "Общий чат"

        # Формируем уведомление
        notification = f"Файл 'list_file.txt' был загружен в группу '{group_name}'. {topic_info}."

        # Отправляем уведомление в ваш личный чат (по User ID)
        await bot.send_message(YOUR_USER_ID, notification)
        logger.info(notification)

if __name__ == "__main__":
    logger.info("Бот запущен.")
    bot.run_until_disconnected()
