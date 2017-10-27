import sys

def check(a,b):
    if sorted(list(str(a))) == sorted(list(str(b))):
        return True
    else: return False

num=1

while True:
    if check(num,num*2):
        if check(num,num*3):
            if check(num,num*4):
                if check(num,num*5):
                    if check(num,num*6):
                        print(num)
                        sys.exit()
                    else:
                        num +=1
                        continue
                else:
                    num +=1
                    continue
            else:
                num +=1
                continue
        else:
            num +=1
            continue
    else:
        num +=1
        continue

