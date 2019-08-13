class Users():
     def __init__(self, Fname, Lname, DOB):
         self.Fname = Fname
         self.Lname = Lname
         self.DOB = DOB
         self.loginAt = 0

     def dateBirth(self):
         return(self.Fname + " date of birth is " + self.DOB)

     def user_desc(self):
         return("Welcome " + self.Fname + " to our website. Please confirm on the below data" + '\n' + "First Name: " + self.Fname + "\n" + "Last Name: " +self.Lname + "\n" + "Date of Birth: "+self.DOB)

     def increment_login(self):
         self.loginAt += 1
         login = "Login attempts " + str(self.loginAt)
         print(login)

     def reset_login(self):
         self.loginAt = 0




my_user = Users("Afeef" , "Khateeb", "30/7/1991")
print(my_user.dateBirth())
print(my_user.user_desc())
my_user.increment_login()
my_user.increment_login()
my_user.increment_login()
my_user.increment_login()
my_user.increment_login()
my_user.increment_login()
my_user.reset_login()
my_user.increment_login()
my_user.increment_login()
my_user.increment_login()
