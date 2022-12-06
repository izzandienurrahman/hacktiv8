import moduleTes as mt

mt.greeting("Izzan")

a = mt.person1["name"]
print(a)

thisdict={
    "brand":"Ford",
    "model":["Mustang",'2'],
}
for i in thisdict:
    print(thisdict[i])

def convert(fahr,kelv):
    cels=fahr*1.8+32.0
    cels2=kelv-273.15
    return cels, cels2

print("Temperature in Kelvin (K) =",convert(32,20))