
import random
from tkinter import *
import tkinter.messagebox as msg
import tkinter as tk
from tkvideo import tkvideo

class gachaimpact:
    def __init__(self,gui,header):
        self.gui = gui
        self.gui.geometry('1025x576')
        self.gui.title(header)
        self.gui.resizable(0,0)
        self.main_screen()
    
    def main_screen(self):
        
        self.bg = PhotoImage(file ="genshinmain.png")
        self.b_main = Label(window, image = self.bg, )
        self.b_main.place(anchor = 'center', relx= 0.5, rely = 0.5)
        
        
        self.lgn= Button(text='Login',bg= "yellow",fg='black',height= '2',width= '20',font=('courier new',12,'bold'),command = self.login)
        self.lgn.place(x=430, y=400)
        self.rgs= Button(text='Register',bg = 'yellow',fg='black',height= '2',width= '20',font=('courier new',12,'bold'),command = self.register)
        self.rgs.place(x=430, y=470)
    
    def login(self):
        
        self.lgn.destroy()
        self.rgs.destroy()
        
        self.entryEmail = Entry(window, width=30)
        self.entryEmail.place(x=427, y= 250)
        self.entryEmail.insert(0, 'Enter Your Email...')
        self.entryEmail.bind('<FocusIn>', self.on_entry_click)
        self.entryEmail.bind('<FocusOut>', self.on_focusout)
        self.entryEmail.config(fg = 'grey')
        
        
        self.entryPass = Entry(window,width=30)
        self.entryPass.place(x=427, y= 290)
        self.entryPass.insert(0, 'Enter Your Password...')
        self.entryPass.bind('<FocusIn>', self.on_entry_click2)
        self.entryPass.bind('<FocusOut>', self.on_focusout2)
        self.entryPass.config(fg = 'grey')
        self.check = IntVar()
        self.showPass = Checkbutton(window, text = "Show Password", variable=self.check,command=self.open_password).place(x=465, y=320)
        self.showPass
        self.btnlogin = Button(window, text="Login", bg= 'lightgreen',fg='black',font=('courier new',12,'bold'),command=self.do_login).place(x=415, y=370)
        
        self.btnCancel = Button(window, text="Cancel", bg='pink',fg='black',font=('courier new',12,'bold'), command=self.main_screen).place(x=550, y=370)
    
    def on_entry_click(self,entry):
    
        if self.entryEmail.get() == 'Enter Your Email...':
            self.entryEmail.delete(0, "end") # delete all the text in the entry
            self.entryEmail.insert(0, '') #Insert blank for user input
            self.entryEmail.config(fg = 'black')
    def on_focusout(self,entry):
        if self.entryEmail.get() == '':
            self.entryEmail.insert(0, 'Enter Your Email...')
            self.entryEmail.config(fg = 'grey')
    
    def on_entry_click2(self,entry):
    
        if  self.entryPass.get() == 'Enter Your Password...':
            self.entryPass.delete(0, "end") # delete all the text in the entry
            self.entryPass.insert(0, '') #Insert blank for user input
            self.entryPass.config(fg = 'black',show='*')
    def on_focusout2(self,entry):
        if  self.entryPass.get() == '':
            self.entryPass.insert(0, 'Enter Your Password...')
            self.entryPass.config(fg = 'grey')
    
    def on_entry_click3(self,entry):
        if self.entryUserName.get() == 'Enter Your Username...':
            self.entryUserName.delete(0, "end") # delete all the text in the entry
            self.entryUserName.insert(0, '') #Insert blank for user input
            self.entryUserName.config(fg = 'black')
    def on_focusout3(self,entry):
        if self.entryUserName.get() == '':
            self.entryUserName.insert(0, 'Enter Your Username...')
            self.entryUserName.config(fg = 'grey')
    
    def register(self):
        
        self.lgn.destroy()
        self.rgs.destroy()
        self.entryUserName = Entry(window, width=30)
        self.entryUserName.place(x=427, y= 210)
        self.entryUserName.insert(0, 'Enter Your Username...')
        self.entryUserName.bind('<FocusIn>', self.on_entry_click3)
        self.entryUserName.bind('<FocusOut>', self.on_focusout3)
        self.entryUserName.config(fg = 'grey')
        self.entryEmail = Entry(window, width=30)
        self.entryEmail.place(x=427, y= 250)
        self.entryEmail.insert(0, 'Enter Your Email...')
        self.entryEmail.bind('<FocusIn>', self.on_entry_click)
        self.entryEmail.bind('<FocusOut>', self.on_focusout)
        self.entryEmail.config(fg = 'grey')
        
        self.entryPass = Entry(window,width=30)
        self.entryPass.place(x=427, y= 290)
        self.entryPass.insert(0, 'Enter Your Password...')
        self.entryPass.bind('<FocusIn>', self.on_entry_click2)
        self.entryPass.bind('<FocusOut>', self.on_focusout2)
        self.entryPass.config(fg = 'grey')
        self.check = IntVar()
        self.showPass = Checkbutton(window, text = "Show Password", variable=self.check,command=self.open_password).place(x=465, y=320)
        self.showPass
        self.btnlogin = Button(window, text="Register", bg= 'lightgreen',fg='black',font=('courier new',12,'bold'),command=self.register_user).place(x=415, y=370)
        
        self.btnCancel = Button(window, text="Cancel", bg='pink',fg='black',font=('courier new',12,'bold'), command=self.main_screen).place(x=550, y=370)
        

    def register_user(self):
        get_name = self.entryUserName.get()
        get_email = self.entryEmail.get()
        get_password = self.entryPass.get()
        if get_name == 'Enter Your Username...':
            msg.showerror('Registry Failed',"Username Can't be Empty",parent=self.gui)
            self.delete_uname()
        elif get_name == "":
            msg.showerror('Registry Failed',"Username Can't be Empty",parent=self.gui)
            self.delete_uname()
        elif get_email == 'Enter Your Email...':
            msg.showerror('Registry Failed',"Email Can't be Empty",parent=self.gui)
            self.delete_uname()
        elif len(get_email) >0 and len(get_email) <=15:
            msg.showerror('Registry Failed','Email Is Too Short',parent=self.gui)
            self.delete_email()
        elif get_email == "":
            msg.showerror('Registry Failed',"Email Can't be Empty!",parent=self.gui)
            self.delete_email()
        elif "@gmail.com" not in get_email:
            msg.showerror("Registry Failed",'Please Include the Domain (@gmail.com)!',parent=self.gui)
            self.delete_email()
        elif " " in get_email:
            msg.showerror("Registry Failed",'Email Address Must Not Use Spaces!',parent=self.gui)
            self.delete_email()
        elif get_password == "":
            msg.showerror('Registry Failed',"Password Can't be Empty!",parent=self.gui)
            self.delete_pass()
        elif get_password == 'Enter Your Password...':
            msg.showerror('Registry Failed',"Password Can't be Empty!",parent=self.gui)
            self.delete_pass()
        elif len(get_password)  <=8 and len(get_password) >0:
            msg.showerror('Registry Failed','Password Is Too Short!',parent=self.gui)
            self.delete_pass()
            

        else :
            file = open('database.txt','a')
            file.write("\n"+get_name+","+get_email+","+get_password)
            file.close()
            self.entryUserName.delete(0,END)
            self.entryEmail.delete(0,END)
            self.entryPass.delete(0,END)
        
            msg.showinfo('Registry Successed','Registry Success, Please Login on the Main Menu!',parent=self.gui)
            self.main_screen()
        
    
    def do_login(self):
        get_useremail = self.entryEmail.get()
        get_password = self.entryPass.get()
        sukses = False
        file = open('database.txt','r')
        
        for i in file :
            name,email,password = i.split(",")
            password = password.strip()
            if get_useremail == email and get_password == password:
                sukses = True
                break
        if (sukses):
            msg.showinfo("Login Success","Welcome to Gacha Impact %s"%(name),parent=self.gui)
            self.wishscr()
            return 
        elif get_useremail == '' or get_password == '':
            msg.showwarning("Login Failed","Email or Password Can't be Empty",parent=self.gui)
            self.entryEmail.focus_set()
        else :
            msg.showerror('Login Failed','Wrong Email or Password ',parent=self.gui)
            self.delete_data()
    
    def temp_text(self):
        self.entryEmail.delete(0,END)
        
    def delete_data(self):
        self.entryEmail.delete(0,END)
        self.entryPass.delete(0,END)
        self.entryEmail.focus_set()

    def delete_uname(self): 
        self.entryPass.focus_set()
        self.entryEmail.focus_set()
        self.entryUserName.delete(0,END)
        self.entryUserName.focus_set()
    
    def delete_email(self):
        self.entryEmail.delete(0,END)
        self.entryPass.focus_set()
        self.entryUserName.focus_set()
        self.entryEmail.focus_set()

    def delete_pass(self):
        self.entryPass.delete(0,END)
        self.entryUserName.focus_set()
        self.entryEmail.focus_set()
        self.entryPass.focus_set()
   
    def open_password(self):
        Show = self.check.get()
        
        if Show == 1:
            self.entryPass['show']=''
        else :
            self.entryPass['show']='*'
    
    def wishscr(self):
        
        self.img = PhotoImage(file= "gbanner.png")
        self.a_main = Label(window, image = self.img)
        self.a_main.place(anchor = 'center', relx= 0.5, rely = 0.5)
        self.label1 = Label(window, text ='Try to Get the 5 Stars Character!!',bg= 'light blue',fg='black',font=('courier new',18,'bold'),width= 60,height=3)
        self.label1.place(x=300,y=0)
        self.wishbtn = Button(text='WISH',bg = 'white',fg='black',height= '2',width= '40',font=('courier new',12,'bold'),command = self.pull)
        self.wishbtn.place(x=600,y=520)
        self.lgoutbtn = Button(text='Logout',bg = 'white',fg='black',height= '2',width= '40',font=('courier new',12,'bold'),command = self.main_screen)
        self.lgoutbtn.place(x=20,y=520)
        self.video_label.destroy()

    def pull(self):
        self.charlist = [1,2,3,4,5,6,7]
        self.freq = 1,1,2,8,8,8,8

        self.wish = random.choices(self.charlist,self.freq)
        
        if self.wish == [1]:
            self.a_main.destroy()
            self.wishbtn.destroy()
            self.lgoutbtn.destroy() 
            self.label1.destroy()            
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo("Ayaka.mp4", self.video_label, loop = 0, size = (1025, 576))
            self.player.play()
            self.backbtn = Button(text='Back',bg = 'white',fg='black',height= '1',width= '20',font=('courier new',12,'bold'),command=self.wishscr).place(x=800, y=540)
            
        elif self.wish == [2]:
            self.a_main.destroy()
            self.wishbtn.destroy()
            self.lgoutbtn.destroy()
            self.label1.destroy()            
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo("Kamisato.mp4", self.video_label, loop = 0, size = (1025, 576))
            self.player.play()
            self.backbtn = Button(text='Back',bg = 'white',fg='black',height= '1',width= '20',font=('courier new',12,'bold'),command=self.wishscr).place(x=800, y=540)
        
        elif self.wish == [3]:
            self.a_main.destroy()
            self.wishbtn.destroy()
            self.lgoutbtn.destroy()
            self.label1.destroy()             
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo("Keqing.mp4", self.video_label, loop = 0, size = (1025, 576))
            self.player.play()
            self.backbtn = Button(text='Back',bg = 'white',fg='black',height= '1',width= '20',font=('courier new',12,'bold'),command=self.wishscr).place(x=800, y=540)
        
        elif self.wish == [4]:
            self.a_main.destroy()
            self.wishbtn.destroy()
            self.lgoutbtn.destroy() 
            self.label1.destroy()            
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo("Rosaria.mp4", self.video_label, loop = 0, size = (1025, 576))
            self.player.play()
            self.backbtn = Button(text='Back',bg = 'white',fg='black',height= '1',width= '20',font=('courier new',12,'bold'),command=self.wishscr).place(x=800, y=540)
        
        elif self.wish == [5]:
            self.a_main.destroy()
            self.wishbtn.destroy()
            self.lgoutbtn.destroy() 
            self.label1.destroy()            
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo("Razor.mp4", self.video_label, loop = 0, size = (1025, 576))
            self.player.play()
            self.backbtn = Button(text='Back',bg = 'white',fg='black',height= '1',width= '20',font=('courier new',12,'bold'),command=self.wishscr).place(x=800, y=540)
        
        elif self.wish == [6]:
            self.a_main.destroy()
            self.wishbtn.destroy()
            self.lgoutbtn.destroy()
            self.label1.destroy()             
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo("Sayu.mp4", self.video_label, loop = 0, size = (1025, 576))
            self.player.play()
            self.backbtn = Button(text='Back',bg = 'white',fg='black',height= '1',width= '20',font=('courier new',12,'bold'),command=self.wishscr).place(x=800, y=540)
        else :
            self.a_main.destroy()
            self.wishbtn.destroy()
            self.lgoutbtn.destroy()
            self.label1.destroy()             
            self.video_label = Label(window)
            self.video_label.pack()
            self.player = tkvideo("Bennett.mp4", self.video_label, loop = 0, size = (1025, 576))
            self.player.play()
            self.backbtn = Button(text='Back',bg = 'white',fg='black',height= '1',width= '20',font=('courier new',12,'bold'),command=self.wishscr).place(x=800, y=540)

if __name__ == '__main__':
    global window
    window = Tk()
    logo = PhotoImage(file="logo genshin.png")
    window.iconphoto(True,logo)
    start = gachaimpact(window,"Gacha Impact Game")
    window.mainloop()