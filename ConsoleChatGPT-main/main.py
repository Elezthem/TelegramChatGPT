import openai
import requests

KEY = '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'

# openai.api_key = KEY
#
#
# def generate_response(text):
#     response = openai.Completion.create(
#         prompt=text,
#         engine='text-davinci-003',
#         max_tokens=100,
#         temperature=0.7,
#         n=1,
#         stop=None,
#         timeout=15
#     )
#
#     if response and response.choices:
#         return response.choices[0].text.strip()
#     else:
#         return None
#
# res = generate_response('Привет, как твой день проходит? Какая погода в Киеве?')
# print(res)

import telebot
import openai

telegram_key = '6125916746:AAGoTr1ZPooXOdu-g2IgWO92XUQ8rJjTONs'
openai.api_key = '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'

bot = telebot.TeleBot(telegram_key)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, я твоя ChatGPT! Готов помочь.')

@bot.message_handler(content_types=['text'])
def main(message):
    reply = ''
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message.text,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )

    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = 'Ой, что-то пошло не так'

    bot.send_message(message.chat.id, reply)

bot.polling(none_stop=True)

#def generate(message):
#    url = 'https://api.openai.com/v1/images/generations'

#    headers = {
#        'Authorization': f'Bearer {KEY}',
#        'Content-Type': 'application/json'
#    }

#    response = requests.post(url, json={"prompt": message}, headers=headers)

#    if response.status_code == 200:
#        result = response.json()
#        print(result)
#    else:
#        print("Error: ", response.text)

#text = 'Discord Bot Python'
#generate(text)

# file = open('zapad.mp3', 'rb')

# result = openai.Audio.translate(
#     api_key=KEY,
#     model='whisper-1',
#     file=file,
#     response_format='text'
# )
#
# print(result)
