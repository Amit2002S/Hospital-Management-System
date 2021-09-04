# HARE KRISHNA..

print('      # Welcome To PROJECT #')
print(' *******                ********')
print('   HOSPITAL MANAGEMENT SYSTEM')
print('_______________________________________')
print('\n')

def patient_data():
    d = {'Rohit': ['20', ' A', 'Male', 'Mehata','Dengue','Low'], 'Aditya': ['19', 'B', 'Male','Agraval','Maleria','Normal'],'Amit':['20','A+','Male','Takre','Fever','High']}
    
    k = input("Enter your Name: ")
    k=k.title()
    x = input("Information you want about (Ex. age, blood group, gender,doctor,disease,status of disease): ")

    if k in d:
        if x == 'age':
           print("Patient's age is ",d[k][0])
        elif x == 'blood group':
           print("Patient's blood group is ",d[k][1])  
        elif x =="gender":
        	print("Patient's gender is " ,d[k][2])
        elif x=='doctor':
        	print('Appointed by Doctor' ,d[k][3])
        elif x=='disease':
        	print('Patient suffering from Disease' ,d[k][4])
        elif x=='status of disease':
        	print('Status of disease' ,d[k][5])
        else:
           print('please put correct input')
        
        print('\n Thank you for getting data from our hospital..')
        print('If you have any health issue, then you can register in our hospital and can get proper treatment..')
        print('We are always ready to take your service..')
        print('\n Thank You..')
        print('\n')
   	 
        value()
    else:
        print("\tYou had not taken our services..")  
        print("\tPlease register for our services..")
        print('\n')  

def register():
    q = {}

    k = input("Enter name of patient: ")
    k=k.title()
    a = int(input("Enter your age: "))
   
    b = input("Enter blood group:")
    c = input('Enter gender:')
    m=input('Which doctor do you want:')
    n=input('Enter name of disease:')
    y=input('Status of disease:')
    print("\n")
    p = [a, b,c,m,n,y]
    q.update({k: p})
    print('New Patient:-')
    print(q)
    print('\n Thank you for taking our service..')
    
    with open('file.txt', 'a') as f:
        f.write(f'\n\n{k},{a},{b},{c},{m},{n},{y}')
        
    print("\n")
    value()

def numbers():
    print("108: Medical Emergency Number")
    print("104: Toll-Free Helpline Number for Medical Consultation")
    print("102: Medical Emergency Number for pregnant women and newborn babies")
    print("\n")
    value()
    
def urgent_call():
	print('Connect following numbers for urgent call to doctors:- ( if urgent )')
	print('Dial:8355997799')
	print('Dial:7771236666')
	print('\n')
	value()
	
def delete_all_record():
	print('Patients={  }')
	print('All records of patients are deleted..')
	print('\n')
	value()

def value():
    print("1.Get patients Data")
    print("2.View present records of all patients")
    print("3.Register for our services")
    print('4.Emergency contact numbers')
    print('5.Number for urgent call to doctors')
    print('6.Delete all records of patient')

    p = int(input("Enter your choice: "))
    print("\n")

    if p == 1:
         patient_data()
    elif p==2:
    	
      t = {'1. Rohit': ['20', ' A', 'Male', 'Mehata','Dengue','Low '], '2. Aditya': ['19', 'B+', 'Male','Agraval','Maleria','Normal'],'3.Amit':['20','A+','Male','Takre','Fever','High']}
      print(t)
      print('\nAbove is the list of all patients with details..\nIf you have any concern then call to below number ; ')
      print('Dial: 8880033367')
      print('\n')
    
    elif p == 3:
        register()
    elif p == 4:
        numbers()
    elif p == 5:
    	urgent_call()
    elif p==6:
    	delete_all_record()
    else:
        print("please select correct option")
        print("\n")    
    value()

value()