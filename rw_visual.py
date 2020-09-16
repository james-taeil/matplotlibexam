import matplotlib.pyplot as plt
from random_walk import RandomWalk

## =============================================
## 랜덤워크 실행
# rw = RandomWalk()
# rw.fill_walk()
#
# plt.scatter(rw.x_values, rw.y_values, s=1)
# plt.show()

## ==============================================
##랜덤워크 반복실행
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.scatter(rw.x_values, rw.y_values, s=1)
#     plt.show()
#
#
#     keep_running = input('다른 랜덤워크를 만들까요?(y/n) : ')
#     if keep_running == 'n' or keep_running == 'N':
#         break

#랜덤워크 계속 만들기
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds,
               edgecolors='none', s=1)

    ax.scatter(0,0,c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('다른 랜덤워크를 만들까요?(y/n) : ')
    if keep_running == 'n' or keep_running == 'N':
        break