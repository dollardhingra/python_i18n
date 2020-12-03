from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, locale='en_US')
# locale.setlocale(locale.LC_ALL, locale='en_GB')
# locale.setlocale(locale.LC_ALL, locale='hi_IN.ISCII-DEV')
# locale.setlocale(locale.LC_ALL, locale='pt_BR')
# check installed locale
# locale -a

local_conv = locale.localeconv()
now = datetime.now()

price = locale.format_string(f='%1.2f', val=1234567.89, grouping=True)
currency_symbol = local_conv['currency_symbol']


print(now.strftime('%x'))
print(f'{currency_symbol}{price}')