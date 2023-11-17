class programmer:
    company = "Microsoft"
    def __init__(self , name , product):
        self.name = name
        self.product = product

    def getInfo(self):
        print (f'{self.name} is a {self.company} programmer and he/she works on {self.product}')

harry = programmer("harry","builder")
john = programmer("John", "Windows 10")
john.getInfo()
harry.getInfo()