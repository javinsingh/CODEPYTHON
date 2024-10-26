import random
import time
def getRandomDate(starDate, endDate):
    print("printing random date between",starDate ,"and",endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(starDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    randomtime = starttime - randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomDate





print("RandomDate =", getRandomDate("1/1/2020", "12/12/2024"))