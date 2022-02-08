from tkinter import *
from tkinter import messagebox
import os
main = Tk()
def add(ID,comname,compadress,comphone,degree,Domain):
	f = open("joboff","r+")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	found = 0
	for i in ch:
		l = i.split("|")[0]
		if l == ID:
			messagebox.showinfo("Message","This job offer ID exists already!")
			found = 1
			break
	if found == 0:
		f = open("joboff","a")
		f.write(ID + "|" + comname + "/" + compadress + "/" + comphone + "|" + degree + "|" + Domain + "\n")
		f.close()
		adminpanel()
def addpanel():
	lis = main.grid_slaves()
	for l in lis:
		l.destroy()
	Label(main,bg="#374a69",text = "Job ID").grid(row = 0 , column = 0)
	e1 = Entry(main)
	e1.grid(row = 0 , column = 1)
	Label(main,bg="#374a69",text = "Company infomations:").grid(row = 1 , column = 0)
	Label(main,bg="#374a69",text = "name:").grid(row = 2 , column = 0)
	e2 = Entry(main)
	e2.grid(row = 2 , column = 1)
	Label(main,bg="#374a69",text = "Adress:").grid(row = 3 , column = 0)
	e3 = Entry(main)
	e3.grid(row = 3 , column = 1)
	Label(main,bg="#374a69",text = "Phone:").grid(row = 4, column = 0)
	e4 = Entry(main)
	e4.grid(row = 4 , column = 1)
	Label(main,bg="#374a69",text = "Requested profile degree:").grid(row = 5, column = 0)
	e5 = Entry(main)
	e5.grid(row = 5 , column = 1)
	Label(main,bg="#374a69",text = "Domain:").grid(row = 6, column = 0)
	e6 = Entry(main)
	e6.grid(row = 6 , column = 1)
	Button(main,text = "Submit",command=lambda: add(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())).grid(row = 7 , column = 0)
	Button(main , text = "Back" , command = adminpanel).grid(row = 7 , column = 1)
def delete(ID):
	f = open("joboff","r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	res = ""
	for i in ch:
		l = i.split("|")[0]
		if not(l == ID):
			res = res + i + "\n"
	f = open("joboff","w")
	f.write(res.strip("\n"))
	f.close()
def deletepanel():
	lis = main.grid_slaves()
	for l in lis:
		l.destroy()
	Label(main,bg="#374a69",text = "Give job offer ID to remove:").grid(row = 0 , column = 0)
	e1 = Entry(main)
	e1.grid(row = 0 , column = 1)
	Button(main , text = "Submit",command=lambda: delete(e1.get())).grid(row = 1 , column = 0)
	Button(main , text = "Back" , command = adminpanel).grid(row = 1 , column = 1)
def update(data):
	lis = main.grid_slaves()
	for l in lis:
		l.destroy()
	adminpanel()
	ch = data.split("-----------------------------\n")
	f = open("joboff","w")
	for i in ch:
		try:
			l = i.split("\n")
			res = l[0].split(":")[1].strip() + "|" + l[2].split(":")[1].strip() + "/" + l[3].split(":")[1].strip() + "/" + l[4].split(":")[1].strip() + "|" + l[5].split(":")[1].strip() + "|" + l[6].split(":")[1].strip()
			f.write(res+"\n")
		except:
			continue
def updatepanel():
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	l = Label(main,bg="#374a69",text="Modify the desired informations then click submit.")
	l.grid(row = 3 , column = 1)
	b1 = Button(main , text = "Submit",command = lambda: update(t.get("1.0",END)))
	b1.grid(row = 4 , column = 2)
	b = Button(main,text = "Close",command=lambda: dis(t,b,l,b1))
	b.grid(row = 4,column = 1)
	f = open("joboff","r")
	ch = f.read().strip()
	ch = ch.split("\n")
	for i in ch:
		t.insert(END,"Job ID: " + i.split("|")[0]+ "\n")
		t.insert(END,"Company informations:\n")
		t.insert(END,"Name: " + i.split("|")[1].split("/")[0]+"\n")
		t.insert(END,"Adress: " + i.split("|")[1].split("/")[1]+"\n")
		t.insert(END,"Phone: " + i.split("|")[1].split("/")[2]+"\n")
		t.insert(END,"Requested degree: " + i.split("|")[2]+ "\n")
		t.insert(END,"Domain: " + i.split("|")[3] + "\n")
		t.insert(END,"-----------------------------\n")
def dis(t,b,l,b1):
	b.destroy()
	l.destroy()
	b1.destroy()
	t.destroy()
def find(ID):
	f = open("joboff","r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	for i in ch:
		if i.split("|")[0] == ID:
			return i.split("|")[1].split("/")[0]
def grep(data):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	adminpanel()
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	Button(main, text = "CLose" , command = cls).grid(row = 3 , column = 3)
	name = find(data)
	f = open("applies","r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	for i in ch:
		try:
			if i.split("|")[1] == data:
				t.insert(END,i.split("|")[0] + " has applied for " + name + "'s job " + i.split("|")[1] + "\n")
				t.insert(END,"-----------------------------\n")
		except:
			continue
def cls():
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	adminpanel()
def specificapp():
	lis = main.grid_slaves()
	for l in lis : 
		l.destroy()
	adminpanel()
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	f = open("joboff","r")
	ch = f.read().strip()
	f.close()
	ch = ch.split("\n")
	for i in ch:
		t.insert(END,"Job ID: " + i.split("|")[0]+ "\n")
		t.insert(END,"Company informations:\n")
		t.insert(END,"Name: " + i.split("|")[1].split("/")[0]+"\n")
		t.insert(END,"Adress: " + i.split("|")[1].split("/")[1]+"\n")
		t.insert(END,"Phone: " + i.split("|")[1].split("/")[2]+"\n")
		t.insert(END,"Requested degree: " + i.split("|")[2]+ "\n")
		t.insert(END,"Domain: " + i.split("|")[3] + "\n")
		t.insert(END,"-----------------------------\n")
	t.config(state = DISABLED)
	Label(main,bg="#374a69", text = "Job ID:").grid(row = 3 , column = 1)
	e1 = Entry(main)
	e1.grid(row = 3 , column = 2)
	Button(main , text = "Submit",command = lambda: grep(e1.get())).grid(row = 3 , column = 3)

def allapp():
	lis = main.grid_slaves()
	for l in lis : 
		l.destroy()
	adminpanel()
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	Button(main, text = "CLose" , command = cls).grid(row = 3 , column = 4)
	f = open("applies","r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	for i in ch:
		try:
			t.insert(END,i.split("|")[0] + " has applied for " + find(i.split("|")[1]) + "'s job " + i.split("|")[1] + "\n")
			t.insert(END,"------------------------\n")
		except:
			continue
def browpanel():
	lis = main.grid_slaves()
	for l in lis : 
		l.destroy()
	adminpanel()
	Label(main,bg="#374a69", text = "choose an option please?").grid(row = 3 , column = 0)
	b = Button(main , text = "All applies",command = allapp)
	b1 = Button(main , text = "Specific job offer",command = specificapp)
	b.grid(row = 4 , column = 0)
	b1.grid(row = 4 , column = 1)
def adminpanel():
	lis = main.grid_slaves()
	for l in lis:
		l.destroy()
	Label(main,bg="#374a69" , text = "Admin").grid(row = 0 , column = 3)
	Button(main , text = "ADD",command=addpanel).grid(row = 1 , column = 0)
	Button(main , text = "DELETE",command=deletepanel).grid(row = 1 , column = 1)
	Button(main , text = "UPDATE",command=updatepanel).grid(row = 2 , column = 0)
	Button(main , text = "BROW",command=browpanel).grid(row = 2, column = 1)
	Button(main , text = "LOGOUT",command=construct).grid(row = 0, column = 4)
def exe(ID,data):
	
	f = open("joboff","r")
	ch = f.read().strip()
	f.close()
	ch = ch.split("\n")
	found = 0 
	for i in ch:
		if i.split("|")[0] == data:
			lis = main.grid_slaves()
			for l in lis:
				l.destroy()
			userpanel(ID)
			t = Text(main,height=30, width=30)
			t.grid(row = 3 , column = 0)
			t.insert(END,"Job ID: " + i.split("|")[0]+ "\n")
			t.insert(END,"Company informations:\n")
			t.insert(END,"Name: " + i.split("|")[1].split("/")[0]+"\n")
			t.insert(END,"Adress: " + i.split("|")[1].split("/")[1]+"\n")
			t.insert(END,"Phone: " + i.split("|")[1].split("/")[2]+"\n")
			t.insert(END,"Requested degree: " + i.split("|")[2]+ "\n")
			Button(main , text = "Close",command = lambda: bck(ID)).grid(row = 3 , column = 1)
			found = 1
			t.config(state = DISABLED)
			break
	if found == 0:
		messagebox.showinfo("Message","Job offer not found!")
	
def bck(ID):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)	
def byID(ID):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	Label(main,bg="#374a69",text = "Give job ID:").grid(row = 0 , column = 0)
	e = Entry(main)
	e.grid(row = 0 , column = 1)
	Button(main,text = "Submit",command=lambda: exe(ID,e.get())).grid(row = 1 , column = 0 )
	Button(main,text = "Back",command=lambda: bck(ID)).grid(row = 1 , column = 1 )
def exd(ID,data):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)
	f = open("joboff", "r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	for i in ch:
		try:
			if i.split("|")[3].strip() == data:
				t.insert(END,"Job ID: " + i.split("|")[0]+ "\n")
				t.insert(END,"Company informations:\n")
				t.insert(END,"Name: " + i.split("|")[1].split("/")[0]+"\n")
				t.insert(END,"Adress: " + i.split("|")[1].split("/")[1]+"\n")
				t.insert(END,"Phone: " + i.split("|")[1].split("/")[2]+"\n")
				t.insert(END,"Requested degree: " + i.split("|")[2]+ "\n")
				t.insert(END,"Domain: " + i.split("|")[3] + "\n")
				t.insert(END,"------------------------\n")
		except:
			continue
	Button(main , text = "Close",command = lambda: bck(ID)).grid(row = 3 , column = 1)

def bydomain(ID):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)
	Label(main,bg="#374a69" , text = "Domain: ").grid(row = 3 , column = 0)
	e1 = Entry(main)
	e1.grid(row = 3 , column = 1)
	Button(main , text = "Submit" , command = lambda: exd(ID,e1.get())).grid(row = 3 , column = 2)
	Button(main,text = "Close" , command= lambda: bck(ID)).grid(row = 4 , column = 1)
def exl(ID,data):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)
	f = open("joboff", "r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	for i in ch:
		try:
			if data in i.split("|")[1].split("/")[1].strip():
				t.insert(END,"Job ID: " + i.split("|")[0]+ "\n")
				t.insert(END,"Company informations:\n")
				t.insert(END,"Name: " + i.split("|")[1].split("/")[0]+"\n")
				t.insert(END,"Adress: " + i.split("|")[1].split("/")[1]+"\n")
				t.insert(END,"Phone: " + i.split("|")[1].split("/")[2]+"\n")
				t.insert(END,"Requested degree: " + i.split("|")[2]+ "\n")
				t.insert(END,"Domain: " + i.split("|")[3] + "\n")
				t.insert(END,"------------------------\n")
		except:
			continue
	Button(main , text = "Close",command = lambda: bck(ID)).grid(row = 3 , column = 1)
def bylocation(ID):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)
	Label(main,bg="#374a69" , text = "location: ").grid(row = 3 , column = 0)
	e1 = Entry(main)
	e1.grid(row = 3 , column = 1)
	Button(main , text = "Submit" , command = lambda: exl(ID,e1.get())).grid(row = 3 , column = 2)
	Button(main,text = "Close" , command= lambda: bck(ID)).grid(row = 4 , column = 1)
def search(ID):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)
	Label(main,bg="#374a69",text = "Choose an option please?").grid(row = 3 , column = 0)
	Button(main , text = "By ID",command=lambda: byID(ID)).grid(row = 4 , column = 0)
	Button(main , text = "By Domain",command=lambda: bydomain(ID)).grid(row = 4 , column = 1)
	Button(main , text = "By location",command=lambda: bylocation(ID)).grid(row = 4 , column = 2)
def confirm(ID,IDC,name,add,tel,deg,skill):
	f = open("usersdata","a")
	f.write(ID + "|" + IDC + "/" + name + "/" + add + "/" + tel + "|" + deg + "|" + skill + "\n")
	f.close()
	userpanel(ID)
def appl(ID,data):
	f = open("applies","r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	if ID+"|"+data in ch:
		messagebox.showinfo("Message","You already applied for that job!")
		return
	f = open("joboff","r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	found = 0
	for i in ch:
		if i.split("|")[0] == data:
			found = 1
			break
	if found == 0:
		messagebox.showinfo("Message","Job offer not found!")
		return 
	f = open("applies","a")
	f.write(ID + "|" + data + "\n")
	f.close()
	f = open("usersdata","r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	found = 0
	for i in ch:
		if i.split("|")[0].strip() == ID:
			messagebox.showinfo("Message","We already have your personal data. Applied successfully!")
			found = 1
			userpanel(ID)
			break
	if found == 0:
		lis = main.grid_slaves()
		for i in lis:
			i.destroy()
		Label(main,bg="#374a69" , text = "We need some data please...").grid(row = 0 , column = 0)
		Label(main,bg="#374a69" , text = "ID card: ").grid(row = 1 , column = 0)
		e1 = Entry(main)
		e1.grid(row = 1 , column = 1)
		Label(main,bg="#374a69", text = "Name: ").grid(row = 2 , column = 0)
		e2 = Entry(main)
		e2.grid(row = 2 , column = 1)
		Label(main,bg="#374a69" , text = "address: ").grid(row = 3 , column = 0)
		e3 = Entry(main)
		e3.grid(row = 3 , column = 1)
		Label(main,bg="#374a69" , text = "Phone number: ").grid(row = 4 , column = 0)
		e4 = Entry(main)
		e4.grid(row = 4 , column = 1)
		Label(main,bg="#374a69" , text = "Degree: ").grid(row = 5 , column = 0)
		e5 = Entry(main)
		e5.grid(row = 5 , column = 1)
		Label(main,bg="#374a69", text = "Skills: ").grid(row = 6 , column = 0)
		e6 = Entry(main)
		e6.grid(row = 6 , column = 1)
		Button(main,text = "Submit",command = lambda: confirm(ID,e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())).grid(row = 7 , column = 0)

def app(ID):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)
	f = open("joboff","r")
	ch = f.read().strip()
	ch = ch.split("\n")
	f.close()
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	for i in ch:
		try:
			t.insert(END,"Job ID: " + i.split("|")[0]+ "\n")
			t.insert(END,"Company informations:\n")
			t.insert(END,"Name: " + i.split("|")[1].split("/")[0]+"\n")
			t.insert(END,"Adress: " + i.split("|")[1].split("/")[1]+"\n")
			t.insert(END,"Phone: " + i.split("|")[1].split("/")[2]+"\n")
			t.insert(END,"Requested degree: " + i.split("|")[2]+ "\n")
			t.insert(END,"Domain: " + i.split("|")[3] + "\n")
			t.insert(END,"-----------------------------\n")
		except:
			continue
	Button(main , text = "Close",command = lambda: bck(ID)).grid(row = 3 , column = 1)
	Label(main,bg="#374a69",text = "Job ID to apply:").grid(row = 4 , column = 0)
	e1 = Entry(main)
	e1.grid(row = 4 , column = 1)
	Button(main , text = "Submit", command = lambda: appl(ID,e1.get())).grid(row = 4 , column = 2)
def upd(ID,data):
	f = open("usersdata","r")
	f1 = open("tmp","w")
	ch = f.read()
	ch = ch.split("\n")
	for i in ch:
		if not(i.split("|")[0] == ID):
			f1.write(i)
	f1.close()
	f.close()
	f1 = open("tmp","a")
	dt = data.split("\n")
	f1.write(ID + "|" + dt[0].split(":")[1].strip() + "/" +dt[1].split(":")[1].strip() + "/" + dt[2].split(":")[1].strip() + "/" + dt[3].split(":")[1].strip() + "|" + dt[4].split(":")[1].strip() + "|" + dt[5].split(":")[1].strip() + "\n" )
	f1.close()
	f = open("tmp","r")
	f1 = open("usersdata" , "w")
	f1.write(f.read())
	f1.close()
	f.close()
	userpanel(ID)
	os.system("del tmp")
def updateinfo(ID):
	lis = main.grid_slaves()
	for i in lis:
		i.destroy()
	userpanel(ID)
	t = Text(main,height=30, width=30)
	t.grid(row = 3 , column = 0)
	l = Label(main,bg="#374a69",text="Modify the desired informations then click submit.")
	l.grid(row = 3 , column = 1)
	b1 = Button(main , text = "Submit",command = lambda: upd(ID,t.get("1.0",END)))
	b1.grid(row = 4 , column = 2)
	b = Button(main,text = "Close",command=lambda: bck(ID))
	b.grid(row = 4,column = 1)
	f = open("usersdata", "r")
	ch = f.read()
	f.close()
	ch = ch.split("\n")
	for i in ch:
		if i.split("|")[0] == ID:
			t.insert(END,"ID Card: " + i.split("|")[1].split("/")[0]+"\n")
			t.insert(END,"Name: " + i.split("|")[1].split("/")[1]+"\n")
			t.insert(END,"Address: " + i.split("|")[1].split("/")[2]+"\n")
			t.insert(END,"Phone number: " + i.split("|")[1].split("/")[3]+"\n")
			t.insert(END, "Degree: " + i.split("|")[2]+"\n")
			t.insert(END,"Skills: " + i.split("|")[3]+"\n")
			break
def userpanel(ID):
	lis = main.grid_slaves()
	for l in lis:
		l.destroy()
	Label(main,bg="#374a69" , text = ID).grid(row = 0 , column = 3)
	Button(main , text = "LOGOUT",command=construct).grid(row = 0, column = 4)
	Button(main , text = "Search a job offer",command=lambda: search(ID)).grid(row = 1 , column = 0)
	Button(main , text = "Apply for a job offer",command=lambda: app(ID)).grid(row = 1 , column = 1)
	Button(main , text = "update informations",command=lambda: updateinfo(ID)).grid(row = 1 , column = 2)
def usertest(a,b):
	if not(a == "" or b == ""):
		f = open("users.txt","r")
		ch = f.read()
		ch = ch.split("\n")
		islogged = 0
		found = 0
		for i in ch:
			l = i.split("|")
			if l[0] == a:
				found = 1
				if l[1].strip() == b:
					islogged = 1 
					messagebox.showinfo("Message","Welcome back "+a+" !")
					if a == "admin":
						adminpanel()
					else:
						userpanel(a)
				else:
					messagebox.showinfo("Message","Wrong password!")
		if found == 0:
					messagebox.showinfo("Message","Wrong Username!")

def login():
	main.config(bg="#374a69")
	lis = main.grid_slaves()
	for l in lis:
		l.destroy()
	Label(main,bg="#374a69", text="Username :").grid(row=0)
	Label(main,bg="#374a69", text="Password :").grid(row=1)
	e1 = Entry(main)
	e2 = Entry(main,show = "*")
	e1.grid(row = 0 , column = 1 )
	e2.grid(row = 1 , column = 1 )
	Button(main, text = "Back",command=construct).grid(row = 10,column = 1)
	Button(main, text = "Submit",command=lambda: usertest(e1.get(),e2.get())).grid(row = 10,column = 0)
def save(user,pas):
	f = open("users.txt","a")
	f.write(user + "|" + pas + "\n")
	construct()
def signup():
	main.config(bg="#374a69")
	lis = main.grid_slaves()
	for l in lis: 
		l.destroy()
	Label(main,bg="#374a69", text="Username :").grid(row=0)
	Label(main,bg="#374a69", text="Password :").grid(row=1)
	e1 = Entry(main)
	e2 = Entry(main,show = "*")
	e1.grid(row = 0 , column = 1 )
	e2.grid(row = 1 , column = 1 )
	Button(main, text = "Back",command=construct).grid(row = 10,column = 1)
	Button(main, text = "Submit",command=lambda: save(e1.get(),e2.get())).grid(row = 10,column = 0)
def exi():
	exit(0)
def construct():
	lis = main.grid_slaves()
	for l in lis: 
		l.destroy()
	main.config(bg="black")
	b = Button(main,text="EXIT",command=exi)
	b.grid(row = 2 , column = 5)
	lab = Label(main,bg="#374a69",text = "Welcome to my project.")
	lab.config(bg='black', fg='blue')
	lab.config(height=3, width=50)
	lab.config(font=("Courier", 20))
	lab.grid(row = 0 , column = 3)
	b2 = Button(main , text = "SIGNUP" , command=signup)
	b2.grid(row = 2 , column = 1)
	b1 = Button(main,text="SIGNIN",command=login)
	b1.grid(row = 2 , column = 3)
construct()
main.mainloop()
