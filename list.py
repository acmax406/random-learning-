# xxpppp last 4 word were palindrome
#after one mile means (xxpppp+1) ->>   xppp(p+1) this become palendrome, means x=p+1,p=p
#after one mile xxppp(p+1)+1=xxppp(p+2) --> xppp middle 4 become palindrome means x=p
#after one mile xxppp(p+2)+1=xppp(p+3) become palindrome, means x=p+3,p=p
def ometer(x):
    digit = [0]*6
    T=0
    for i in range(6):
        digit[i]= x % 10
        x=x-digit[i]
        x= int(x/10)# this is to avoid the decimal places

    digit=digit[::-1] #reversing the digits
#======================================================
# xxpppp last 4 word were palindrome
    s=digit[2:6]
    if s == s[::-1]:
        case1=T
#after one mile means (xxpppp+1) ->>   xppp(p+1) this become palendrome, means x=p+1,p=p
        digit[5]=digit[5]+1
        t= digit[1:6]
        if t==t[::-1]:
            case2=T
#after one mile xxppp(p+1)+1=xxppp(p+2) --> xppp middle 4 become palindrome means x=p
            digit[5]=digit[5]+1
            u = digit[1:5]
            if u ==u[::-1]:
                case3=T
#after one mile xxppp(p+2)+1=xppp(p+3) become palindrome, means x=p+3,p=p
                digit[5]=digit[5]+1
                v = digit[0:6]
                if v==v[::-1]:
                    case4=T
    if case1==case2==case3==case4:
        print(x)


for i in range(100000,999999,1):
    print(ometer(i))


