import re
import json
import urllib.request


def get_exchange_rate(currency):
    url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREX"+currency.upper()+"CNY&column=Code,Price"
    req = urllib.request.Request(url)
    f = urllib.request.urlopen(req)
    html = f.read().decode("utf-8")

    s = re.findall("{.*}", str(html))[0]
    sjson = json.loads(s)

    USDCNY = sjson["Data"][0][0][1]/10000
    rate = currency.upper() + "汇率： " + str(USDCNY)
    return rate