from telethon import TelegramClient, events
from telegram import SessionManager

# Inisialisasi sesi
SessionManager.telethon(session_file=True)

# Inisialisasi klien Telegram
api_id = '22768764'
api_hash = 'b7f581bda2bf5bf41ebb20d643006024'
bot_token = '7485975304:AAHsCVFFG559b15tmBozprDv42UUyRABP7w'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Fungsi untuk memproses pesan
def process_message(menyala):
    response = f"Kamu mengirim pesan: {menyala}"
    return response

# Handler event untuk pesan baru
@client.on(events.NewMessage)
async def handler(event):
    message = event.message.message
    response = process_message(message)
    await event.reply(response)

# Mulai klien
client.run_until_disconnected()
