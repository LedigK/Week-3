#ex3.3
score = input("Enter Score:", )
try:
    g = float(score)
except:
    print("Bad Score")
    quit()
if g >= 0.9 and g < 1.0:
    print("A")
elif g >= 0.8 and g < 0.9:
    print("B")
elif g >= 0.7 and g < 0.8:
    print("C")
elif g >= 0.6 and g < 0.7:
    print("D")
elif g < 0.6:
    print("F")
else:
    print("Bad Score")
    quit()
