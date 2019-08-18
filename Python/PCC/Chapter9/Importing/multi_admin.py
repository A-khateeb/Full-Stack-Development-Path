from multi_user import Users
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
