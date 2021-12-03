d= int(input("Enter Day:"))
m= int(input("Enter month:"))
y= int(input("Enter year:"))
a= int(str(y)[-2:])
b= a//4
if y >1899 and y<2000 :
    c= 0
if y >1599 and y<1700:
        c=6
if y >1699 and y<1800:
            c= 4
if y>1799 and y<1900:
                c= 2
if y  >1999 and y<2100:
                    c= 6
else :
                        print("The Date provided is out of range")


if m== 1:
    mm= 0
if m== 2:
        mm= 3
if m== 3:
            mm= 3
if m== 4:
                mm= 6
if m== 5:
                    mm=1
if m== 6:
                        mm= 4
if m== 7:
                            mm= 6
if m== 8:
                                mm= 2
if m== 9:
                                    mm= 5
if m== 10:
                                        mm= 0
if m==11:
                                            mm= 3
if m== 12:
                                                mm= 5
                     
 
 

fin_sum= (a+b+d+c+mm)
week= (fin_sum%7)   

if week == 0:
    print("Sunday")
if week==1:
    print("Monday")
if week==2:
    print("Tuesday")
if week==3:
    print("Wednesday")
if week==4:
    print("Thursday")
if week ==5:
    print("Friday")
if week== 6:
    print("Saturday")

                            
                            
                            

                        
                                                                        
                                                                      

                
                                
                                                                
                        
                        
                        
                        
    



