print("hello world")

for i, kk in enumerate(my_number_list):
    print(i,kk)

for zz, mm  in enumerate(my_number_list):
    if zz > 4:
        print(mm)
        #total += zz
    print(zz)


 "if zz > 4

total = 0

for hh, pp in enumerate(my_randomly_organised_stuff):
    if hh > 4:
        print(pp)


indexBlack=[]
indexRed=[]
for i in range(len(x)):
    if x[i]<1 and y[i]>1:
        indexBlack.append(i)
    else:
        indexRed.append(i)

plt.figure()
plt.scatter(x[indexRed], y[indexRed], color='k')
plt.scatter(x[indexBlack], y[indexBlack], color='r')
plt.show()

#ALTERNATIVE

for h, x_val in enumerate(x):
    if x_val<1 and y[i] >1:

# ALTERNATIVE
both= np.logical_and(x<1, y>1)
plt.scatter(x[both], y[both], color='r')
plt.scatter(x[~both], y[~both], color='k')
plt.show()

plt.scatter(x[both], y[both], color='r')
plt.scatter(x[~both], y[~both], color='k')
plt.show()
for aa, zz in enumerate(x):
    if zz < 1:
        print(aa)

for ab, zb in enumerate(y):
    if zb[aa] > 1:
        print(ab)


xtracks = np.load(
            r"C:\Users\Simon Weiler\AppData\Local\Temp\pystarters2019-master\pystarters2019-master\data\dlc_x_tracks.npy")
ytracks = np.load(
            r"C:\Users\Simon Weiler\AppData\Local\Temp\pystarters2019-master\pystarters2019-master\data\dlc_y_tracks.npy")
plt.figure()
plt.plot(xtracks, ytracks, color='r')
plt.show()
plt.plot(xtracks[:1888],ytracks[:1888],color='k')
plt.show()

subx=xtracks[:1888]
suby=ytracks[:1888]


plt.figure()
plt.plot(subx, suby, color='k')
plt.show()
con= np.where(np.diff(subx>200))[0]
plt.scatter(subx[con], suby[con], color='r')
plt.show()

import pandas as pd
speed = pd.read_csv(r"C:\Users\Simon Weiler\AppData\Local\Temp\pystarters2019-master\pystarters2019-master\data\tracks.csv")
xspeed=speed['x_speed']

plt.figure()
plt.plot(xspeed, color='k')
plt.show()

#Functions

def make_a_sound
    print("quack")