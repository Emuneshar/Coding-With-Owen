class User:

    # Constructor
    def __init__ (self, firstName, lastName, username, password, accountNumber, accountBalance):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance

    # Getters and Setters

    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    

