#ex3.2
try:
    hr = input("Enter Hours: ")
    r = input("Enter Rate: ")
except:
    print("Error, Please input numeric value")
fh = float(hr)
fr = float(r)
if fh > 40 :
    # print("overtime")
    reg = fr * fh
    ot = (fh-40.0) * (fr * 0.5)
    # print(reg,ot)
    p = reg + ot
else:
    # print("Regular")
    p = fh * fr
print("pay:", p)
