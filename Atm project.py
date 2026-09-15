print("hello welcome to canara bank")
pin=7890
balance=100000
while True :
   a=int(input("enter your pin ="))
   if(a==pin):
      print("your account is successfully login ")
   else:
      print("your password is wrong")
      print("3 attemp is left")
      a=int(input("enter your pin="))
      if a==pin:
         print("your account is login")
      else:
         print("2 attemp is left")
         a=int(input("enter your pin="))
         if a==pin:
            print("your account is login ")
         else:
            print("1 attemp is left")
            a=int(input("enter your pin= "))
            if a==pin:
                continue
            else:
                print("Your account is now block")
                break

   print("1.withdraw cash")
   print("2.deposite")
   print("3.balance check")
   print("4.pin change")
   print("5.exit")
   a=int(input("enter your choice="))
   if a==1:
      d=int(input("enter your amount="))
      p=balance-d
      balance=p
      print("total amount is ",p)
      n=input("Do you want to continue Y/N=")
      if n=="Y":
          continue
      else:
          break
          
   elif a==2:
      x=int(input("enter your amount="))
      p=balance+x
      balance=p
      print("total amount is",balance)
      n=input("Do you want to continue Y/N=")
      if n=="Y":
          continue
      else:
          break

   elif a==3:
      print("your total balance is ",balance)
      n=input("Do you want to continue Y/N=")
      if n=="Y":
          continue
      else:
          break

   elif a==4:
      user_pin=int(input("enter your old pin="))
      if(user_pin==pin):
         newpin=int(input("enter your new pin ="))
         pin=newpin
         print("your new pin is",newpin)
         n=input("Do you want to continue Y/N=")
         if n=="Y":
            continue
         else:
            break
   elif a==5:
      print("exit")
      break
   else:
      print("somrthing wrong")