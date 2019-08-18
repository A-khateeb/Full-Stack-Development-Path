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
        self.can_add_post = "Add post"
        self.can_ban_user = "Ban user"
        self.can_delete_post = "Delete post"
    def show_privialges(self):
        message = "Admin user can: " + "\n"+self.can_ban_user + "\n"+self.can_add_post + "\n"+self.can_delete_post
        return(message)
