def points(games):
    pnt = 0
    for element in games:
        new_list = element.split(':')
        if int(new_list[0]) > int(new_list[1]):
            pnt += 3
        elif int(new_list[0]) < int(new_list[1]):
            pnt += 0
        elif int(new_list[0]) == int(new_list[1]):
            pnt += 1
    return pnt

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))