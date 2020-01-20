import datetime
import time
from json import loads, dump
import csv
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def time_dec(func):
    def wrapper(parm):
        start_time = time.time()
        result = func(parm)
        new_time = time.time()
        print((new_time-start_time))
        return result
    return wrapper


@time_dec
def create_csv_file(data):
    with open('csv_ok.csv', mode='w', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=';')
        writer.writeheader()
        writer.writerows(data)

@time_dec
def create_json_file(data):
    with open('json_ok.json', mode='w', encoding='utf8') as file:
        dump(data, file)


temper = DocxTemplate('report1.docx')
with open('data_ru.json') as file:
    data = loads(file.read())
context = {
    'date': datetime.datetime.now().date(),
    'cars': data,
    'img': InlineImage(temper, 'IiGd2vv6-Cc.jpg', Cm(4))
}
temper.render(context)
temper.save("report_ok.docx")
create_csv_file(data)
with open('csv_ok.csv', mode='r', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter=';')
    data = list(reader)
data = [dict(x) for x in data]
create_json_file(list(data))
