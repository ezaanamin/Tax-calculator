age=int(input("Enter your age"))
income=input("Enter your annual income")
income=float(income)
tax=0
sp=0
AFTR=0
if age<60 and income==20000:
	print(' Income after Tax Reduction =$',income)
elif age<60 and income>20000 and income<=50000:
	tax=0.2
	sp=income*tax
	AFTR=income-sp
	print(' Income after Tax Reduction =$',AFTR)
elif age<60 and income>50000 and income<=100000:
	tax=0.3
	sp=income*tax
	AFTR=income-sp
	print(' Income after Tax Reduction =$',AFTR)
elif age<60 and income>100000:
	tax=0.4
	sp=income*tax
	AFTR=income-sp
	print(' Income after Tax Reduction =$',AFTR)
elif age>=60 and income==20000:
	print(' Income after Tax Reduction =$',income)
elif age>=60 and income>20000 and income <=50000:
	tax=0.1
	sp=income*tax
	AFTR=income-sp
	print(' Income after Tax Reduction =$',AFTR)
elif age>60 and income>50000 and income<=100000:
	tax=0.2
	sp=income*tax
	AFTR=income-sp
	print(' Income after Tax Reduction =$',AFTR)
elif age>60 and income>100000:
	tax=0.3
	sp=income*tax
	AFTR=income-sp
	print(' Income after Tax Reduction =$',AFTR)

	

	




