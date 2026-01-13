from datetime import datetime


def dateFormat(data = datetime.now(), formato = '%d/%m/%Y'):
    return datetime.strftime(data, formato)

def criarData(data, formato = '%Y-%m-%d'):
    return datetime.strptime(data, formato)

# data = criarData('3031-05-30')
# dataFormat = dateFormat(data, '%Y/%m/%d')

# print(dataFormat)