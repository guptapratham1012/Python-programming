import csv
def write(list_):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(['Name', 'Age', 'Contact_number', 'Email_ID'])
        writer.writerow(list_)

if __name__=='__main__':
    x=True
    num=1
    while(x):
        student=input('Enter Student info for student #{} in the following format(Name, Age, Contact_number, Email_ID):'
                      .format(num))
        
        list_=student.split(' ')

        print('\nEntered information:\nName: {}\nAge: {}\nContact_Number: {}\nEmail_ID: {}'
                  .format(list_[0],list_[1],list_[2],list_[3]))
        ch=input('\nIs the entered information correct?(yes/no): ')
        if ch=='yes':
            write(list_)
            chk=input('Enter(yes/no)to continue with entering student details?: ')
            if chk=='yes':
                x=True
                num=num+1
            elif chk=='no':
                x=False
        elif ch=='no':
            print('User re-enter the values')
