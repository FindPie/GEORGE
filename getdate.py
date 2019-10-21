from datetime import datetime
import pytz

def get_date():
    #   获得datetime形式的时间
    #   获得datetime形式的时间
    Amarican_time = pytz.timezone('US/Eastern')
    beijing_time = pytz.timezone('Asia/Shanghai')
    London_time = pytz.timezone('Europe/London')
    japan_time = pytz.timezone('Asia/Tokyo')

    #   将datetime转为合适的结果

    Amarican_time = str(datetime.now(Amarican_time))
    beijing_time = str(datetime.now(beijing_time))
    London_time = str(datetime.now(London_time))
    japan_time = str(datetime.now(japan_time))

    A = Amarican_time.split(' ', 1)
    B = beijing_time.split(' ', 1)
    U = London_time.split(' ', 1)
    J = japan_time.split(' ', 1)

    return A[0], B[0], U[0], J[0]


def get_time():
    #   获得datetime形式的时间
    Amarican_time = pytz.timezone('US/Eastern')
    beijing_time = pytz.timezone('Asia/Shanghai')
    London_time = pytz.timezone('Europe/London')
    japan_time = pytz.timezone('Asia/Tokyo')

    #   将datetime转为合适的结果

    Amarican_time = str(datetime.now(Amarican_time))
    beijing_time = str(datetime.now(beijing_time))
    London_time = str(datetime.now(London_time))
    japan_time = str(datetime.now(japan_time))

    A = Amarican_time.split(' ', 1)
    B = beijing_time.split(' ', 1)
    U = London_time.split(' ', 1)
    J = japan_time.split(' ', 1)

    Amarican_time = A[1].split('.', 1)[0]
    beijing_time = B[1].split('.', 1)[0]
    London_time = U[1].split('.', 1)[0]
    japan_time = J[1].split('.', 1)[0]

    return Amarican_time, beijing_time, London_time, japan_time

#   找时区
#print(pytz.country_timezones('us'))
#print(pytz.all_timezones)
