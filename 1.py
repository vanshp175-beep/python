#1.Accept the project marks, internal marks, external marks from student
#2. passmarks is 50 in each subject
#3. calculate total score if student got more than or equal to 50 in each subject.

#total_score=70% on project+20% on external+10% on internal
   #Print A grade if score is 90+
         #B grade if score b/w 70-90
         #C grade if scpre b/w 50-70      

Internalmarks=int(input("enter the marks"))
externalmarks=int(input("enter the marks"))
projectmarks=int(input("enter the marks"))
passmarks=50
if Internalmarks>=passmarks and externalmarks>=passmarks and projectmarks>=passmarks:
  print("pass")
else:
  print("fail")

Total_score=(0.7*Internalmarks)+(0.1*Internalmarks)+(0.2*externalmarks)
if Total_score>=90:
  print("A grade")
elif Total_score>=70:
  print("B grade")
elif Total_score>=50:
  print("C grade")
else:
  print("fail")




        