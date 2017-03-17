


def binaryConvert(n):
    if n == 0:
        return '0'
    else:
        return binaryConvert(n//2) + str(n%2)

#print(binaryConvert(5))


a = bin(3)

#print(str.replace(a,'b',''))

#print(15//2)



def base10toN(num,n):
   return ((num == 0) and  "0" ) or ( base10toN(num // n, n).strip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[:n][num % n])

if("Leben"):
    print("TEST")
