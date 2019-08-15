choice=0
class node:
    def  __init__(self,data):
        self.data=data
        self.nextvalue=None
class linkedlist:
    def __init__(self):
        self.head=None
    def atbegin(self,value):
        newnode=node(value)
        newnode.nextvalue=self.head
        self.head=newnode
def getv():
    print('1.inert value 2.insert value at any position 3.insert at end 4.delete at begining 5.delete at end 6.delete at any position 7.display 8.exit')
    
ll=linkedlist()
choice=1
while(choice!=8):
    if(choice==7):
        temp=ll.head
        while(temp.nextvalue!=None):
            temp=temp.nextvalue
            print(temp.data)
    elif(choice==1):
        a=int(input("enter the value to be inserted "))
        linkedlist.atbegin(a)
    
    elif(choice==2):
        i=1
        val=input('enter the value to be iserted ')
        a=int(input('enter the node position for inserting '))
        temp=linkedlist.head
        while(i<a):
            temp=temp.nextvalue
            i=i+1
        newnode=node(val)
        newnode.nextvalue=temp.nextvalue
        temp.nextvalue=newnode
        
    elif(choice==3):
        temp=lnkedlist.head
        while(temp.nextvalue!= None):
            temp=temp.nextvalue
        a=int(input('enter the value to be inserted '))
        newnode=node(a)
        temp.nextvalue=newnode
        
    elif(choice==4):
        temp=linkedlist.head
        linkedlist.head=linkedlist.head.nextvalue
        temp.data=None
        
    elif(choice==5):
        temp=linkedlist.head
        temp1=temp.nextvalue
        while(temp1.nextvalue!=None):
            temp=temp.nextvalue
            temp1=temp.nextvalue
        temp.nextvalue=None
        temp1=None
        
    elif(choice==6):
        a=int(input('enter the position you want to delete '))
        i=0
        temp=linkedlist.head
        while(i<a):
            temp=temp.nextvalue #node before deleting node
            temp1=temp.nextvalue
            temp2=temp1.nextvalue #node after deleting node
        temp.nextvalue=temp2
        temp1.data=None
        
    elif(c==7):
        temp=linkedlist.head
        while(temp.nextvalue==None):
            print(temp.data)
            temp=temp.nextvalue
        print(temp.data)    
    getv()
    c=int(input('enter the choice'))
        
