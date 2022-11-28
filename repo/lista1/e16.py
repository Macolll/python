lis=[["greys",13],["saul",24]]

for i in lis:
    for j in i:
        if(type(j)==int):
            if(j>=18):
                print(f"{i[0]} {j}") 