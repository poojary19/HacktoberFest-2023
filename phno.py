import re
def isphonenumber(numstr):
    if len(numstr)!=12:
        return False
    for i in range(len(numstr)):
        if i==3 or i==7:
            if numstr[i]!="-":
                return False
        else:
            if numstr[i].isdigit()==False:
                return False
    return True
def chkphonenumber(numstr):
    ph_no_pattern= re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match(numstr):
        return True
    else:
        return False

ph_num=input("enter the number")
print("without using regular no")
if isphonenumber(ph_num):
    print("valid no")
else:
    print("invalid no")
print(" using regular no")
if chkphonenumber(ph_num):
    print("valid no")
else:
    print("invalid no")
