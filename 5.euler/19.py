# # 1900년 1월 1일 월요일
# # 0 = Sun , 1 = Mon , .. , 6 = Sat

# year1 = [31,28,31,30,31,30,31,31,30,31,30,31]
# year2 = [31,29,31,30,31,30,31,31,30,31,30,31] # 윤년

# # def calander(Y, M, D, DD):


# def checkSun():
#     DD = 1
#     num = 0
#     for i in range(1901, 2000 + 1):
#         year = year1
#         if  i % 4 == 0 :
#             year = year2
#             if i % 100 == 0:
#                 year = year1
#                 if i % 400 == 0:
#                     year = year2
#         for jj , j in enumerate(year):
#             for k in range(j):
#                 if k == 0 and DD%7 == 0:
#                     num += 1
#                     print(i,jj+1, DD)
#                 DD += 1
#     print(num)

# if __name__ == "__main__":
#     checkSun()

from datetime import datetime, timedelta 
startDate = datetime(1901,1,1) 
endDate = datetime(2000,12,31) 
plusDay = timedelta(days=1) 
countOfSunday = 0 
while True: 
    if startDate == endDate:
        break; 
    if startDate.weekday() == 6 and startDate.day == 1: #일요일이고 1일 
        countOfSunday += 1 
        print (startDate) 
    startDate = startDate + plusDay #하루 증가 
print (countOfSunday)
