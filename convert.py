   
 import datetime, pytz
from persiantools.jdatetime import JalaliDateTime
from persiantools import digits
 def jdate(self,year,month,day,hour,minute,second,microsecond):
        time = JalaliDateTime.to_jalali(
            datetime.datetime(year, month, day, hour, minute, second,microsecond, pytz.utc)).strftime("%c")
        print(time)
        str_day, int_day, str_month, year, rest = time.split(' ')
        hour,min,sec=rest.split(":")
        print(sec)
        day_dict = {
            'Shanbe': 'شنبه',
            'Yekshanbe': "یکشنبه",
            'Doshanbe': "دوشنبه",
            'Seshanbe': "سه شنبه",
            'Chaharshanbeh': "چهارشنبه",
            'Panjshanbeh': "پنجشنبه",
            'Jomeh': "جمعه"
        }

        month_dict = {"Farvardin": "فروردین",
                      "Ordibehesht": "اردیبهشت",
                      "Khordad": "خرداد",
                      "Tir": "تیر",
                      "Mordad": "مرداد",
                      "Shahrivar": "شهریور",
                      "Mehr": "مهر",
                      "Aban": "آبان",
                      "Azar": "آذر",
                      "Dey": "دی",
                      "Bahman": "بهمن",
                      "Esfand": "اسفند",

                      }
        formated_time = f'{day_dict[str_day]} {digits.en_to_fa(int_day)} {month_dict[str_month]} {digits.en_to_fa(year)} ساعت {digits.en_to_fa(hour)}: {digits.en_to_fa(min)}:{digits.en_to_fa(sec)}'
        print(formated_time)
        return formated_time
