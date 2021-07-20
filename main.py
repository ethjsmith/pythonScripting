#TODO 10, 11, after 17

import pyWars,sys, secret, codecs, base64, operator
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
def q1(q):
    data = q.data(1)
    return data + 5
def q2(q):
    data = q.data(2)
    return 16 ** data
def q3(q):
    data = q.data(3)
    return float(data)
def q4(q):
    data = q.data(4)
    return data >> 4
def q5(q):
    data = q.data(5)
    return data.decode()
def q6(q):
    data = q.data(6)
    return data.encode()
def q7(q):
    data = q.data(7)
    return ord(data[4])
def q8(q):
    data = q.data(8)
    return len(data.encode())
def q9(q):
    data = q.data(9)
    return codecs.encode(data,"rot_13")
def q10(q):
    data = q.data(10)
    return base64.b64decode(data)
def q11(q):
    data = q.data(11)
    return data.upper()
def q12(q):
    data = q.data(12)
    return data.find("SANS")
def q13(q):
    data = q.data(13)
    return data[::-1]
def q14(q):
    data = q.data(14)
    return data + data[::-1] + data
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
def q31(q):
    data = q.data(30)
    d = set()
    for x in data:
        for y in x:
            d.add(y)
    print(d)
    return sorted(d)

def q31(q):
    data = q.data(31)
    return sorted(data)

def q32(q):
    data = q.data(32)
    lst = []
    for x in data:
        lst.append(data[x])
    return sorted(lst)

def q33(q):
    data = q.data(33)
    lst = []
    for x in data:
        lst.append((x,data[x]))
    return sorted(lst)

def q34(q):
    data = q.data(34)
    return data["python"] + data["rocks"]

def q35(q):
    data = q.data(35)
    # I can't read lol
    return data["6-2017"]["Vista"]

def q36(q):# yeah
    data = q.data(36)
    btotal = 0
    best = ""
    for x in data:
        total =float(data[x]["WinXP"]) + float(data[x]["Vista"]) + float(data[x]["NT*"])
        if total > btotal:
            best = x
            btotal = total
    return best[0]

def q37(q):
    data = q.data(37)
    return sorted(data)

def q38(q):
    data = q.data(38)
    ans = []
    for x in data:
        z = x.split(",")
        if int(z[1]) % int(z[0]) == 0:
            ans.append("True")
        else:
            ans.append("False")
    return ans
def q39(q):
    data = q.data(39)
    ans = []
    for x in data:
        ans.append(type(x))
    return ans

def q40(q): # what ?? brute force, try different things each time or this wont work, answer is "turtle"
    data = q.data(40)
    data = data.split(",")
    d2 = []
    for x in data:
        y = x.split(":")
        d2.append(y[1])
    for x in d2[::-1]:
        print(f"trying {x}, {q.answer(x)}")
def current(q): # FINISH THIS ONE
    data = q.data(41)
    decry = b""
    a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(data, "0x61")]
    # for char in data:
    #     #z = char.encode() ^ "0x61".encode()
    #     decry += operator.xor(ord(char),ord("0x61"))
    #     #a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)]
    # print(decry)
    print(a_list)
    return a_list



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
