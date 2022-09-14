#2.WAP for calculating student marks in 5-subjects,and find  grades,(suppose grade A,B,C and Fail)?
dic={}
while True:
    name=input("Enter name:")
    if name=="":
        break
    else:
        adding=0
        subjects=5
        for i in range(subjects):
            marks=int(input("Enter marks"))
            adding=adding+marks
            average=adding//subjects
        dic[name]=average
    print("\n")
for k,v in dic.items():
    if v>=80:
        print(k,"average marks:-",v,"A Grade")
    elif 60<=v<80:
        print(k,"average marks:-",v,"B Grade")
    elif 35<=v<60:
        print(k,"average marks:-",v,"B Grade")
    else:
        print(k,"average marks:-",v,"Fail")

