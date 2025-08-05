
# print(dir())

# функція time() показує
# кількість секунд, які
# минули від 1 січня 1970р
#########################

# import time

# print(time.time())

##########################
# конвертування дати за
# допомогою ASCTIME
##################

# import time

# print(time.asctime())
# print(time.ctime())

# виклик asctime з параметром,
# створює кортеж зі
# значенням дати й часу:
# рік, місяць, день, години
# хвилини, секунди, день тижня
# (0-це понеділок, 1-вівторок),
# день року(тимчасово
# ставимо 0), а також це літній
# час чи ні (0 якщо ні, 1 якщо так)
#############################

# import time

# t=(2020,2,23,10,30,48,6,0,0)
# print(time.asctime(t))

#############################

# import time

# print(time.localtime())

############

# import time

# t=time.localtime()
# year=t[0]
# month=t[1]
# print("Current year " + str(year))
# print("Current month " , month)

##########################################
# функція sleep уповільнює
# відтерміновує запуск програми

# import time
# for x in range(1,11):
#     print(x)
#     time.sleep(4.5)

#################################

# import datetime

# x = datetime.datetime.now()

# print(x)
#################################
# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))
##################################
# To create a date, we can use the
# datetime() class (constructor) of
# the datetime module.

# The datetime() class requires three
# parameters to create a date: year, month, day.
# The datetime() class also takes parameters for
# time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a
# default value of 0, (None for timezone).
########################################
# import datetime

# x = datetime.datetime(2020, 5, 17)

# print(x)
####################################
# The datetime object has a
# method for formatting date
# objects into readable strings.

# The method is called strftime(),
# and takes one parameter, format,
# to specify the format of the returned string:
#####################################
# import datetime

# x = datetime.datetime(2018, 6, 1, 14, 34, 58)

# print(x.strftime("%a")) #Weekday, short version
# print(x.strftime("%A")) #Weekday, full version
# print(x.strftime("%B")) #Month name, full version
# print(x.strftime("%w")) #Weekday as a number 0-6, 0 is Sunday
# print(x.strftime("%d")) #Day of month 01-31
# print(x.strftime("%b")) #Month name, short version
# print(x.strftime("%m")) #Month as a number 01-12
# print(x.strftime("%Y")) #Year, full version
# print(x.strftime("%H")) #Hour 00-23
# print(x.strftime("%I")) #Hour 00-12
# print(x.strftime("%p")) #AM/PM	PM
# print(x.strftime("%M")) #Minute 00-59
# print(x.strftime("%S")) #Second 00-59
