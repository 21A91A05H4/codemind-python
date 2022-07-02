s=input()
h=(ord(s[0])-48)*10+ord(s[1])-48
m=(ord(s[3])-48)*10+ord(s[4])-48
an=30*h-11*m*0.5
if an<0:
    an+=360
if an>180:
    an=360-an
print("{:.1f}".format(an))