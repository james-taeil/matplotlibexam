# import csv
#
# filename = '8month_date.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
#
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
#
# import csv
#
# filename = '8month_date.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
#
#     temperature = []
#     for row in reader:
#         temperature.append(row[3])
#     print(temperature)

# #8월달 온도
# import csv
# from matplotlib import pyplot as plt
#
# filename = '8month_date.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     temperature = []
#     for row in reader:
#         temperature.append(row[3])
#         temperature.sort()
#     print(temperature)
#
# fig = plt.figure(figsize=(20,20))
# plt.plot(temperature, c='red')
#
# plt.title("KOREA - 2020.08", fontsize=24)
# plt.xlabel('',fontsize=16)
# plt.ylabel("Temperature (C)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=5)
#
# plt.show()
#
# #7월달 온도
# import csv
# from matplotlib import pyplot as plt
#
# filename = 'OBS_ASOS_TIM_20200717142443.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     temperature = []
#     for row in reader:
#         temperature.append(row[3])
#         temperature.sort()
#     print(temperature)
#
# fig = plt.figure(figsize=(10,10))
# plt.plot(temperature, c='red')
#
# plt.title("KOREA - 2020.07", fontsize=24)
# plt.xlabel('',fontsize=16)
# plt.ylabel("Temperature (C)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=5)
#
# plt.show()


#
import csv
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt

filename = 'OBS_ASOS_TIM_20200717142443.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    city, temperature = [], []
    for row in reader:
        city.append(row[1])
        temperature.append(row[3])
        temperature.sort()
    print(city)
    print(temperature)

plt.style.use('seaborn')
plt.rc('font', family='batang')
plt.rc('axes', unicode_minus=False)

fig = plt.figure(figsize=(10,10))
plt.plot(temperature, c='red')

plt.title("한국 도시 30cm 지중 온도 - 2020.07", fontsize=24)
plt.xlabel('지점명(도시)', fontsize=24)
fig.autofmt_xdate() #날짜 레이블이 겹치지 않게 사선으로 표시
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()