# import csv
#
# filename = 'sitka_weather_2018_simple.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
# ==================================================
# import csv
#
# filename = 'sitka_weather_2018_simple.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
#
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
# ==================================================
# import csv
#
# filename = 'sitka_weather_2018_simple.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     #5번 인덱스 TMAX만 출력 // 최고기온
#     highs = []
#     for row in reader:
#         highs.append(row[5])
#     print(highs)

#================================================
##온도 그래프 그리기

# import csv
# from matplotlib import pyplot as plt
#
# filename = 'sitka_weather_2018_simple.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     #5번 인덱스 TMAX만 출력 // 최고기온
#     highs = []
#     for row in reader:
#         highs.append(row[5])
#     print(highs)
#
#
# fig = plt.figure(dpi=128, figsize=(10,6))
# plt.plot(highs, c='red')
#
# plt.title("Daily high and low temperatures - 2018", fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Temperature (F)', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()

# ==============================================

#그래프 + 날짜표시

# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
#
# filename = 'sitka_weather_2018_simple.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     #5번 인덱스 TMAX만 출력 // 최고기온
#     dates, highs = [],[]
#     for row in reader:
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         dates.append(current_date)
#
#         high = int(row[5])
#         highs.append(high)
#
#
# fig = plt.figure(dpi=128, figsize=(10,6))
# plt.plot(highs, c='red')
#
# plt.title("Daily high and low temperatures - 2018", fontsize=24)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate() #날짜 레이블이 겹치지 않게 사선으로 표시
# plt.ylabel('Temperature (F)', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()


#그래프 두개 그리기

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #5번 인덱스 TMAX만 출력 // 최고기온
    dates, highs, lows = [],[], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5) #최고온도
ax.plot(dates, lows, c='blue', alpha=0.5) #최저온도
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1) #색 채우기

ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #날짜 레이블이 겹치지 않게 사선으로 표시
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()