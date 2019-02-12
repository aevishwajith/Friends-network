
class network:
    friend=["viswa","ajith","raj","ram","rahul"]
    viswa=[];
    ajith=[];
    raj=[];
    ram=[];
    rahul=[];
    
    def add(self):
        self.viswa1=self.viswa;
        self.ajith1=self.ajith
        self.raj1=self.raj
        self.ram1=self.ram
        self.rahul1=self.rahul
        print("which person you want to add");
        self.person=input();
        print("you can add upto 3 friends max!!..if it exceeds according to alphabatical order a person will be deleted");
        print("whom to add");
        self.addfriend=input();

     
        
        if(self.person=="viswa"):
          if(len(self.viswa1)<3):
                
            self.viswa1.append(self.addfriend);
            if(self.addfriend=="raj"):
                self.raj1.append(self.person)
            if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
            if(self.addfriend=="ram"):
                self.ram1.append(self.person)
            if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
            
           
          else:
              self.viswa1.sort();
              self.viswa1.remove(self.viswa1[len(self.viswa1)-1])
              self.viswa1.append(self.addfriend);
              if(self.addfriend=="raj"):
                self.raj1.append(self.person)
              if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
              if(self.addfriend=="ram"):
                self.ram1.append(self.person)
              if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
                 
           




        if(self.person=="raj"):
          if(len(self.raj1)<3):
                
            self.raj1.append(self.addfriend);
            if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
            if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
            if(self.addfriend=="ram"):
                self.ram1.append(self.person)
            if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
                
           

          else:
              self.raj1.sort();
              self.raj1.remove(self.raj1[len(self.raj1)-1])
              self.raj1.append(self.addfriend);
              if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
              if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
              if(self.addfriend=="ram"):
                self.ram1.append(self.person)
              if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
                
           




        if(self.person=="ajith"):
          if(len(self.ajith1)<3):
                
            self.ajith1.append(self.addfriend);
            if(self.addfriend=="raj"):
                self.raj1.append(self.person)
            if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
            if(self.addfriend=="ram"):
                self.ram1.append(self.person)
            if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
             
          else:
              self.ajith1.sort();
              self.ajith1.remove(self.ajith1[len(self.ajith1)-1])
              self.ajith1.append(self.addfriend);
              if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
              if(self.addfriend=="raj"):
                self.raj1.append(self.person)
              if(self.addfriend=="ram"):
                self.ram1.append(self.person)
              if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
              




        if(self.person=="ram"):
          if(len(self.ram1)<3):
                
            self.ram1.append(self.addfriend);
            if(self.addfriend=="raj"):
                self.raj1.append(self.person)
            if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
            if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
            if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
            
          else:
              self.ram1.sort();
              self.ram1.remove(self.ram1[len(self.ram1)-1])
              self.ram1.append(self.addfriend);
              if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
              if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
              if(self.addfriend=="raj"):
                self.raj1.append(self.person)
              if(self.addfriend=="rahul"):
                self.rahul1.append(self.person)
              
           
      
    
        if(self.person=="rahul"):
          if(len(self.rahul1)<3):
                
            self.rahul1.append(self.addfriend);
            if(self.addfriend=="raj"):
                self.raj1.append(self.person)
            if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
            if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
            if(self.addfriend=="ram"):
                self.ram1.append(self.person)
            
          else:
              self.rahul1.sort();
              self.rahul1.remove(self.rahul1[len(self.rahul1)-1])
              self.rahul1.append(self.addfriend);
              if(self.addfriend=="viswa"):
                self.viswa1.append(self.person)
              if(self.addfriend=="ajith"):
                self.ajith1.append(self.person)
              if(self.addfriend=="ram"):
                self.ram1.append(self.person)
              if(self.addfriend=="raj"):
                self.raj1.append(self.person)
                  
           
      
        
    def display(self):
        print("whom you want to display");
        self.disp=input();
        if(self.disp=="viswa"):
            print(self.viswa1);
        if(self.disp=="raj"):
            print(self.raj1);
        if(self.disp=="ajith"):
            print(self.ajith1);
        if(self.disp=="ram"):
            print(self.ram1);
        if(self.disp=="rahul"):
            print(self.rahul1);    
            
    def delete(self):
        print("for whom  you want to delete");
        self.deleting=input();
        print("who you want to delete");
        self.person=input();
        if(self.deleting=="viswa"):
            self.viswa1.remove(self.person)
        if(self.deleting=="raj"):
            self.raj1.remove(self.person)
        if(self.deleting=="ajith"):
            self.ajith1.remove(self.person)
        if(self.deleting=="ram"):
            self.ram1.remove(self.person)
        if(self.deleting=="rahul"):
            self.rahul1.remove(self.person)
          

obj=network()
while(True):
  print("1.add 2.delete 3.display");
  ch=int(input("enter choice"));

  if(ch==1):       
    obj.add();
  if(ch==2):
    obj.delete();  
  if(ch==3):
    obj.display();



        
