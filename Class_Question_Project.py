def value(i):
    if i==1:
        return '\N{SUPERSCRIPT ONE}'
    elif i==2:
        return '\N{SUPERSCRIPT TWO}'
    elif i==3:
        return '\N{SUPERSCRIPT THREE}'
    elif i==4:
        return '\N{SUPERSCRIPT FOUR}'
    elif i==5:
        return '\N{SUPERSCRIPT FIVE}'
    elif i==6:
        return '\N{SUPERSCRIPT SIX}'
    elif i==7:
        return '\N{SUPERSCRIPT SEVEN}'
    elif i==8:
        return '\N{SUPERSCRIPT EIGHT}'
    elif i==9:
        return '\N{SUPERSCRIPT NINE}'
    else:
        return '\N{SUPERSCRIPT FOUR}'


str1 = ''
str2 = ''
str3 = ''
str4 = '   '
str5 = '    '
str6 = '     '
k=1

m = int(input('enter the value of m :  '))
print()
for i in range(1,m+1):
    str1 = str1+str(i)
    digit = list(str(k))
    j=0
    while(j<len(digit)):
        str1 = str1+value(int(digit[j]))
        j = j+1
    if(i>=10):
        str1 = str1+str6
        str3 = str3+str(3)+value(4)+str6+'  '
    else:
        if(i>=6):
            str1 = str1 + str5
            str3 = str3+str(3)+value(4)+str5+' '
        else:
            str1 = str1 + str4
            str3 = str3+str(3)+value(4)+str4+''
    k=k+2
print(str1)
strr = ''
for i in range(m):
    if(i<=5):
        strr = strr+'-- + '
    elif(i>5 and i<=8):
        strr = strr+'  --- +'
    else:
        strr = strr+'  ---- + '
if(m<9):
    print(strr[:-2])
else:
    print(strr[:-3])
print(str3)
