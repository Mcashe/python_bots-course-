from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F


BOT_TOKEN = '7938316152:AAE_J10eHZHnjdHXOOokda6GLguIjOTmfHM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands="start"))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.answer_photo(message.photo[0].file_id)

@dp.message(F.audio)
async def send_audio_echo(message: Message):
    await message.answer_audio(message.auido.file_id)

@dp.message(F.sticker)
async def send_audio_echo(message: Message):
    await message.answer_audio(message.sticker.file_id)

@dp.message(F.audio_note)
async def send_audio_echo(message: Message):
    await message.answer_audio_note(message.auido.file_id)

if __name__ == '__main__':
    dp.run_polling(bot)