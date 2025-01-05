import telebot
import os

bot = telebot.TeleBot(os.environ.get('TOKEN'))
chat_id = os.environ.get('CHAT_ID')
release_tag = os.environ.get('RELEASE_TAG')
release_title = os.environ.get('RELEASE_TITLE')
release_body = os.environ.get('RELEASE_BODY')

message = (
    f'🎉 {release_tag} - {release_title}\n\n'
    f'🛠 Changes:\n'
    f'{release_body}\n\n'
    f'<a href="https://github.com/eternnoir/pyTelegramBotAPI/releases/tag/{release_tag}">Release</a>'
)

bot.send_message(
    chat_id,
    message,
    parse_mode='HTML',
    link_preview_options=telebot.types.LinkPreviewOptions(is_disabled=True)
)
