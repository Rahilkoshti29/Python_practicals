f=0
gr=0
sub1 = int(input("Enter C Marks:"))
if(sub1<40):
    f = f+1
    gr = 40 - sub1
sub2 = int(input("Enter C++ Marks:"))
if(sub2<40):
    f = f+1
    gr = gr + (40 - sub2)
sub3 = int(input("Enter Java Marks:"))
if(sub3<40):
    f = f+1
    gr = gr + (40 - sub3)
sub4 = int(input("Enter Pyhton Marks:"))
if(sub4<40):
    f = f+1
    gr = gr + (40 - sub4)
sub5 = int(input("Enter Php Marks:"))
if(sub5<40):
    f = f+1
    gr = gr + (40 - sub5)

if(f<=2):
    if(gr<=7):
        total = sub1+sub2+sub3+sub4+sub5
        per = (total/500)*100
        print("Total Marks is:",total)
        print("Percentage is:",per)
        
        if(per>=84):
            print("Grade A")
        elif(per<84 and per>=70):
            print("Grade B")
        elif(per<70 and per>=54):
            print("Grade C")
        elif(per<54 and per>=40):
            print("Grade D")
        else:
            print("Grade E")
        if(gr>0):
            print("You passes with gracing marks",gm)
    else:
        print("Your Grace marks is more than seven")
else:
    print("You are failed bcz your failing subject is more than 2")
