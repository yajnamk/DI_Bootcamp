class speed():
    speed=0

def cal_speed(dist, time):
    print(" Distance(km) :", dist)
    print(" Time(hr) :", time)
    return dist / time

print(" The calculated Speed(km / hr) is :",
      cal_speed(abs(40.0), abs(2.0)))