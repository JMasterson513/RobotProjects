#user = input("Enter your name: ")
user = raw_input("Enter your name: ")

class Lab():

    def name(n='student'):
        print('Welcome ' + n)

L = Lab()

L.name(user)

