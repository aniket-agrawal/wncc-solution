import math

f = open("timestat.txt")
i = 0
n = 0
real = []
tr = float(0)
sr = float(0)
user = []
tu = float(0)
su = float(0)
sys = []
ts = float(0)
ss = float(0)
for x in f:
    if i == 0:
        i = 1
    else:
        y = x.split()
        l = list(y)
        s = l[1]
        t = (float(s[0]) * 60) + (float(s[2:7]))
        if i == 1:
            i = 2
            real += [t]
            tr += t
            sr += t * t
            n += 1
        elif i == 2:
            i = 3
            user += [t]
            tu += t
            su += t * t
        else:
            i = 0
            sys += [t]
            ts += t
            ss += t * t
avgr = float(tr) / n
avgu = float(tu) / n
avgs = float(ts) / n
sdr = float(sr) / n - avgr * avgr
sdr = math.sqrt(sdr)
sdu = float(su) / n - avgu * avgu
sdu = math.sqrt(sdu)
sds = float(ss) / n - avgs * avgs
sds = math.sqrt(sds)
nr = 0
nu = 0
ns = 0
for x in real:
    if avgr - sdr <= x <= avgr + sdr:
        nr += 1
for x in user:
    if avgu - sdu <= x <= avgu + sdu:
        nu += 1
for x in sys:
    if avgs - sds <= x <= avgs + sds:
        ns += 1
print("Average Time statistics")
print("real ", avgr, "user ", avgu, "sys ", avgs)
print("Standard deviation of Time statistics")
print("real ", sdr, "user ", sdu, "sys ", sds)
print("Number of runs within (average - standard deviation) to (average + standard deviation)")
print("real ", nr, "user ", nu, "sys ", ns)
