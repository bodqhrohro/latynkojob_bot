# import telebot
import sys
import re
from collections import OrderedDict
from functools import reduce

# bot = telebot.TeleBot("your_token")

latynko_soft_digraph_dict = OrderedDict([
    ('cj',    'шь'),
    ('gj',    'жь'),
    ('tj',    'ть'),
    ('dj',    'дь'),
    ('lj',    'ль'),
    ('nj',    'нь'),
    ('rj',    'рь'),
    ('sj',    'сь'),
    ('zj',    'зь'),
    ('tsj',   'ць'),
    ('tcj',   'чь'),
])

latynko_apostrophe_digraph_dict = OrderedDict([
    ('bj',    'бʼj'),
    ('pj',    'пʼj'),
    ('qj',    'ґʼj'),
    ('kj',    'кʼj'),
    ('fj',    'фʼj'),
    ('vj',    'вʼj'),
    ('wj',    'ввʼj'),
    ('hj',    'гʼj'),
    ('xj',    'хʼj'),
    ('mj',    'мʼj'),
    ('svja',  'свя'), # *ь non-normal // tbh no need, but current OG-fags
    ('tsvja', 'цвя'),
    ('dzvja', 'дзвя'),
    ('tjmja', 'тьмя'),
])

latynko_jotted_digraph_dict = OrderedDict([
    ('ja',    'я'),
    ('je',    'є'),
    ('ji',    'ї'),
    ('jy',    'ї'),
    ('ju',    'ю'),
])

latynko_letter_dict = OrderedDict([
    ('ctc',   'щ'),
    ('tc',    'ч'),
    ('ts',    'ц'),
    ('a',     'а'),
    ('b',     'б'),
    ('c',     'ш'),
    ('d',     'д'),
    ('e',     'е'),
    ('f',     'ф'),
    ('g',     'ж'),
    ('h',     'г'),
    ('i',     'і'),
    ('j',     'й'),
    ('k',     'к'),
    ('l',     'л'),
    ('m',     'м'),
    ('n',     'н'),
    ('o',     'о'),
    ('p',     'п'),
    ('q',     'ґ'),
    ('r',     'р'),
    ('s',     'с'),
    ('t',     'т'),
    ('u',     'у'),
    ('v',     'в'),
    ('w',     'вв'),
    ('x',     'х'),
    ('y',     'и'),
    ('z',     'з'),
    ('\'',    'ʼ'),
])

patterns_dicts = [(re.compile("(%s)" % '|'.join(dict.keys())), dict) for dict in (
    latynko_apostrophe_digraph_dict,
    latynko_jotted_digraph_dict,
    latynko_soft_digraph_dict,
    latynko_letter_dict,
)]


def is_latynka(str):
    return re.search(r"[a-z\']", str)


def xlate(s, pattern_dict):
    regex, dict = pattern_dict
    return regex.sub(lambda x: dict[x.group()], s)


# @bot.message_handler(content_types=['text'])
# def reply(message):
    # latynka = message.text.lower()
latynka = str(sys.argv[1]).lower() 
if is_latynka(latynka):
    kyrylka = reduce(xlate, patterns_dicts, latynka)
        # bot.send_message(message.chat.id, kyrylka)

print(kyrylka)
# bot.polling()
