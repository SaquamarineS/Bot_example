import logging
from aiogram import Bot, Dispatcher, executor, types
pip freeze > requirements.txt

TOKEN = '6090188735:AAE-7Q6frjzI4-WiH8cIgBG1fEJSbNYsW30'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_func(message : types.Message):
    await message.raply('Starter')
    
    
    
@dp.message_handler(commands=['help'])
async def start_func(message : types.Message):
    await message.raply('Helper')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)












