class Users():
	def __init__(self, Fname, Lname, DOB):
		self.Fname = Fname
		self.Lname = Lname
		self.DOB = DOB
	def dateBirth(self):
		return(self.Fname + " date of birth is " + self.DOB)

	def user_desc(self):
		return("Welcome " + self.Fname + " to our website. Please confirm on the below data" + '\n' + "First Name: " + self.Fname + "\n" + "Last Name: " +self.Lname + "\n" + "Date of Birth: "+self.DOB)

class Admin(Users):
    def __init__(self, Fname, Lname, DOB):
        super().__init__(Fname, Lname, DOB)
        self.Fname = Fname
        self.Lname = Lname
        self.DOB = DOB
        self.can_add_post = "can add post"
        self.can_ban_user = "can ban user"
        self.can_delete_post = "can delete post"
    def show_privialges(self):
        message = "Admin user: " + self.can_ban_user + self.can_add_post + self.can_delete_post
        return(message)

#my_user = Users("Afeef" , "Khateeb", "30/7/1991")
Admin_user = Admin("Afeef" , "Khateeb", "30/7/1991")
print(Admin_user.user_desc())
print(Admin_user.show_privialges())
# print(my_user.dateBirth())
# print(my_user.user_desc())
