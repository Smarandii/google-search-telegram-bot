from serpapi import GoogleSearch
from __init__ import bot, SEARCH_API_KEY, TG_ADMIN_ID


def txt_to_bold(txt: str) -> str:
    __BOLD_SYMBOL_START = "*"
    __BOLD_SYMBOL_END = "*"
    txt = prepare_txt_4_md(txt)
    return f"{__BOLD_SYMBOL_START}{txt}{__BOLD_SYMBOL_END}"


def prepare_txt_4_md(txt: str) -> str:
    __RESERVED_SMBLS = ['_', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    txt = str(txt)
    for smbl in __RESERVED_SMBLS:
        txt = txt.replace(smbl, f"\\{smbl}")
    return txt


def get_string_results(message):
    params = {
        "engine": "google",
        "q": message.text,
        "kl": "ru-ru",
        "api_key": SEARCH_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    organic_results = results['organic_results']
    print(organic_results)
    response = ""
    counter = 0
    for result in organic_results:
        if counter >= 5:
            break
        title = f'{result["title"]}\n{result["link"]}'
        response += f'{title}\n\n{result["snippet"]}\n\n\n'
        counter += 1

    print(response)
    return response


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Поиск будет производиться по домену google.ru")


@bot.message_handler(content_types=["text"])
def send_results(message):
    bot.send_message(message.chat.id, get_string_results(message), disable_web_page_preview=True)


while True:
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        bot.send_message(int(TG_ADMIN_ID), e.args)
