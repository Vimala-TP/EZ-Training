#Sports Equipment Management Syatem
List_of_items={
   'BT001':['MRF Bat','Good','Available'],
   'BT002':['MRF1 Bat','Good','Available'],
   'HS001':['MR Hocky stick','Better','Available'],
   'HS002':['RR Hocky stick','Good','Available'],
   'FB001':['VM Boll','Better','Available'],
   'VB005':['BE Volley Boll','Good','Available'],
   'BB007':['BB Basket','Good','Available']
 }
sd={}
class Sports:
    def list_of_Equipments(self):
        print('''--------------------------------------------------
{:<7} {:<20} {:<10} {:<12}\n--------------------------------------------------
              '''.format('Eid','EName','Condition','State'))
        for i,j in List_of_items.items():
            EName,Condition,State=j
            print('{:<7} {:<20} {:<10} {:<12}'.format(i,EName,Condition,State)) 
    def take_rent(self):
        print('List of equipments')
        o.list_of_Equipments()
        usn=input('Enter your usn =')
        name=input('Enter your name =')
        while 1:
            eid=input('Enter equipment id =')
            if eid in List_of_items:
                break
            else:
                print('Invalid equipment id\nEnter valid equipment id')
        start_time=input('Enter the start time of taking rent =')
        sd[usn]=[name,eid,start_time,'-']
        List_of_items[eid][2]='Unavailable'
    def return_item(self):
        while 1:
            usn=input('Enter your usn =')
            if usn in sd:
                while 1:
                    eid=input('Enter equipment id =')
                    if eid in List_of_items:
                        break
                    else:
                        print('Invalid equipment id\nEnter valid equipment id')
                end_time=input('Enter the return time of an equipment =')
                sd[usn][3]=end_time
                List_of_items[eid][2]='Available'
                break
            else:
                print('Invalid usn')
    def List_of_students(self):
        print('''-------------------------------------------------------------
{:<7} {:<20} {:<20} {:<10} {:<10}\n-------------------------------------------------------------
              '''.format('USN','Name','Equipment_id','Start_date','End_date'))
        for i,j in sd.items():
            Name,eid,Std,ed=j
            print('{:<7} {:<20} {:<20} {:<10} {:<10}'.format(i,Name,eid,Std,ed)) 
o=Sports()
while 1:
    print('''
---Sports Equpment Management Syatem---          
1.Show the list of equipments
2.Take rent of equipment
3.Return the equipment
4.Show the list of students who took equipment for rent
5.exit''')
    ch=int(input('Enter your choice ='))
    if ch==1:
        o.list_of_Equipments()
    elif ch==2:
        o.take_rent()
    elif ch==3:
        o.return_item()
    elif ch==4:
        o.List_of_students()
    elif ch==5:
        print('Thank You.....:)')
        break
    else:
        print('Invalid choice')       