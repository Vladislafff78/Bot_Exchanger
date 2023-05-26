from config import bot

from currency import Currency


class APIException(Exception):
    def __str__(self):
        return "Для запуска бота\n" \
               "нажми команду   /start!"


class Currencies:
    currencies = ["RUB", "EUR", "USD"]


@bot.message_handler(commands=["start", "help"])
def helper(message) -> None:
    command_list = "Приветствую!\n" \
                   "Для получения курса обмена валют\n" \
                   "Введите в ряд данные для обмена\n" \
                   "Например: EUR USD 100\n" \
                   "\n" \
                   "Для получения списка доступных \n" \
                   "валют, нажмите команду: /values"
    bot.send_message(message.chat.id, command_list)


@bot.message_handler(commands=["values"])
def list_of_currencies(message) -> None:
    values = " Информация о всех доступных валютах \n" \
             "RUB\n" \
             "EUR\n" \
             "USD"
    bot.send_message(message.chat.id, values)


@bot.message_handler(content_types=["text"])
def starter(message) -> None:
    try:
        text = message.text.upper().split(" ")
        if len(text) == 3:
            FROM, TO, AMOUNT = text
        else:
            raise APIException
    except APIException:
        bot.send_message(message.chat.id, "Для запуска бота\n"
                                          "нажми команду   /start!")
    else:
        if text[0] in Currencies.currencies and text[1] in Currencies.currencies:
            try:
                if float(AMOUNT):
                    formula = Currency.get_price(FROM, TO, AMOUNT)
                    bot.send_message(message.chat.id, "{to} {get:.2f}".format(to=TO, get=formula))
            except ValueError:
                bot.send_message(message.chat.id, "Введена некорректная сумма !")
        else:
            bot.send_message(message.chat.id, "Введена валюта о которой я не знаю!")


bot.polling(non_stop=True)
