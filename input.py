import yagmail

user = input("Please enter your gmail account: ")
psw = input("Please enter your gmail password: ")
username = ("'"+user+"'")
password = ("'"+psw+"'")

yagmail.register(username, password)
yag = yagmail.SMTP(username)

print("User registred")

reciver = input("Please enter the reciver: ")
sub = input("Please enter the subject: ")
con = input("Please enter the contents: ")
reciverTO = ("'"+reciver+"'")
subjectTO = ("'"+sub+"'")
contentsTO= ("'"+con+"'")

yag.send(to = reciverTO, subject = subjectTO, contents = contentsTO)

print("Email sent")