import matplotlib.pyplot as plt

x = ['Station 1','Station 2','Station 3','Station 4','Station 5','Station 6','Station 7','Station 8','Station 9']
with open('solution.final', 'r') as f:  # 打开文件
    data = f.read()  # 读取文件
    a = []
    for line in data:

        a.append(line.split())
        print(a)
        if a.pop() == [',']:
            pass
    print(a)
    y1 = {}

    y1 = [10, 20, 10, 30]
    y2 = [20, 25, 15, 25]
    y3 = [20, 25, 15, 25]
    y4 = [20, 25, 15, 25]
    y5 = [20, 25, 15, 25]
    y6 = [10, 20, 10, 30]
    y7 = [20, 25, 15, 25]
    y8 = [20, 25, 15, 25]
    y9 = [20, 25, 15, 25]




# plot bars in stack manner
# plt.bar(x, y1, color='r')
# plt.bar(x, y2, bottom=y1, color='b')
# plt.bar(x, y3, bottom=y1+y2 ,color='r')
# plt.bar(x, y4, bottom=y1+y2+y3, color='b')
# plt.bar(x, y5, bottom=y1+y2+y3+y4, color='r')
# plt.bar(x, y6, bottom=y1+y2+y3+y4+y5, color='b')
# plt.bar(x, y7, bottom=y1+y2+y3+y4+y5+y6, color='r')
# plt.bar(x, y8, bottom=y1+y2+y3+y4+y5+y6+y7, color='b')
# plt.bar(x, y9, bottom=y1+y2+y3+y4+y5+y6+y7+y8, color='b')

plt.show()