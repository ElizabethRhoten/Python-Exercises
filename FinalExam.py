deer=["Dasher","Dancer","Prancer","Vixen","Comet","Cupid","Donner","Blitzen"]

with open("reindeer.txt","w") as filehandle:
    for listitem in deer:
        filehandle.write("%s\n" % listitem)
        
with open("reindeer.txt","r") as f:
    print(f.read())

