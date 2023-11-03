# -*- coding: utf-8 -*-



Str1="_setmaterial Plate_75_2 Phase_45 Shotcrete28days"
A=["76_1","76_2","32_1", "54_1", "54_2", "10_1"]
AddNumber=list(range(13))
#A_modified = [str(int(part.split('_')[0]) + n)+'_' + part.split('_')[1] for part in A]
B = [str(x) for x in range(45, 71)]

"""for index1 , i in enumerate(A):
    for index2, j in enumerate(B):
        Str2=Str1
        Str2=Str1.replace("75_2", i)
        Str2=Str2.replace("45", j)
        with open('D:\example.txt', 'a') as file:
            # Write the string to the file
            file.write(Str2+'\n')"""

for index1 , n in enumerate(AddNumber):
    A_modified = [str(int(part.split('_')[0]) + n)+'_' + part.split('_')[1] for part in A]
    for index1 , i in enumerate(A_modified):
        for index2, j in enumerate(B):
            Str2=Str1
            Str2=Str1.replace("75_2", i)
            Str2=Str2.replace("45", j)
            with open('D:\example.txt', 'a') as file:
                # Write the string to the file
                file.write(Str2+'\n')