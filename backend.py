import json
import requests
import time
import urllib
import random
from menu import *

token = '510073879:AAF-XCHpIBp-fOyoyqRi-SXxARIQ8wF0uq0'
URL = 'https://api.telegram.org/bot{}/'.format(token)


def get_url(url):
	a = 0
	while a != 1:
		try:
			response = requests.get(url)
			content = response.content.decode('utf8')
			a = 1
			return content
		except: 
			print('There is an issue with connecting to Telegram!')
			time.sleep(10)


def get_json_from_url(url):
	try:
		content = get_url(url)
		js = json.loads(content)
		return js
	except: print("Не удалось преобразовать контент в Json-файл!")


def get_updates(offset=None):
	url = URL + 'getUpdates?timeout=100'
	if offset:
		url += '&offset={}'.format(offset)
	js = get_json_from_url(url)
	return js


def get_last_update_id(updates):
	update_ids = []
	for update in updates['result']:
		update_ids.append(int(update['update_id']))
	return max(update_ids)

def handle_updates(updates):
	for update in updates["result"]:
		chat = update["message"]["chat"]["id"]
		main_keyboard = main_menu_keyboard()
		try:
			text = update["message"]["text"]

			if text.lower() == "/start":
				send_message(
					"Привет, *моя любимая*! Этого бота я сделал специально для тебя. Он может показать тебе, _сколько дней мы уже встречаемся_, "
					"может напомнить, _как давно мы познакомились_. В минуты, когда тебе грустно, *{}*, он всегда придёт тебе на помощь и расскажет, "
					"_почему ты самая лучшая_ и отчего же _я так сильно тебя люблю_. Я вложил в бота частички своей души и безграничной любви к тебе! Я очень "
					"надеюсь, что он тебе понравится, *{}* ❤ ".format(random.choice(names), random.choice(names)),
					chat, main_keyboard)

			elif text.lower() == "наша первая встреча была...":
				days = count_days_from_meeting()
				years = days // 365
				if years < 1:
					send_message("...*{} дней* назад".format(days), chat,
								 main_keyboard)
				elif years == 1:
					send_message("...*1 год* и *{} дней* назад. Время летит так быстро, не правда ли?".format(days - 365), chat,
								 main_keyboard)
					#рандом
					#send_message("...*1 год* и *{} дней* назад. Ты все еще помнишь тот наш ночной разговор?".format(days - 365), chat,main_keyboard)
				else:
					send_message("...*{} года* и *{} дней* назад. Время летит так быстро, не правда ли?".format( years, (days - years * 365) ), chat,
								 main_keyboard)

			elif text.lower() == "мы встречаемся уже...":
				days = count_days_from_offer()
				years = days // 365
				ost = days - years * 365
				if years < 1:
					send_message("...*{} дней*. А ведь ты только представь: с каждым днем я люблю тебя всё больше и больше!".format(days),
								 chat, main_keyboard)
				elif years == 1 and days == 365:
					send_message("...*{} дней*, или *целый ГОДИК*! Это особенный день, {}! Я благодарен тебе за каждую секунду, что мы вместе!".format(days,
								 random.choice(names)), chat, main_keyboard)
				elif years == 1:
					send_message("...*{} дней*, или *целый годик и {} {}*! А ведь ты только представь: с каждым днем я люблю тебя всё больше и больше, {}!".format(days,
								 ost, numbers[ost[len(str(ost))-1:len(str(ost))]], random.choice(names)), chat, main_keyboard)
				else:
					send_message("...*{} дней*, или *{} года и {} дней*! Мы с тобой уже так долго вместе, {}. Спасибо тебе за то, что ты есть!".format(days,
							     years, ost, random.choice(names)), chat, main_keyboard)

			elif text.lower() == "почему я тебя люблю?":
				send_message('Потому что *{}*'.format(random.choice(reasons)), chat, main_keyboard)

			elif text.lower() == "я люблю тебя! ❤":
				send_message("Я тоже тебя люблю, {} ❤ ".format(random.choice(names)), chat, main_keyboard)

			else:
				send_message("Я не обучен такой команде! ^_^", chat, main_keyboard)

		except KeyError:
			send_message("К сожалению, у меня лапки, и я на такие сообщения не отвечаю :)", chat, main_keyboard)
			pass

def get_last_chat_id_and_text(updates):
	num_updates = len(updates['result'])
	last_update = num_updates - 1
	text = updates['result'][last_update]['message']['text']
	chat_id = updates['result'][last_update]['message']['chat']['id']
	return(text, chat_id)


def send_message(text, chat_id, reply_markup = None):
	text = urllib.parse.quote_plus(text)
	url = URL + 'sendMessage?text={}&chat_id={}&parse_mode=Markdown'.format(text, chat_id)
	if reply_markup:
		url += "&reply_markup={}".format(reply_markup)
	get_url(url)


def main_menu_keyboard():
	keyboard = [["Наша первая встреча была..."], ["Мы встречаемся уже..."], ["Почему я тебя люблю?"], ["Я люблю тебя! ❤"]]
	reply_markup = {"keyboard":keyboard, "one_time_keyboard":False, "resize_keyboard": True}
	return json.dumps(reply_markup)


"""
def echo_all(updates):
	for update in updates['result']:
		try:
			text = update['message']['text']
			chat = update['message']['chat']['id']
			send_message(text, chat)
		except Exception as e:
			print(e)
"""

def main():
	last_update_id = None
	print("Getting updates...")
	while True:
		updates = get_updates(last_update_id)
		if len(updates['result']) > 0:
			last_update_id = get_last_update_id(updates) + 1
			handle_updates(updates)


if __name__ == '__main__':
	main()
