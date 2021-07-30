import matplotlib.pyplot as plt

# code used to showcase hysteresis loop 


f = open(r"widthMod_HDS.out\table.txt", "r" )

# readlines returns all lines in a file where each line is an item in the list object
lines = f.readlines()

# defining and appending the magnetising force
m_x = []
i = 0
for x in lines:
    if i > 0:
        m_x.append(float(x.split('\t')[2]))
    i += 1


# defining and appending the external field
b_ext = []
i = 0
for x in lines:
    if i > 0:
        b_ext.append(float(x.split('\t')[5]))
    i += 1
f.close()

# visualising the data
plt.figure()
plt.title("Hysteresis Loop")
plt.xlabel("b_ext(T)")
plt.ylabel("m")
plt.grid()
plt.plot(b_ext,m_x)
plt.savefig("hysteresis_loop.png")
plt.show()



