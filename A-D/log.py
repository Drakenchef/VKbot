import datetime


def log(key, comment): # принимает ключ логирования и комментарий
    f = open("log-" + str(datetime.date.today()) + ".txt", "a")
    f.write(f"{key}---{str(datetime.datetime.now())[:-4]}---{comment}\n")
    f.close()