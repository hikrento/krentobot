from aiogram import types
from dispatcher import dp
import config
import random
from array import *

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    button_invite = KeyboardButton('Invite me to the orden!')
    button_random_cat = KeyboardButton('Random Cat')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    greet_kb.add(button_invite, button_random_cat)

    await message.answer("hi.", reply_markup=greet_kb)

@dp.message_handler(lambda message: message.text == "Invite me to the orden!")
async def process_randcat(message: types.Message):
    await message.answer("send me password. if it ll be true i ll send u invite link")

@dp.message_handler(lambda message: message.text == "494444")
async def process_randcat(message: types.Message):
    await message.answer("https://t.me/+ygdHL1GTWZllMTYy")

@dp.message_handler(lambda message: message.text == "Random Cat")
async def process_randcat(message: types.Message):
    cats = [
        'CAACAgIAAxkBAAEEYgRiTKPmQH2TqmM0AlfB3lxBD8GrbgACLhcAAnbsqUhSONZmcbrzYSME',
        'CAACAgIAAxkBAAEEYgZiTKP18IIy7FOK7zA814u87sHgUQACKxYAAlL-QUkTlcssdcKwByME',
        'CAACAgIAAxkBAAEEYghiTKQMdOMLAuOjLG7AriQbH67I8AACIhMAAjGVQUnDun6DQKPWQSME',
        'CAACAgIAAxkBAAEEYgpiTKQbnBTk1UY7qFMYfe4oujUafQACeBcAAl5e6Uua4FtQMS7rZiME',
        'CAACAgIAAxkBAAEEYiJiTKUgvRQKchCvU1AcU37WDtAExQACcBIAAo1uGUhRUkL5gjt1WCME',
        'CAACAgIAAxkBAAEEYg5iTKQ1mRwBrD8NSXDESG9ANWrQ7gAC4RcAAjJ2KEhk_AG4J7o5iSME',
        'CAACAgIAAxkBAAEEYiZiTKVTTfGyMNbx1HEBOyGE4tpKPwAC1RYAAnLeMUj1r--RPMdj-yME',
        'CAACAgIAAxkBAAEEYhJiTKRGwaoxEDTTymbs4yLlRA-RngACDBkAAiZiyUtfSS1RShAQXCME',
        'CAACAgIAAxkBAAEEYhRiTKRNRjgIDyX458GLDcOeXmjgFAAC6BQAAmrfyUuCW-2PIL3BMSME',
        'CAACAgIAAxkBAAEEYhZiTKRWadU3pXfDuU1CZjzI93IWTwACnRMAAo3R0UtBlgtVJTVjbCME',
        'CAACAgIAAxkBAAEEYhhiTKRe0brNvzcdhCvwAAEHUpUm18UAAjcUAALP48lL-1cPeXwzvDQjBA',
        'CAACAgIAAxkBAAEEYhpiTKSaefd-Bb4wpK5w4zRRzL-daQAC1xUAAjni0Euew4kBM4ZPZCME',
        'CAACAgIAAxkBAAEEYhxiTKSimOPsp7p3iQEJD0YYTmHGhgAChhoAAq2BwUtEuouDJcO3XyME',
        'CAACAgIAAxkBAAEEYh5iTKSw5MBJPB5Ph5OpP2RI7vV6PwACixQAAtMncEjDbeKmKcIRGCME',
        'CAACAgIAAxkBAAEEYi5iTKq9CRnVCBpsFNGpY8SpPCOiwAACMxUAAhZmSEkuOG9iyhH7RSME',
        'CAACAgIAAxkBAAEEYjBiTKrSt7y5PvuqUHbQyMFiuMgxFgAC9BUAAmAPKEjThgapEZbujCME',
        'CAACAgIAAxkBAAEEYkZiTKv8rr6zQqbgOVcuQ6mkEtSazwACxRcAAkHhKEgeEKdULvTz5yME',
        'CAACAgIAAxkBAAEEYjRiTKtAWDAmF0qmb6IT0XdOEaPxqAAC0Q8AAqeAyEtx1lPcgJ-pWSME',
        'CAACAgIAAxkBAAEEYjViTKtBj0PUbErAmQlj1VgRDxrmqgACChoAAojy0EtnWpcq_Ye04SME',
        'CAACAgIAAxkBAAEEYjhiTKtS0O5HkzliYfqujynZCtjlBwACqRYAAqnQ0UtEsMKQ0Z3RbyME',
        'CAACAgIAAxkBAAEEYjpiTKtYcpEwD8SEsslWszSf59_zNgACpBIAAopt8EuzZOCk0OgHQSME',
        'CAACAgIAAxkBAAEEYjxiTKt2hLBBJiUUm9dlwsuWFegIFwACdhcAAtUsaUh8hC0Y9ciSbyME',
        'CAACAgIAAxkBAAEEYj5iTKt_yOM7HeXRwZUjVIBGuP8sjgACjhcAAgzYaUjbXjCV4aGCOyME',
        'CAACAgIAAxkBAAEEYkJiTKuuyLA_bXE1xoVc_msY1x1xjAAC3hYAAkAi6Ut6vdE_cd-0-yME'
    ]

    await message.answer_sticker(cats[random.randint(0,len(cats) - 1)])

@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def content_type_example(msg: types.Message):
    await msg.answer('Looking good!xD')