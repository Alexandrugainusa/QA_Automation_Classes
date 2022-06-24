xy = [(0, 200), (350, 250), (400, 150), (200, 50)]

# EXPLODE X AND Y
def explode_xy(xy):
    xl = []
    yl= []
    for i in range(len(xy)):
        xl.append(xy[i][0])
        yl.append(xy[i][1])
    return xl,yl


def shoelace_area(x_list, y_list):
    a1, a2 = 0, 0
    x_list.append(x_list[0])
    y_list.append(y_list[0])
    for j in range(len(x_list) - 1):
        a1 += x_list[j] * y_list[j + 1]
        a2 += y_list[j] * x_list[j + 1]
    l = abs(a1 - a2) / 2
    return l


xy_e = explode_xy(xy)
print(xy_e)

A = shoelace_area(xy_e[0], xy_e[1])
print(A)
