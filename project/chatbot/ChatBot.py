# -*- coding: utf-8 -*-
import collections
from urllib import parse

from pymongo import MongoClient
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler  # import modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token = '802722566:AAHyHh8GRpIeFRKk9-SgQHxuED7ngjpbeSY'

print('start telegram chat bot')
client= MongoClient('localhost', 27017)
db= client['dbJMT']
collection = db['JMT']

# message reply function
def get_message(bot, update):
    if '안녕' in update.message.text:
        keyboard = [
            [
                InlineKeyboardButton("마포구", callback_data='마포구'),
                InlineKeyboardButton("종로구", callback_data='종로구'),
                InlineKeyboardButton("강남구", callback_data='강남구'),
            ],
            [   InlineKeyboardButton("중구", callback_data='중구'),
                InlineKeyboardButton("서대문구", callback_data='서대문구'),
                InlineKeyboardButton("영등포구", callback_data='영등포구'),
                InlineKeyboardButton("용산구", callback_data='용산구'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('안녕~ 나는 ^^서울시장 맛집봇 이야^^ 이제부터 나의 단골맛집을 소개할게!''지역을 선택해줘~.~', reply_markup=reply_markup)
    elif '잘가' in update.message.text:
        update.message.reply_text('너도 잘가~')
    else:
        update.message.reply_text('"안녕"이라고 말해줄래?')

def callback_get(bot, update):
    chat_id = update.callback_query.message.chat_id
    message_id = update.callback_query.message.message_id
    if '마포구' in update.callback_query.data:
        # DB에서 마포구 읽어오기
        stores = collection.find({'address': {'$regex': '.*마포구.*'}})
        store_list = []
        for store in stores:
            store_list.append(store['store'])
        store_dict = {}
        for store in store_list:
            if store in store_dict:
                store_dict[store] += 1
            else:
                store_dict[store] = 1
        stores = collections.OrderedDict(sorted(store_dict.items(), key=lambda x: int(x[1]), reverse=True))

        store_list = []
        i = 0
        for key, val in stores.items():
            if i == 5:
                break
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(parse.quote(key))
            store_list.append('* 나는 단골가게 "{}"에 총 "{}"회 방문했어 *\n'
                              '자세한 정보는 여기에!: {}'.format(key, val, url))
            i += 1
        # 그 중에서 맛집으로 추정되는 곳 5개 추리기
        bot.edit_message_text('나의 마포구 단골 가게 리스트야 ~.~ \n'
                              '{}\n'.format('\n'.join(store_list)),
                              chat_id=chat_id,
                              message_id=message_id)
    elif '종로구' in update.callback_query.data:
        # DB에서 종로구 읽어오기
        stores = collection.find({'address': {'$regex': '.*종로구.*'}})
        store_list = []
        for store in stores:
            store_list.append(store['store'])
        store_dict ={}
        for store in store_list:
            if store in store_dict:
                store_dict[store] += 1
            else:
                store_dict[store]= 1
        stores = collections.OrderedDict(sorted(store_dict.items(), key=lambda x: int(x[1]), reverse=True))

        store_list = []
        i = 0
        for key, val in stores.items():
            if i == 5:
                break
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(parse.quote(key))
            store_list.append('* 나는 단골가게 "{}"에 총 "{}"회 방문했어 *\n'
                              '자세한 정보는 여기에!: {}'.format(key, val, url))
            i += 1
        # 그 중에서 맛집으로 추정되는 곳 5개 추리기
        bot.edit_message_text('나의 종로구 단골 가게 리스트야 ~.~\n'
                              '{}\n'.format('\n'.join(store_list)),
                              chat_id=chat_id,
                              message_id=message_id)
    elif '강남구' in update.callback_query.data:
        # DB에서 강남구 읽어오기
        stores = collection.find({'address': {'$regex': '.*강남구.*'}})
        store_list = []
        for store in stores:
            store_list.append(store['store'])
        store_dict = {}
        for store in store_list:
            if store in store_dict:
                store_dict[store] += 1
            else:
                store_dict[store] = 1
        stores = collections.OrderedDict(sorted(store_dict.items(), key=lambda x: int(x[1]), reverse=True))

        store_list = []
        i = 0
        for key, val in stores.items():
            if i == 5:
                break
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(parse.quote(key))
            store_list.append('* 나는 단골가게 "{}"에 총 "{}"회 방문했어 *\n'
                              '자세한 정보는 여기에!: {}'.format(key, val, url))
            i += 1
        # 그 중에서 맛집으로 추정되는 곳 5개 추리기
        bot.edit_message_text('나의 강남구 단골 가게 리스트야 ~.~ \n'
                              '{}\n'.format('\n'.join(store_list)),
                              chat_id=chat_id,
                              message_id=message_id)
    elif '중구' in update.callback_query.data:
        # DB에서 구 읽어오기
        stores = collection.find({'address': {'$regex': '.*중구.*'}})
        store_list = []
        for store in stores:
            store_list.append(store['store'])
        store_dict = {}
        for store in store_list:
            if store in store_dict:
                store_dict[store] += 1
            else:
                store_dict[store] = 1
        stores = collections.OrderedDict(sorted(store_dict.items(), key=lambda x: int(x[1]), reverse=True))

        store_list = []
        i = 0
        for key, val in stores.items():
            if i == 5:
                break
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(parse.quote(key))
            store_list.append('* 나는 단골가게 "{}"에 총 "{}"회 방문했어 *\n'
                              '자세한 정보는 여기에!: {}'.format(key, val, url))
            i += 1
        # 그 중에서 맛집으로 추정되는 곳 5개 추리기
        bot.edit_message_text('나의 중구 단골 가게 리스트야 ~.~\n'
                              '{}\n'.format('\n'.join(store_list)),
                              chat_id=chat_id,
                              message_id=message_id)
    elif '서대문구' in update.callback_query.data:
        # DB에서 서대문구 읽어오기
        stores = collection.find({'address': {'$regex': '.*서대문구.*'}})
        store_list = []
        for store in stores:
            store_list.append(store['store'])
        store_dict = {}
        for store in store_list:
            if store in store_dict:
                store_dict[store] += 1
            else:
                store_dict[store] = 1
        stores = collections.OrderedDict(sorted(store_dict.items(), key=lambda x: int(x[1]), reverse=True))

        store_list = []
        i = 0
        for key, val in stores.items():
            if i == 5:
                break
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(parse.quote(key))
            store_list.append('* 나는 단골가게 "{}"에 총 "{}"회 방문했어 *\n'
                              '자세한 정보는 여기에!: {}'.format(key, val, url))
            i += 1
        # 그 중에서 맛집으로 추정되는 곳 5개 추리기
        bot.edit_message_text('나의 서대문구 단골 가게 리스트야 ~.~ \n'
                              '{}\n'.format('\n'.join(store_list)),
                              chat_id=chat_id,
                              message_id=message_id)
    elif '영등포구' in update.callback_query.data:
        # DB에서 영등포구 읽어오기
        stores = collection.find({'address': {'$regex': '.*영등포구.*'}})
        store_list = []
        for store in stores:
            store_list.append(store['store'])
        store_dict = {}
        for store in store_list:
            if store in store_dict:
                store_dict[store] += 1
            else:
                store_dict[store] = 1
        stores = collections.OrderedDict(sorted(store_dict.items(), key=lambda x: int(x[1]), reverse=True))

        store_list = []
        i = 0
        for key, val in stores.items():
            if i == 5:
                break
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(parse.quote(key))
            store_list.append('* 나는 단골가게 "{}"에 총 "{}"회 방문했어 *\n'
                              '자세한 정보는 여기에!: {}'.format(key, val, url))
            i += 1
        # 그 중에서 맛집으로 추정되는 곳 5개 추리기
        bot.edit_message_text('나의 영등포구 단골 가게 리스트야 ~.~ \n'
                              '{}\n'.format('\n'.join(store_list)),
                              chat_id=chat_id,
                              message_id=message_id)
    elif '용산구' in update.callback_query.data:
        # DB에서 용구 읽어오기
        stores = collection.find({'address': {'$regex': '.*용산구.*'}})
        store_list = []
        for store in stores:
            store_list.append(store['store'])
        store_dict = {}
        for store in store_list:
            if store in store_dict:
                store_dict[store] += 1
            else:
                store_dict[store] = 1
        stores = collections.OrderedDict(sorted(store_dict.items(), key=lambda x: int(x[1]), reverse=True))

        store_list = []
        i = 0
        for key, val in stores.items():
            if i == 5:
                break
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(parse.quote(key))
            store_list.append('* 나는 단골가게 "{}"에 총 "{}"회 방문했어 *\n'
                              '자세한 정보는 여기에!: {}'.format(key, val, url))
            i += 1
        # 그 중에서 맛집으로 추정되는 곳 5개 추리기
        bot.edit_message_text('나의 용구 단골 가게 리스트야 ~.~ \n'
                              '{}\n'.format('\n'.join(store_list)),
                              chat_id=chat_id,
                              message_id=message_id)
updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))

updater.start_polling(timeout=3, clean=True)
updater.idle()
