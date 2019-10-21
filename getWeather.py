from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
from googletrans import Translator
translator = Translator()

def get_weather():

    data = YahooWeather(APP_ID="YHtM6G4m",
                     api_key="dj0yJmk9akZCYUNvMktDYVBKJmQ9WVdrOVdVaDBUVFpITkcwbWN"
                             "HbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWYz",
                     api_secret="4ba0d4a13d3f3c8da7fa13a96de81c027feded92")

    data.get_yahoo_weather_by_city("beijing", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_beijing = "北京: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("sheffield", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_sheffield = "谢菲尔德: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("Nottingham", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_Nottingham = "诺丁汉: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("tokyo", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_tokyo = "东京: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("boston", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_boston = "波士顿: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("anshun", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_anshun = "安顺: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("chengdu", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_chengdu = "成都: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("jinan", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_jinan = "济南: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("shanghai", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_shanghai = "上海: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("guangzhou", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_guangzhou = "广州: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    data.get_yahoo_weather_by_city("quanzhou", Unit.celsius)
    weather_cn = translator.translate(data.condition.text, dest='zh-CN').text
    if weather_cn == '明确':
        weather_cn = '晴朗'
    weather_quanzhou = "泉州: " + str(data.condition.temperature) + "度  " + str(weather_cn)

    weather = weather_beijing + '\n' + weather_sheffield + '\n' + weather_Nottingham + '\n'+ weather_tokyo + '\n'\
                + weather_boston + '\n' + weather_anshun + '\n' + weather_chengdu + '\n' + weather_jinan + '\n'\
                + weather_shanghai + '\n' + weather_guangzhou + '\n' + weather_quanzhou

    return weather
    print(weather)
