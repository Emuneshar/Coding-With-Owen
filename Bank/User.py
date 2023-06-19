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

    def getLastName(self):
        return self.lastName
    
    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getUserName(self):
        return self.username
    
    def setUserName(self, newUsername):
        self.username = newUsername

    def getPassword(self):
        return self.password
    
    def setPassword(self, newPassword):
        self.password = newPassword

    def getAccountNumber(self):
        return self.accountNumber
    
    def setAccountNumber(self, newAccountNumber):
        self.accountNumber = newAccountNumber

    def getAccountBalance(self):
        return self.accountBalance
    
    def setAccountBalance(self, newAccountBalance):
        self.accountBalance = newAccountBalance

    

    

    
