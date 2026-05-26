from services import (
    BranchSales,
    WeeklySales,
    ProductPrice,
    ProductPopularity,
    SalesRevenue,
    MenuHandler
)


class Admin:
    admin_created = False  

    def __init__(self, username, password):
        if not Admin.admin_created:
            self.username = username
            self.password = password
            Admin.admin_created = True
        else:
            print("Admin account already exists!")

    def logon(self):
        entered_user = input("Enter username: ")
        entered_pass = input("Enter password: ")

        if entered_user == self.username and entered_pass == self.password:
            print("Login successful!\n")
            menu = MenuHandler()
            menu.showOptions()
        else:
            print("Incorrect username or password.")


if __name__ == "__main__":
    admin = Admin("Sampath", "12345")
    admin.logon()
