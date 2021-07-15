#TODO 10, 11, after 17

import pyWars,sys, secret
def login ():
    q = pyWars.exercise("https://od.sec573.com:10000")
    q.login(secret.user(),secret.passw())
    return q

def q(q,num):
    print(f"Question {num}: ")
    q.question(num)
    print( "DATA:  ")
    print(q.data(num))


def ans(q,answer): # use to answer a question :)
    print(q.answer(answer))
def ok (q,num): # write challenges here idk lol
    z = q.data(num)
    z = z + z[::-1] + z
    print(q.answer(z))
def q15(q,num):
    data = q.data(15)
    ans = data[1] + data[4] + data[8]
    print(q.answer(ans))
def q16(q):
    data = q.data(16)
    #print(data)
    tmp = data[0]
    data = data[-1] + data[1:-1] + data[0]
    #print(data)
    ans(q,data)
def q17(q):
    data = q.data(17)
    print(data)
    modded = data[:len(data)//2]
    mod = modded[::-1] + data[len(data)//2:]
    print(mod)
    return mod
def q18(q):
    data = q.data(18)
    dz = data.replace("E","3").replace("A","4").replace("T","7").replace("S","5").replace("G","6")
    return dz
def q19(q):
    return q.data(19)[2]
def q20(q):
    data = q.data(20)
    l = []
    for x in range(data-1):
        l.append(x+1)
    print(l)
    return l
def q21(q):
    return len(q.data(21))

def q22(q):
    data = q.data(22)
    data = data.split(",")
    return data[9]

def q23(q):
    data = q.data(23)
    data = data.split(":")
    data = data[1].split("$")
    return data[2] # tricky
def q24(q):
    data = q.data(24)
    data.append("Pywars rocks")
    return data
def q25(q):
    data = q.data(25)
    total = 0
    for x in data:
        total += x
    return total
def q26(q):
    data = q.data(26)
    data = data.split(" ")
    total = 0
    for x in data:
        total += int(x)
    return total
def q27(q):#first
    data = q.data(27)
    a = "this-python-stuff-really-is-fun"
    a = a.replace("-", data)
    return a

def q28(q):#first
    data = q.data(28)
    ans = []
    for x in range(1,1000):
        if x % data == 0:
            ans.append(x)
    return ans

def q29(q):
    data = q.data(29)
    s = ""
    for x in data:
        b = bytes.fromhex(x)
        aqs = b.decode()
        s += aqs
    print(s)
    return s

if __name__ == "__main__":
    if len(sys.argv) == 3:
            a = login()
            if sys.argv[1] == "q":
                q(a,int(sys.argv[2]))
            elif sys.argv[1] == "a":
                ans(a,current(a))
            else:
                print("error")
    else:
        print(f"enter the correct amount of parameters pls :{len(sys.argv)}")
