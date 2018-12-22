import telebot
import re
from collections import OrderedDict
from functools import reduce

bot = telebot.TeleBot("your_token")

latynko_soft_digraph_dict = OrderedDict([
    ('cja', 'шя'),
    ('dja', 'дя'),
    ('lja', 'ля'),
    ('mja', 'мя'),
    ('nja', 'ня'),
    ('pja', 'пя'),
    ('rja', 'ря'),
    ('sja', 'ся'),
    ('tja', 'тя'),
    ('vja', 'вя'),
    ('wja', 'вя'),
    ('zja', 'зя'),
    ('cje', 'шє'),
    ('dje', 'дє'),
    ('lje', 'лє'),
    ('mje', 'мє'),
    ('nje', 'нє'),
    ('pje', 'пє'),
    ('rje', 'рє'),
    ('sje', 'сє'),
    ('tje', 'тє'),
    ('vje', 'вє'),
    ('wje', 'вє'),
    ('zje', 'зє'),
    ('cju', 'шю'),
    ('dju', 'дю'),
    ('lju', 'лю'),
    ('mju', 'мю'),
    ('nju', 'ню'),
    ('pju', 'пю'),
    ('rju', 'рю'),
    ('sju', 'сю'),
    ('tju', 'тю'),
    ('vju', 'вю'),
    ('wju', 'вю'),
    ('zju', 'зю'),
    ('cj', 'шь'),
    ('dj', 'дь'),
    ('lj', 'ль'),
    ('nj', 'нь'),
    ('rj', 'рь'),
    ('sj', 'сь'),
    ('tj', 'ть'),
    ('zj', 'зь'),
    ('tsja', 'ця'),
    ('tsje', 'цє'),
    ('tsju', 'цю'),
    ('tsj', 'ць'),
])

latynko_apostrophe_digraph_dict = OrderedDict([
    ('bja', 'б\'я'),
    ('fja', 'ф\'я'),
    ('gja', 'ж\'я'),
    ('hja', 'г\'я'),
    ('kja', 'к\'я'),
    ('m-ja', 'м\'я'),
    ('p-ja', 'п\'я'),
    ('qja', 'ґ\'я'),
    ('r-ja', 'р\'я'),
    ('v-ja', 'в\'я'),
    ('w-ja', 'в\'я'),
    ('xja', 'х\'я'),
    ('z-ja', 'з\'я'),
    ('bje', 'б\'є'),
    ('fje', 'ф\'є'),
    ('gje', 'ж\'є'),
    ('hje', 'г\'є'),
    ('kje', 'к\'є'),
    ('m-je', 'м\'є'),
    ('p-je', 'п\'є'),
    ('qje', 'ґ\'є'),
    ('r-je', 'р\'є'),
    ('v-je', 'в\'є'),
    ('w-je', 'в\'є'),
    ('xje', 'х\'є'),
    ('z-je', 'з\'є'),
    ('bji', 'б\'ї'),
    ('dji', 'д\'ї'),
    ('fji', 'ф\'ї'),
    ('gji', 'ж\'ї'),
    ('hji', 'г\'ї'),
    ('kji', 'к\'ї'),
    ('m-ji', 'м\'ї'),
    ('p-ji', 'п\'ї'),
    ('qji', 'ґ\'ї'),
    ('r-ji', 'р\'ї'),
    ('v-ji', 'в\'ї'),
    ('w-ji', 'в\'ї'),
    ('xji', 'х\'ї'),
    ('z-ji', 'з\'ї'),
    ('bju', 'б\'ю'),
    ('fju', 'ф\'ю'),
    ('gju', 'ж\'ю'),
    ('hju', 'г\'ю'),
    ('kju', 'к\'ю'),
    ('m-ju', 'м\'ю'),
    ('p-ju', 'п\'ю'),
    ('qju', 'ґ\'ю'),
    ('r-ju', 'р\'ю'),
    ('v-ju', 'в\'ю'),
    ('w-ju', 'в\'ю'),
    ('xju', 'х\'ю'),
    ('z-ju', 'з\'ю'),
    ('bj', 'б\'й'),
    ('fj', 'ф\'й'),
    ('gj', 'ж\'й'),
    ('hj', 'г\'й'),
    ('kj', 'к\'й'),
    ('m-j', 'м\'й'),
    ('qj', 'ґ\'й'),
    ('p-j', 'п\'й'),
    ('r-j', 'р\'й'),
    ('v-j', 'в\'й'),
    ('w-j', 'в\'й'),
    ('xj', 'х\'й'),
    ('z-j', 'з\'й'),
])

latynko_jotted_digraph_dict = OrderedDict([
    ('ja', 'я'),
    ('je', 'є'),
    ('ji', 'ї'),
    ('jy', 'ї'),
    ('ju', 'ю'),
])

latynko_letter_dict = OrderedDict([
    ('ctc', 'щ'),
    ('tc', 'ч'),
    ('ts', 'ц'),
    ('a', 'а'),
    ('b', 'б'),
    ('c', 'ш'),
    ('d', 'д'),
    ('e', 'е'),
    ('f', 'ф'),
    ('g', 'ж'),
    ('h', 'г'),
    ('i', 'і'),
    ('j', 'й'),
    ('k', 'к'),
    ('l', 'л'),
    ('m', 'м'),
    ('n', 'н'),
    ('o', 'о'),
    ('p', 'п'),
    ('q', 'ґ'),
    ('r', 'р'),
    ('s', 'с'),
    ('t', 'т'),
    ('u', 'у'),
    ('v', 'в'),
    ('w', 'в'),
    ('x', 'х'),
    ('y', 'и'),
    ('z', 'з'),
])

patterns_dicts = [(re.compile("(%s)" % '|'.join(dict.keys())), dict) for dict in (
    latynko_apostrophe_digraph_dict,
    latynko_jotted_digraph_dict,
    latynko_soft_digraph_dict,
    latynko_letter_dict,
)]


def is_latynka(str):
    # str = str.replace(r'\bhttp[^\b]+', '')
    # return re.search(r'(sj|tc|nj|ynk|tj|nj|aj|ij|bj|cj|dj|uj|vj)', str)
    return re.search(r'[a-z]', str)


def xlate(s, pattern_dict):
    regex, dict = pattern_dict
    return regex.sub(lambda x: dict[x.group()], s)


@bot.message_handler(content_types=['text'])
def reply(message):
    latynka = message.text.lower()
    if is_latynka(latynka):
        # kyrylka = latynko_digraph_pattern.sub(lambda x: print(x.group(), latynko_digraph_dict[x.group()]), kyrylka)
        # kyrylka = latynko_pattern.sub(lambda x: print(x.group()), kyrylka)
        kyrylka = reduce(xlate, patterns_dicts, latynka)
        bot.send_message(message.chat.id, kyrylka)


bot.polling()
