from matplotlib import pyplot
import seaborn as sns

numAs = 0
numBs = 0
numCs = 0
numDs = 0
numFs = 0

grade  = int(input("시험 성적 입력 후 -1 을 입력하여 종료 : "))
while grade >= 0:
    if grade >= 90.0:
        numAs = numAs + 1
    elif grade >= 80.0:
        numBs = numBs + 1
    elif grade >= 70.0:
        numCs = numCs + 1
    elif grade >= 60.0:
        numDs = numDs + 1
    else:
        numFs += 1

    grade = int(input("시험 성적 입력 후 -1 을 입력하여 종료 : "))

pyplot.style.use("seaborn")
pyplot.rc('font', family='batang')
pyplot.rc('axes', unicode_minus=False)

pyplot.bar(1, numAs)
pyplot.bar(2, numBs)
pyplot.bar(3, numCs)
pyplot.bar(4, numDs)
pyplot.bar(5, numFs)

pyplot.xlabel("등급")
pyplot.ylabel("학생수")

numStudents = numAs + numBs + numCs + numDs + numFs
pyplot.title("%d 명 학생 \n 등급 분포" % numStudents)

pyplot.xticks([1,2,3,4,5],['A','B','C','D','F'])

pyplot.show()


