def roman2Dec(romStr):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    romanBack=list(romStr)[::-1]
    value=0
    rightVal =roman_dict[romanBack[0]]
    for numeral in romanBack:
        leftVal=roman_dict[numeral]
        if leftVal<rightVal:
            value-=leftVal
        else:
            value+=leftVal
        rightVal=leftVal
    return value
romanStr=input("enter the roman number")
print(roman2Dec(romanStr))

