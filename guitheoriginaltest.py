from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from io import BytesIO
import smtplib, ssl

def studentlogin():    
    def forenter():
        global info1,info2,info3,info4,info5,info6,info7,info8,info9,a1,a2,a3,a4,a5,a6,a7,a8,a9,con,cur,table,root
        table="students"
        a1=info1.get()
        a2=info2.get()
        a3=info3.get()
        a4=info4.get()
        a5=info5.get()
        a6=info6.get()
        a7=info7.get()
        a8=info8.get()
        a9=info9.get()
        mypass="root"
        mydatabase="original"
        con =pymysql.connect(host="localhost",user="root",password="root",database="original")
        cur=con.cursor()

        insertdata= "insert into "+table+"(userid,password,name,class,registerno,address,fathername,mothername,mobileno) values ('"+a1+"','"+a2+"','"+a3+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"','"+a8+"','"+a9+"')"
        check="SELECT * FROM students WHERE  registerno='"+a5+"'"
        try:
            cur.execute(check)
            con.commit()
            rowcount=cur.rowcount
            print(rowcount)
            #print("Hi")
        except Exception as a:
            print("dai",a)
            
        if(rowcount==0):
            try:
                cur.execute(insertdata)
                con.commit()
                messagebox.showinfo('Success',"your informations added")
            except Exception as a:
                print("error",a)
                messagebox.showinfo('Error',"can't add to database")
        elif(rowcount==1):
            messagebox.showinfo('ERROR',"your register number is already occupied check your register number")
    
        
    
    def newlogin():
        def nexter():
            global openfile,entryof,aa1
            def openfile():
                global openfile,entryof,aa1,filesetter
            
                def call(call,filesetter):
                    print(call)
                    print(filesetter)
                   # global filename,aa1,filesetter              
                    
                    def convertToBinaryData(filesetter):
                        #global filename,aa1
                        #Convert digital data to binary format
                        with open(filesetter, 'rb') as file:
                            blobData = file.read()
                        return blobData
                
                
                    def insertBLOB(aa1, filesetter):
                        #global filenmae,aa1
                        try:                           
                            sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                            #sqliteConnection = sqlite3.connect('SQLite_Python.db')
                            cursor = sqliteConnection.cursor()
                            print("Connected to SQLite")
                            sqlite_insert_blob_query = " UPDATE students  SET photo=%s WHERE registerno=%s"

                            empPhoto = convertToBinaryData(filesetter)
                            #resume = convertToBinaryData(resumeFile)
                            # Convert data into tuple format
                            data_tuple = (empPhoto,aa1)
                            cursor.execute(sqlite_insert_blob_query, (empPhoto,aa1))

                            
                            sqliteConnection.commit()
                            print("Image and file inserted successfully as a BLOB into a table")
                            messagebox.showinfo('Success',"your profile added ")
                            cursor.close()

                        except Exception as error:
                            print("Failed to insert blob data into mysql table", error)
                        finally:
                            if (sqliteConnection):
                                sqliteConnection.close()
                            print("the mysql connection is closed")

                    aa1=entryof.get()
                    print("1-->",aa1)
                    print('2-->',filesetter)
                    insertBLOB(aa1,filesetter)
                    print("2-=>",aa1)
                
                aa1=entryof.get()
                print(aa1)    
                from tkinter.filedialog import askopenfilename
                filesetter=askopenfilename(initialdir ="/",title="select a file",filetypes=(("Template files",".tplate"),("images files",".jpg"),("HTML files", "*.html;*.htm"),("all files","*.*")))
                print(filesetter)
                call(aa1,filesetter)
                


                    
                
            root = Toplevel()
            root.title("upload image")
            root.minsize(width=500,height=500)
            root.geometry("700x600")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#f7ff0f")
            Canvas1.pack(expand=True,fill=BOTH)            
            headingFrame1 = Frame(root,bg="green",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="UPLOAD YOUR PROFILE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.5)

            labelof=Label(root, text="REGISTER NO   :",bg='black',fg='white',font=('Courier',10))
            labelof.place(relx=0.10,rely=0.40)
            entryof=Entry(root)
            entryof.place(relx=0.30,rely=0.40,relwidth=0.60)

            buttonof=Button(root, text=" UPLOAD IMAGE ",bg='black',fg='white',font=('Courier',10),command=openfile)
            buttonof.place(relx=0.40,rely=0.55)
            
##            buttonof=Button(root, text=" EXIT<<< ",bg='black',fg='white',font=('Courier',10),command=root.quit())
##            buttonof.place(relx=0.70,rely=0.55)

            root.mainloop()
    
            
                  
        
    
        messagebox.showinfo('please',"Enter your deatils properly")
        global info1,info2,info3,info4,info5,info6,info7,info8,info9,con,cur,table,root
        
        root=Tk()
        root.title("NEW LOGIN")
        root.minsize(width=600,height=600)
        root.geometry("700x600")
        Canvas1 = Canvas(root)    
        Canvas1.config(bg="#2fddf7")
        Canvas1.pack(expand=True,fill=BOTH)                
        headingFrame1 = Frame(root,bg="blue",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text ="WELCOME TO\n NEW LOGIN SITE", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        labelFrame = Frame(root,bg='black')
        labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)
        
        lbl1=Label(root, text="USER ID       :",bg='black',fg='white',font=('Courier',10))
        lbl1.place(relx=0.10,rely=0.30)
        info1=Entry(root)
        info1.place(relx=0.30,rely=0.30,relwidth=0.62)

        lbl2=Label(root, text="PASSWORD      :",bg='black',fg='white',font=('Courier',10))
        lbl2.place(relx=0.10,rely=0.35)
        info2=Entry(root)
        info2.place(relx=0.30,rely=0.35,relwidth=0.62)

        lbl3=Label(root, text="NAME          :",bg='black',fg='white',font=('Courier',10))
        lbl3.place(relx=0.10,rely=0.40)
        info3=Entry(root)
        info3.place(relx=0.30,rely=0.40,relwidth=0.62)

        lbl4=Label(root, text="CLASS         :",bg='black',fg='white',font=('Courier',10))
        lbl4.place(relx=0.10,rely=0.45)
        info4=Entry(root)
        info4.place(relx=0.30,rely=0.45,relwidth=0.62)

        lbl5=Label(root, text="REGISTER NO   :",bg='black',fg='white',font=('Courier',10))
        lbl5.place(relx=0.10,rely=0.50)
        info5=Entry(root)
        info5.place(relx=0.30,rely=0.50,relwidth=0.62)

        lbl6=Label(root, text="ADDRESS       :",bg='black',fg='white',font=('Courier',10))
        lbl6.place(relx=0.10,rely=0.55)
        info6=Entry(root)
        info6.place(relx=0.30,rely=0.55,relwidth=0.62)

        lbl7=Label(root, text="FATHER'S NAME :",bg='black',fg='white',font=('Courier',10))
        lbl7.place(relx=0.10,rely=0.60)
        info7=Entry(root)
        info7.place(relx=0.30,rely=0.60,relwidth=0.62)

        lbl8=Label(root, text="MOTHER'S NAME :",bg='black',fg='white',font=('Courier',10))
        lbl8.place(relx=0.10,rely=0.65)
        info8=Entry(root)
        info8.place(relx=0.30,rely=0.65,relwidth=0.62)

        upldbtn=Button(root, text=" NEXT>>> ",bg='black',fg='white',font=('Courier',10),command=nexter)
        upldbtn.place(relx=0.60,rely=0.80)

        submitbtn=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=forenter)
        submitbtn.place(relx=0.40,rely=0.80)

        lbl9=Label(root, text="MOBILE NO     :",bg='black',fg='white',font=('Courier',10))
        lbl9.place(relx=0.10,rely=0.70)
        info9=Entry(root)
        info9.place(relx=0.30,rely=0.70,relwidth=0.62)
         


        root.mainloop()
        

        
    def ifcheck():
        def nexte():
            global entryof1,yourentry,passentry,teachentry
            def openfile11():
                global openfile,entryof1,aa1,filesetter
            
                def call(call,filesetter):
                    print(call)
                    print(filesetter)
                   # global filename,aa1,filesetter              
                    
                    def convertToBinaryData(filesetter):
                        #global filename,aa1
                        #Convert digital data to binary format
                        with open(filesetter, 'rb') as file:
                            blobData = file.read()
                        return blobData
                
                
                    def insertBLOB(aa1, filesetter):
                        #global filenmae,aa1
                        try:                           
                            sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                            #sqliteConnection = sqlite3.connect('SQLite_Python.db')
                            cursor = sqliteConnection.cursor()
                            print("Connected to SQLite")
                            sqlite_insert_blob_query = " UPDATE requestbox SET photo=%s WHERE registerno=%s"

                            empPhoto = convertToBinaryData(filesetter)
                            #resume = convertToBinaryData(resumeFile)
                            # Convert data into tuple format
                            data_tuple = (empPhoto,aa1)
                            cursor.execute(sqlite_insert_blob_query, (empPhoto,aa1))

                            
                            sqliteConnection.commit()
                            print("Image and file inserted successfully as a BLOB into a table")
                            messagebox.showinfo('Success',"your profile added please inform your class teacher through mail for his\her approvel")
                            cursor.close()

                        except Exception as error:
                            print("Failed to insert blob data into mysql table", error)
                        finally:
                            if (sqliteConnection):
                                sqliteConnection.close()
                            print("the mysql connection is closed")

                    aa1=entryof1.get()
                    print("1-->",aa1)
                    print('2-->',filesetter)
                    insertBLOB(aa1,filesetter)
                    print("2-=>",aa1)
                
                aa1=entryof1.get()
                print(aa1)    
                from tkinter.filedialog import askopenfilename
                filesetter=askopenfilename(initialdir ="/",title="select a file",filetypes=(("Template files",".tplate"),("images files",".jpg"),("HTML files", "*.html;*.htm"),("all files","*.*")))
                print(filesetter)
                call(aa1,filesetter)
            def sentmail():
                global yourentry,passentry,teachentry,aa1
                send=yourentry.get()
                password=passentry.get()
                teach=teachentry.get()
                
                port = 587  # For starttls
                smtp_server = "smtp.gmail.com"
                sender_email = '%s'%(send)
                receiver_email ='%s'%(teach) 
                password ='%s'%(password)
                message = """\
                Subject: DEAR MAM, I AM YOUR STUDENT OF REGISTERNO:'%s'%(aa1) ,MY BIO-BATA HAS SOME MISATKE/n
                SO I CHANGED IT , PLEASE APPRVE IT MAM , THANK U!          

                This message is sent from python"""
                
                try:                    
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()  # Can be omitted
                        server.starttls(context=context)
                        server.ehlo()  # Can be omitted
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                        messagebox.showinfo('SUCCESS',"REQUEST SENT")
                except Exception as a:
                    messagebox.showinfo('FAILED',"MAIL NOT SENT")
                    print("error",a)
                

                    
            root = Toplevel()
            root.title("upload image")
            root.minsize(width=500,height=500)
            root.geometry("1000x1000")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#6b32f0")
            Canvas1.pack(expand=True,fill=BOTH)            
            headingFrame1 = Frame(root,bg="green",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="UPLOAD YOUR PROFILE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.5)

            labelof1=Label(root, text="REGISTER NO   :",bg='black',fg='white',font=('Courier',10))
            labelof1.place(relx=0.10,rely=0.40)
            entryof1=Entry(root)
            entryof1.place(relx=0.20,rely=0.40,relwidth=0.30)

            buttonof=Button(root, text=" UPLOAD IMAGE ",bg='black',fg='white',font=('Courier',10),command=openfile11)
            buttonof.place(relx=0.55,rely=0.40)

            warninglbl=Label(root,text=" ! ! ! REQUEST YOUR APPROVAL TO YOUR CLASS TEACHER ! ! !",bg='red',fg='white',font=('Courier',13))
            warninglbl.place(relx=0.15,rely=0.50)

            yourmail=Label(root,text="YOUR MAIL ID:",bg='black',fg='white',font=('Courier',10))
            yourmail.place(relx=0.20,rely=0.55)

            password=Label(root,text="PASSWORD    :",bg='black',fg='white',font=('Courier',10))
            password.place(relx=0.20,rely=0.60)

            teachermail=Label(root,text="CLASS TEACHER MAIL ID :",bg='black',fg='white',font=('Courier',10))
            teachermail.place(relx=0.12,rely=0.65)

            yourentry=Entry(root)
            yourentry.place(relx=0.32,rely=0.55,relwidth=0.25)

            passentry=Entry(root)
            bullet="\u2022"
            passentry.config(show=bullet)
            passentry.place(relx=0.32,rely=0.60,relwidth=0.25)

            teachentry=Entry(root)
            teachentry.place(relx=0.32,rely=0.65,relwidth=0.25)

            request=Button(root,text=" REQUEST " ,bg='black',fg='white',font=('Courier',10),command=sentmail)
            request.place(relx=0.65,rely=0.60)
            

                    
        def foreditprofile():
            global infi1,infi2,infi3,infi4,infi5,infi6,infi7,infi8,infi9,con,cur,table,root
            table="requestbox"
            a1=infi1.get()
            a2=infi2.get()
            a3=infi3.get()
            a4=infi4.get()
            a5=infi5.get()
            a6=infi6.get()
            a7=infi7.get()
            a8=infi8.get()
            a9=infi9.get()
            mypass="root"
            mydatabase="original"
            con =pymysql.connect(host="localhost",user="root",password="root",database="original")
            cur=con.cursor()

            insertdata="insert into "+table+"(userid,password,name,class,registerno,address,fathername,mothername,mobileno) values ('"+a1+"','"+a2+"','"+a3+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"','"+a8+"','"+a9+"')"
            try:
                cur.execute(insertdata)
                con.commit()
                messagebox.showinfo('Success',"your profile edit request is added click next button and /n and upload your photo and send mail to your class teacher")
            except Exception as a:
                print("error",a)
                messagebox.showinfo('Error',"can't add to database")
                

        def report():
            messagebox.showinfo('OK',"Your Report has submitted to your staff now you can Change Mark")
            
            global regnoen,nameen,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
            def markquarter():
                global regnoen,nameen,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
                table="studentsq"
                a1=regnoen.get()
                a2=nameen.get()
                q1=qtamilen.get()
                q2=qengen.get()
                q3=qmaten.get()
                q4=qscien.get()
                q5=qsocen.get()
                    
                mypass="root"
                mydatabase="original"
                con =pymysql.connect(host="localhost",user="root",password="root",database="original")
                cur=con.cursor()

                insertdata="UPDATE  "+table+" SET tamil='"+q1+"',english='"+q2+"',maths='"+q3+"',science='"+q4+"',social='"+q5+"' where registerno='"+a1+"'"
                try:
                    cur.execute(insertdata)
                    con.commit()
                    messagebox.showinfo('Success',"Marks are added")
                except Exception as a:
                    print("error",a)
                    messagebox.showinfo('Error',"can't add to database")

            def markhalfer():
                global regnoen,nameon,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
                table="studentsh"
                a1=regnoen.get()
                a2=nameen.get()                
                h6=htamilen.get()
                h7=hengen.get()
                h8=hmaten.get()
                h9=hscien.get()
                h10=hsocen.get()

                mypass="root"
                mydatabase="original"
                con =pymysql.connect(host="localhost",user="root",password="root",database="original")
                cur=con.cursor()

                insertdata="UPDATE  "+table+" SET tamil='"+h6+"',english='"+h7+"',maths='"+h8+"',science='"+h9+"',social='"+h10+"' where registerno='"+a1+"'"
                try:
                    cur.execute(insertdata)
                    con.commit()
                    messagebox.showinfo('Success',"your informations added")
                except Exception as a:
                    print("error",a)
                    messagebox.showinfo('Error',"can't add to database")
                
            def markannua():
                global regnoen,nameon,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
                table="studentsa"
                a1=regnoen.get()
                a2=nameen.get()
                an6=atamilen.get()
                an7=aengen.get()
                an8=amaten.get()
                an9=ascien.get()
                an10=asocen.get()
                mypass="root"
                mydatabase="original"
                con =pymysql.connect(host="localhost",user="root",password="root",database="original")
                cur=con.cursor()
                insertdata="UPDATE  "+table+" SET tamil='"+an6+"',english='"+an7+"',maths='"+an8+"',science='"+an9+"',social='"+an10+"'where registerno='"+a1+"'"
                try:
                    cur.execute(insertdata)
                    con.commit()
                    messagebox.showinfo('Success',"your informations added")
                except Exception as a:
                    print("error",a)
                    messagebox.showinfo('Error',"can't add to database")       

                
            root = Toplevel()
            root.title("staffs information")
            root.minsize(width=400,height=400)
            root.geometry("1100x1100")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#fc2403")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="blue",bd=5)
            headingFrame1.place(relx=0.25,rely=0.03,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="RENTER MARKS", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.18,relwidth=0.9,relheight=0.8)

            regno=Label(root,text="REGISTER NO :",bg='black',fg='white',font=('Courier',10))
            regno.place(relx=0.30,rely=0.21)
            regnoen=Entry(root)
            regnoen.place(relx=0.40,rely=0.21,relwidth=0.22)

            nameno=Label(root,text="NAME        :",bg='black',fg='white',font=('Courier',10))
            nameno.place(relx=0.30,rely=0.25)
            nameen=Entry(root)
            nameen.place(relx=0.40,rely=0.25,relwidth=0.22)

            quarterlylbl=Label(root,text="QUARTERLY EXAM MARKS",bg='black',fg='blue',font=('Courier',15))
            quarterlylbl.place(relx=0.35,rely=0.30)

            qtamil=Label(root,text="TAMIL   :",bg='black',fg='white',font=('Courier',10))
            qtamil.place(relx=0.20,rely=0.34)
            qtamilen=Entry(root)
            qtamilen.place(relx=0.30,rely=0.34,relwidth=0.42)

            qeng=Label(root,text="ENGLISH :",bg='black',fg='white',font=('Courier',10))
            qeng.place(relx=0.20,rely=0.38)
            qengen=Entry(root)
            qengen.place(relx=0.30,rely=0.38,relwidth=0.42)

            qmat=Label(root,text="MATHS   :",bg='black',fg='white',font=('Courier',10))
            qmat.place(relx=0.20,rely=0.42)
            qmaten=Entry(root)
            qmaten.place(relx=0.30,rely=0.42,relwidth=0.42)

            qsci=Label(root,text="SCIENCE :",bg='black',fg='white',font=('Courier',10))
            qsci.place(relx=0.20,rely=0.46)
            qscien=Entry(root)
            qscien.place(relx=0.30,rely=0.46,relwidth=0.42)

            qsoc=Label(root,text="SOCIAL  :",bg='black',fg='white',font=('Courier',10))
            qsoc.place(relx=0.20,rely=0.50)
            qsocen=Entry(root)
            qsocen.place(relx=0.30,rely=0.50,relwidth=0.42)

            qsubmit=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=lambda:markquarter())
            qsubmit.place(relx=0.80,rely=0.42)
            print("submit")


            halferly=Label(root,text="HALFEARLY EXAM MARKS",bg='black',fg='violet',font=('Courier',15))
            halferly.place(relx=0.35,rely=0.54)

            htamil=Label(root,text="TAMIL   :",bg='black',fg='white',font=('Courier',10))
            htamil.place(relx=0.20,rely=0.58)
            htamilen=Entry(root)
            htamilen.place(relx=0.30,rely=0.58,relwidth=0.42)

            heng=Label(root,text="ENGLISH :",bg='black',fg='white',font=('Courier',10))
            heng.place(relx=0.20,rely=0.62)
            hengen=Entry(root)
            hengen.place(relx=0.30,rely=0.62,relwidth=0.42)

            hmat=Label(root,text="MATHS   :",bg='black',fg='white',font=('Courier',10))
            hmat.place(relx=0.20,rely=0.66)
            hmaten=Entry(root)
            hmaten.place(relx=0.30,rely=0.66,relwidth=0.42)

            hsci=Label(root,text="SCIENCE :",bg='black',fg='white',font=('Courier',10))
            hsci.place(relx=0.20,rely=0.70)
            hscien=Entry(root)
            hscien.place(relx=0.30,rely=0.70,relwidth=0.42)

            hsoc=Label(root,text="SOCIAL  :",bg='black',fg='white',font=('Courier',10))
            hsoc.place(relx=0.20,rely=0.74)
            hsocen=Entry(root)
            hsocen.place(relx=0.30,rely=0.74,relwidth=0.42)

            hsubmit=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=lambda:markhalfer())
            hsubmit.place(relx=0.80,rely=0.66)

            annual=Label(root,text="ANNUALY EXAM MARKS",bg='black',fg='red',font=('Courier',15))
            annual.place(relx=0.39,rely=0.77)

            atamil=Label(root,text="TAMIL   :",bg='black',fg='white',font=('Courier',10))
            atamil.place(relx=0.20,rely=0.81)
            atamilen=Entry(root)
            atamilen.place(relx=0.30,rely=0.81,relwidth=0.42)

            aeng=Label(root,text="ENGLISH :",bg='black',fg='white',font=('Courier',10))
            aeng.place(relx=0.20,rely=0.84)
            aengen=Entry(root)
            aengen.place(relx=0.30,rely=0.84,relwidth=0.42)

            amat=Label(root,text="MATHS   :",bg='black',fg='white',font=('Courier',10))
            amat.place(relx=0.20,rely=0.87)
            amaten=Entry(root)
            amaten.place(relx=0.30,rely=0.87,relwidth=0.42)

            asci=Label(root,text="SCIENCE :",bg='black',fg='white',font=('Courier',10))
            asci.place(relx=0.20,rely=0.90)
            ascien=Entry(root)
            ascien.place(relx=0.30,rely=0.90,relwidth=0.42)

            asoc=Label(root,text="SOCIAL  :",bg='black',fg='white',font=('Courier',10))
            asoc.place(relx=0.20,rely=0.93)
            asocen=Entry(root)
            asocen.place(relx=0.30,rely=0.93,relwidth=0.42)

            asubmit=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=lambda:markannua())
            asubmit.place(relx=0.80,rely=0.87)
            

        def seemarks():
            global ent
            def marks():
                global btn
                et=ent.get()                
                my_connect = pymysql.connect(
                host="localhost",
                user="root", 
                passwd="root",
                database="original"
                )
                my_conn = my_connect.cursor()
                ####### end of connection ####
                my_conn.execute("SELECT * FROM studentsq WHERE registerno='"+et+"'")
                name=my_conn.fetchone()
                print(name)

                quarterlylbl=Label(root,text="QUARTERLY EXAM MARKS --->",bg='black',fg='blue',font=('Courier',15))
                quarterlylbl.place(relx=0.10,rely=0.36)
                
                tamil=Label(root,text="TAMIL =",bg='black',fg='white',font=('Courier',13))
                tamil.place(relx=0.45,rely=0.30)
                tamilm=Label(root,text=name[2],bg='black',fg='white',font=('Courier',13))
                tamilm.place(relx=0.54,rely=0.30)

                english=Label(root,text="ENGLISH =",bg='black',fg='white',font=('Courier',13))
                english.place(relx=0.45,rely=0.34)
                englishm=Label(root,text=name[3],bg='black',fg='white',font=('Courier',13))
                englishm.place(relx=0.54,rely=0.34)

                maths=Label(root,text="MATHS =",bg='black',fg='white',font=('Courier',13))
                maths.place(relx=0.45,rely=0.38)
                mathsm=Label(root,text=name[4],bg='black',fg='white',font=('Courier',13))
                mathsm.place(relx=0.54,rely=0.38)

                science=Label(root,text="SCIENCE =",bg='black',fg='white',font=('Courier',13))
                science.place(relx=0.45,rely=0.42)
                sciencem=Label(root,text=name[5],bg='black',fg='white',font=('Courier',13))
                sciencem.place(relx=0.54,rely=0.42)

                social=Label(root,text="SOCIAL =",bg='black',fg='white',font=('Courier',13))
                social.place(relx=0.45,rely=0.46)
                socialm=Label(root,text=name[6],bg='black',fg='white',font=('Courier',13))
                socialm.place(relx=0.54,rely=0.46)

                global btn
                et=ent.get()                
                my_connect = pymysql.connect(
                host="localhost",
                user="root", 
                passwd="root",
                database="original"
                )
                my_conn = my_connect.cursor()
                ####### end of connection ####
                my_conn.execute("SELECT * FROM studentsh WHERE registerno='"+et+"'")
                name=my_conn.fetchone()      

                halferlylbl=Label(root,text="HALFERLY EXAM MARKS --->",bg='black',fg='red',font=('Courier',15))
                halferlylbl.place(relx=0.10,rely=0.64)

                tamilq=Label(root,text="TAMIL =",bg='black',fg='white',font=('Courier',13))
                tamilq.place(relx=0.45,rely=0.56)
                tamilmq=Label(root,text=name[2],bg='black',fg='white',font=('Courier',13))
                tamilmq.place(relx=0.54,rely=0.56)

                englishq=Label(root,text="ENGLISH =",bg='black',fg='white',font=('Courier',13))
                englishq.place(relx=0.45,rely=0.60)
                englishmq=Label(root,text=name[3],bg='black',fg='white',font=('Courier',13))
                englishmq.place(relx=0.54,rely=0.60)

                mathsq=Label(root,text="MATHS =",bg='black',fg='white',font=('Courier',13))
                mathsq.place(relx=0.45,rely=0.64)
                mathsmq=Label(root,text=name[4],bg='black',fg='white',font=('Courier',13))
                mathsmq.place(relx=0.54,rely=0.64)

                scienceq=Label(root,text="SCIENCE =",bg='black',fg='white',font=('Courier',13))
                scienceq.place(relx=0.45,rely=0.68)
                sciencemq=Label(root,text=name[5],bg='black',fg='white',font=('Courier',13))
                sciencemq.place(relx=0.54,rely=0.68)

                socialq=Label(root,text="SOCIAL =",bg='black',fg='white',font=('Courier',13))
                socialq.place(relx=0.45,rely=0.72)
                socialmq=Label(root,text=name[6],bg='black',fg='white',font=('Courier',13))
                socialmq.place(relx=0.54,rely=0.72)

                global btn
                et=ent.get()                
                my_connect = pymysql.connect(
                host="localhost",
                user="root", 
                passwd="root",
                database="original"
                )
                my_conn = my_connect.cursor()
                ####### end of connection ####
                my_conn.execute("SELECT * FROM studentsa WHERE registerno='"+et+"'")
                name=my_conn.fetchone()

                annuallbl=Label(root,text="ANNUAL  EXAM MARKS --->",bg='black',fg='violet',font=('Courier',15))
                annuallbl.place(relx=0.10,rely=0.86)

                tamila=Label(root,text="TAMIL =",bg='black',fg='white',font=('Courier',13))
                tamila.place(relx=0.45,rely=0.78)
                tamilma=Label(root,text=name[2],bg='black',fg='white',font=('Courier',13))
                tamilma.place(relx=0.54,rely=0.78)

                englisha=Label(root,text="ENGLISH =",bg='black',fg='white',font=('Courier',13))
                englisha.place(relx=0.45,rely=0.82)
                englishma=Label(root,text=name[3],bg='black',fg='white',font=('Courier',13))
                englishma.place(relx=0.54,rely=0.82)

                mathsa=Label(root,text="MATHS =",bg='black',fg='white',font=('Courier',13))
                mathsa.place(relx=0.45,rely=0.86)
                mathsma=Label(root,text=name[4],bg='black',fg='white',font=('Courier',13))
                mathsma.place(relx=0.54,rely=0.86)

                sciencea=Label(root,text="SCIENCE =",bg='black',fg='white',font=('Courier',13))
                sciencea.place(relx=0.45,rely=0.90)
                sciencema=Label(root,text=name[5],bg='black',fg='white',font=('Courier',13))
                sciencema.place(relx=0.54,rely=0.90)

                sociala=Label(root,text="SOCIAL =",bg='black',fg='white',font=('Courier',13))
                sociala.place(relx=0.45,rely=0.94)
                socialma=Label(root,text=name[6],bg='black',fg='white',font=('Courier',13))
                socialma.place(relx=0.54,rely=0.94)
                
                issue=Label(root,text="If you have any incorrect marks \n use report button",bg='black',fg='white',font=('Courier',10))
                issue.place(relx=0.71,rely=0.25)
                changemark=Button(root,text=" REPORT ",bg='black',fg='white',font=('Courier',12),command=lambda:report())
                changemark.place(relx=0.78,rely=0.35)

            
                
                
                
            root=Tk()
            root.title("your marks")
            root.minsize(width=600,height=600)
            root.geometry("1100x1100")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#05ffac")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="red",bd=8)
            headingFrame1.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1,text =" YOUR MARKS", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.20,relwidth=0.9,relheight=0.8)

            reg=Label(root,text="REGISTER NO :",bg='black',fg='white',font=('Courier',10))
            reg.place(relx=0.30,rely=0.25)
            ent=Entry(root)
            ent.place(relx=0.40,rely=0.25,relwidth=0.22)
            btn=Button(root,text=" ENTER ",bg='black',fg='white',font=('Courier',10),command=marks)
            btn.place(relx=0.64,rely=0.25)

            
            
            
        def editprofile():
            
            messagebox.showinfo(" WARNING",'If you are going to edit  then you have to edit all your details')
            global infi1,infi2,infi3,infi4,infi5,infi6,infi7,infi8,infi9,con,cur,table,root
            
            root=Tk()
            root.title("NEW LOGIN")
            root.minsize(width=600,height=600)
            root.geometry("700x600")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#028bfa")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="blue",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1,text =" EDIT PROFILE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)
            
            lbl1=Label(root, text="USER ID   :",bg='black',fg='white',font=('Courier',10))
            lbl1.place(relx=0.10,rely=0.30)
            infi1=Entry(root)
            infi1.place(relx=0.30,rely=0.30,relwidth=0.62)

            lbl2=Label(root, text="PASSWORD      :",bg='black',fg='white',font=('Courier',10))
            lbl2.place(relx=0.10,rely=0.35)
            infi2=Entry(root)
            infi2.place(relx=0.30,rely=0.35,relwidth=0.62)

            lbl3=Label(root, text="NAME          :",bg='black',fg='white',font=('Courier',10))
            lbl3.place(relx=0.10,rely=0.40)
            infi3=Entry(root)
            infi3.place(relx=0.30,rely=0.40,relwidth=0.62)

            lbl4=Label(root, text="CLASS         :",bg='black',fg='white',font=('Courier',10))
            lbl4.place(relx=0.10,rely=0.45)
            infi4=Entry(root)
            infi4.place(relx=0.30,rely=0.45,relwidth=0.62)

            lbl5=Label(root, text="REGISTER NO      :",bg='black',fg='white',font=('Courier',10))
            lbl5.place(relx=0.10,rely=0.50)
            infi5=Entry(root)
            infi5.place(relx=0.30,rely=0.50,relwidth=0.62)

            lbl6=Label(root, text="ADDRESS       :",bg='black',fg='white',font=('Courier',10))
            lbl6.place(relx=0.10,rely=0.55)
            infi6=Entry(root)
            infi6.place(relx=0.30,rely=0.55,relwidth=0.62)

            lbl7=Label(root, text="FATHER'S NAME :",bg='black',fg='white',font=('Courier',10))
            lbl7.place(relx=0.10,rely=0.60)
            infi7=Entry(root)
            infi7.place(relx=0.30,rely=0.60,relwidth=0.62)

            lbl8=Label(root, text="MOTHER'S NAME :",bg='black',fg='white',font=('Courier',10))
            lbl8.place(relx=0.10,rely=0.65)
            infi8=Entry(root)
            infi8.place(relx=0.30,rely=0.65,relwidth=0.62)

            lbl9=Label(root, text="MOBILE NO     :",bg='black',fg='white',font=('Courier',10))
            lbl9.place(relx=0.10,rely=0.70)
            infi9=Entry(root)
            infi9.place(relx=0.30,rely=0.70,relwidth=0.62)

            upldbtn=Button(root, text=" NEXT>>> ",bg='black',fg='white',font=('Courier',10),command=nexte)
            upldbtn.place(relx=0.60,rely=0.80)

            submitbtn=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=foreditprofile)
            submitbtn.place(relx=0.40,rely=0.80)

            

        
        import pymysql as mbd
        from tkinter import ttk 
        global info5,a1,a2,con,cur,table,root,a3
        a1=v1.get()
        a2=v2.get()
        a3=v3.get()
##        bb1=info5.get()
        mypass="root"
        mydatabase="original"
        con=pymysql.connect(host="localhost",user="root",password="root",database="original")
        cur=con.cursor()
        table="students"
        check="SELECT * FROM "+table+" WHERE userid='"+a1+"' AND password='"+a2+"' AND registerno='"+a3+"'"
        try:
            cur.execute(check)
            con.commit()
            rowcount=cur.rowcount
            print(rowcount)
            #print("Hi")
        except Exception as a:
            print("dai",a)
            
        if(rowcount==1):
           
            root = Toplevel()
            root.title("students information")
            root.minsize(width=500,height=500)
            root.geometry("1100x1100")
            same=True
            n=1.5
            # Adding a background image
            background_image =Image.open("E:\python\stdbg.jpg")
            [imageSizeWidth, imageSizeHeight] = background_image.size
            newImageSizeWidth = int(imageSizeWidth*n)
            if same:
                newImageSizeHeight = int(imageSizeHeight*n) 
            else:
                newImageSizeHeight = int(imageSizeHeight/n) 
                
            background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(background_image)
            Canvas1 = Canvas(root)
            Canvas1.create_image(300,340,image = img)      
            Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
            Canvas1.pack(expand=True,fill=BOTH)
            headingFrame1 = Frame(root,bg="blue",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="STAFFS DATABASE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)

            
            my_connect = pymysql.connect(
                host="localhost",
                user="root", 
                passwd="root",
                database="original"
                )
            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("SELECT * FROM students WHERE registerno='"+a3+"' AND password='"+a2+"'")
            name=my_conn.fetchone()   
            
            label1=Label(root,text="NAME          :",bg='black',fg='white',font=('Courier',12))
            label1.place(relx=0.46,rely=0.30)          
            labels1=Label(root,text=name[2],bg='black',fg='white',font=('Courier',12))
            labels1.place(relx=0.61,rely=0.30)

            label2=Label(root,text="CLASS         :",bg='black',fg='white',font=('Courier',12))
            label2.place(relx=0.46,rely=0.35)          
            labels2=Label(root,text=name[3],bg='black',fg='white',font=('Courier',12))
            labels2.place(relx=0.61,rely=0.35)

            label3=Label(root,text="REGISTER NO   :",bg='black',fg='white',font=('Courier',12))
            label3.place(relx=0.46,rely=0.40)          
            labels3=Label(root,text=name[4],bg='black',fg='white',font=('Courier',12))
            labels3.place(relx=0.61,rely=0.40)

            label4=Label(root,text="USER ID       :",bg='black',fg='white',font=('Courier',12))
            label4.place(relx=0.46,rely=0.45)          
            labels4=Label(root,text=name[0],bg='black',fg='white',font=('Courier',12))
            labels4.place(relx=0.61,rely=0.45)

            label5=Label(root,text="PASSWORD      :",bg='black',fg='white',font=('Courier',12))
            label5.place(relx=0.46,rely=0.50)          
            labels5=Label(root,text=name[1],bg='black',fg='white',font=('Courier',12))
            labels5.place(relx=0.61,rely=0.50)

            label6=Label(root,text="ADDRESS       :",bg='black',fg='white',font=('Courier',12))
            label6.place(relx=0.46,rely=0.55)          
            labels6=Label(root,text=name[5],bg='black',fg='white',font=('Courier',12))
            labels6.place(relx=0.61,rely=0.55)

            label7=Label(root,text="FATHERNAME    :",bg='black',fg='white',font=('Courier',12))
            label7.place(relx=0.46,rely=0.60)          
            labels7=Label(root,text=name[6],bg='black',fg='white',font=('Courier',12))
            labels7.place(relx=0.61,rely=0.60)

            label8=Label(root,text="MOTHERNAME    :",bg='black',fg='white',font=('Courier',12))
            label8.place(relx=0.46,rely=0.65)          
            labels8=Label(root,text=name[7],bg='black',fg='white',font=('Courier',12))
            labels8.place(relx=0.61,rely=0.65)

            label10=Label(root,text="MOBILE NO     :",bg='black',fg='white',font=('Courier',12))
            label10.place(relx=0.46,rely=0.70)          
            labels10=Label(root,text=name[8],bg='black',fg='white',font=('Courier',12))
            labels10.place(relx=0.61,rely=0.70)

            seemarks=Button(root,text=" SEE MARKS ",bg='black',fg='white',font=('Courier',13),command=seemarks)
            seemarks.place(relx=0.27,rely=0.75)

            editprofile=Button(root,text=" EDIT PROFILE ",bg='black',fg='white',font=('Courier',13),command=editprofile)
            editprofile.place(relx=0.57,rely=0.78)
            
           
            def writeTofile(data, filename):
                global hello
                # Convert binary data to proper format and write it on Hard Disk
                with open(filename, 'wb') as file:
                    file.write(data)
                print("Stored blob data into: ", filename, "\n")
                hello=filename
                print("the global file--->",hello)      
            
            def readBlobData(name):
                global hello
                try:
                    print('name-->',name)
                    sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                    cursor = sqliteConnection.cursor()
                    print("Connected to mysql")

                    sql_fetch_blob_query = """SELECT photo from students where registerno = %s"""
                    cursor.execute(sql_fetch_blob_query, (name,))
                    
                    photo = cursor.fetchone()[0]                  

                    print("Storing employee image and resume on disk \n")
                    photoPath = "C:\\Users\\Hari\\Documents\\students\\" + name + ".png"
                       
                    writeTofile(photo, photoPath)
                    #filename1=writeTofile(hello)
                    print("path-->",hello)
                    w=h=150
                    imgpath=hello
                    ##you can re size the image by changing the value of width and height
                    v = Image.open(imgpath).resize((w,h), Image.ANTIALIAS)
                    logo = ImageTk.PhotoImage(v)

                    w1 = Label(root, image=logo,width = 200, height = 200)
                    w1.place(relx=0.15,rely=0.30)

                    root.mainloop()
                    

                    cursor.close()

                except Exception as error:
                    print("Failed to read blob data from sqlite table", error)
                finally:
                    if (sqliteConnection):
                        sqliteConnection.close()
                        print("sqlite connection is closed")

                        

            print(name[4])    
            readBlobData(name[4])


            root.mainloop()        
                                                                                             
                                                                
        else:                     
            messagebox.showinfo("Not Matching",' Try again')
        root.mainloop()    
    
    
            
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    
    hdfrme1=Label(root,text="USER ID",bg='black', fg='white' )
    hdfrme1.place(relx=0.50,rely=0.28)
    hdfrme2=Label(root,text="PASSWORD",bg='black',fg='white')
    hdfrme2.place(relx=0.50,rely=0.36)
    hdfrme3=Label(root,text="REGISTER NO",bg='black',fg='white')
    hdfrme3.place(relx=0.50,rely=0.44)

    ent1=Entry(root,textvariable=v1)
    ent1.place(relx=0.50,rely=0.32)        
    ent2=Entry(root,textvariable=v2)
    ent2.place(relx=0.50,rely=0.40)
    ent3=Entry(root,textvariable=v3)
    ent3.place(relx=0.50,rely=0.48)
    
    bullet="\u2022"
    ent2.config(show=bullet)
    btns=Button(root,text=" ENTER ",bg='black',fg='white',command=ifcheck)
    btns.place(relx=0.72,rely=0.43)
    btns1=Button(root,text=" NEW LOGIN ",bg='black',fg='white',command=newlogin)
    btns1.place(relx=0.72,rely=0.36)

def staffslogin():
    def forenter1():
            
        global abil1,abil2,abil3,abil4,abil5,abil6,abil7,abil8,abil9,abil10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,con,cur,table,root
        b1=abil1.get()
        b2=abil2.get()
        b3=abil3.get()
        b4=abil4.get()
        b5=abil5.get()
        b6=abil6.get()
        b7=abil7.get()
        b8=abil8.get()
        b9=abil9.get()
        b10=abil10.get()
        
        table="staffs"
        mypass="root"
        mydatabase="original"
        con =pymysql.connect(host="localhost",user="root",password="root",database="original")
        cur=con.cursor()

        insertdata= "insert into "+table+"(userid,password,name,registerno,address,degree,fathername,mothername,mobileno,otherability) values ('"+b1+"','"+b2+"','"+b3+"','"+b4+"','"+b5+"','"+b6+"','"+b7+"','"+b8+"','"+b9+"','"+b10+"')"
        try:
            cur.execute(insertdata)
            con.commit()
            messagebox.showinfo('Success',"your informations added")
        except Exception as a:
            print("error",a)
            messagebox.showinfo('Error',"can't add to database")
            
    def newlogin1():
        def nextbtn():
            global openfile,entryon,aa2
            def openmask():
                global openfile,entryon,aa1,filesetter
            
                def call(call,filesetter):
                    print(call)
                    print(filesetter)
                   # global filename,aa1,filesetter              
                    
                    def convertToBinaryData(filesetter):
                        #global filename,aa1
                        #Convert digital data to binary format
                        with open(filesetter, 'rb') as file:
                            blobData = file.read()
                        return blobData
                
                
                    def insertBLOB(aa1, filesetter):
                        #global filenmae,aa1
                        try:                           
                            sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                            #sqliteConnection = sqlite3.connect('SQLite_Python.db')
                            cursor = sqliteConnection.cursor()
                            print("Connected to SQLite")
                            sqlite_insert_blob_query = " UPDATE  staffs SET photo=%s WHERE registerno=%s"

                            empPhoto = convertToBinaryData(filesetter)
                            #resume = convertToBinaryData(resumeFile)
                            # Convert data into tuple format
                            data_tuple = (empPhoto,aa1)
                            cursor.execute(sqlite_insert_blob_query, (empPhoto,aa1))

                            
                            sqliteConnection.commit()
                            print("Image and file inserted successfully as a BLOB into a table")
                            messagebox.showinfo('Success',"your profile added added")
                            cursor.close()

                        except Exception as error:
                            print("Failed to insert blob data into mysql table", error)
                        finally:
                            if (sqliteConnection):
                                sqliteConnection.close()
                            print("the mysql connection is closed")

                    aa1=entryon.get()
                    print("1-->",aa1)
                    print('2-->',filesetter)
                    insertBLOB(aa1,filesetter)
                    print("2-=>",aa1)
                
                aa1=entryon.get()
                print(aa1)    
                from tkinter.filedialog import askopenfilename
                filesetter=askopenfilename(initialdir ="/",title="select a file",filetypes=(("Template files",".tplate"),("images files",".jpg"),("HTML files", "*.html;*.htm"),("all files","*.*")))
                print(filesetter)
                call(aa1,filesetter)
                
            root = Toplevel()
            root.title("upload image")
            root.minsize(width=500,height=500)
            root.geometry("700x600")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#40ff43")
            Canvas1.pack(expand=True,fill=BOTH)            
            headingFrame1 = Frame(root,bg="green",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="UPLOAD YOUR PROFILE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.5)

            labelon=Label(root, text="REGISTER NO   :",bg='black',fg='white',font=('Courier',10))
            labelon.place(relx=0.10,rely=0.40)
            entryon=Entry(root)
            entryon.place(relx=0.30,rely=0.40,relwidth=0.60)

            buttonof=Button(root, text=" UPLOAD IMAGE ",bg='black',fg='white',font=('Courier',10),command=openmask)
            buttonof.place(relx=0.40,rely=0.55)
            
        messagebox.showinfo('please',"Enter your deatils properly")
        global abil1,abil2,abil3,abil4,abil5,abil6,abil7,abil8,abil9,abil10,con,cur,table,root        
        root=Tk()
        root.title("NEW LOGIN")
        root.minsize(width=600,height=600)
        root.geometry("700x600")
        Canvas1 = Canvas(root)    
        Canvas1.config(bg="#fffb00")
        Canvas1.pack(expand=True,fill=BOTH)                
        headingFrame1 = Frame(root,bg="blue",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text ="WELCOME TO\n NEW LOGIN SITE", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        labelFrame = Frame(root,bg='black')
        labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)
        
        lbl1=Label(root, text="USER ID       :",bg='black',fg='white',font=('Courier',10))
        lbl1.place(relx=0.10,rely=0.30)
        abil1=Entry(root)
        abil1.place(relx=0.30,rely=0.30,relwidth=0.62)

        lbl2=Label(root, text="PASSWORD      :",bg='black',fg='white',font=('Courier',10))
        lbl2.place(relx=0.10,rely=0.35)
        abil2=Entry(root)
        abil2.place(relx=0.30,rely=0.35,relwidth=0.62)

        lbl3=Label(root, text="NAME          :",bg='black',fg='white',font=('Courier',10))
        lbl3.place(relx=0.10,rely=0.40)
        abil3=Entry(root)
        abil3.place(relx=0.30,rely=0.40,relwidth=0.62)

        lbl4=Label(root, text="REGISTER NO   :",bg='black',fg='white',font=('Courier',10))
        lbl4.place(relx=0.10,rely=0.45)
        abil4=Entry(root)
        abil4.place(relx=0.30,rely=0.45,relwidth=0.62)

        lbl5=Label(root, text="ADDRESS       :",bg='black',fg='white',font=('Courier',10))
        lbl5.place(relx=0.10,rely=0.50)
        abil5=Entry(root)
        abil5.place(relx=0.30,rely=0.50,relwidth=0.62)

        lbl6=Label(root, text="DEGREE        :",bg='black',fg='white',font=('Courier',10))
        lbl6.place(relx=0.10,rely=0.55)
        abil6=Entry(root)
        abil6.place(relx=0.30,rely=0.55,relwidth=0.62)

        lbl7=Label(root, text="FATHER'S NAME :",bg='black',fg='white',font=('Courier',10))
        lbl7.place(relx=0.10,rely=0.60)
        abil7=Entry(root)
        abil7.place(relx=0.30,rely=0.60,relwidth=0.62)

        lbl8=Label(root, text="MOTHER'S NAME :",bg='black',fg='white',font=('Courier',10))
        lbl8.place(relx=0.10,rely=0.65)
        abil8=Entry(root)
        abil8.place(relx=0.30,rely=0.65,relwidth=0.62)
                
        lbl9=Label(root, text="MOBILE NO     :",bg='black',fg='white',font=('Courier',10))
        lbl9.place(relx=0.10,rely=0.70)
        abil9=Entry(root)
        abil9.place(relx=0.30,rely=0.70,relwidth=0.62)

        lbl10=Label(root, text="OTHER ABILITY :",bg='black',fg='white',font=('Courier',10))
        lbl10.place(relx=0.10,rely=0.75)
        abil10=Entry(root)
        abil10.place(relx=0.30,rely=0.75,relwidth=0.62)


        upldbtn=Button(root, text=" NEXT>>> ",bg='black',fg='white',font=('Courier',10),command=nextbtn)
        upldbtn.place(relx=0.70,rely=0.85)

        submitbtn=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=forenter1)
        submitbtn.place(relx=0.50,rely=0.85)

        root.mainloop()
        
    def ifcheck1():
        def nexte():
            global entryof1
            def openfile11():
                global openfile,entryof1,aa1,filesetter
            
                def call(call,filesetter):
                    print(call)
                    print(filesetter)
                   # global filename,aa1,filesetter              
                    
                    def convertToBinaryData(filesetter):
                        #global filename,aa1
                        #Convert digital data to binary format
                        with open(filesetter, 'rb') as file:
                            blobData = file.read()
                        return blobData
                
                
                    def insertBLOB(aa1, filesetter):
                        #global filenmae,aa1
                        try:                           
                            sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                            #sqliteConnection = sqlite3.connect('SQLite_Python.db')
                            cursor = sqliteConnection.cursor()
                            print("Connected to SQLite")
                            sqlite_insert_blob_query = " UPDATE  staffs SET photo=%s WHERE registerno=%s"

                            empPhoto = convertToBinaryData(filesetter)
                            #resume = convertToBinaryData(resumeFile)
                            # Convert data into tuple format
                            data_tuple = (empPhoto,aa1)
                            cursor.execute(sqlite_insert_blob_query, (empPhoto,aa1))

                            
                            sqliteConnection.commit()
                            print("Image and file inserted successfully as a BLOB into a table")
                            messagebox.showinfo('Success',"your profile added added")
                            cursor.close()

                        except Exception as error:
                            print("Failed to insert blob data into mysql table", error)
                        finally:
                            if (sqliteConnection):
                                sqliteConnection.close()
                            print("the mysql connection is closed")

                    aa1=entryof1.get()
                    print("1-->",aa1)
                    print('2-->',filesetter)
                    insertBLOB(aa1,filesetter)
                    print("2-=>",aa1)
                
                aa1=entryof1.get()
                print(aa1)    
                from tkinter.filedialog import askopenfilename
                filesetter=askopenfilename(initialdir ="/",title="select a file",filetypes=(("Template files",".tplate"),("images files",".jpg"),("HTML files", "*.html;*.htm"),("all files","*.*")))
                print(filesetter)
                call(aa1,filesetter)
                
                
                    
            root = Toplevel()
            root.title("upload image")
            root.minsize(width=500,height=500)
            root.geometry("700x600")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#6b32f0")
            Canvas1.pack(expand=True,fill=BOTH)            
            headingFrame1 = Frame(root,bg="green",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="UPLOAD YOUR PROFILE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.5)

            labelof1=Label(root, text="REGISTER NO   :",bg='black',fg='white',font=('Courier',10))
            labelof1.place(relx=0.10,rely=0.40)
            entryof1=Entry(root)
            entryof1.place(relx=0.30,rely=0.40,relwidth=0.60)

            buttonof=Button(root, text=" UPLOAD IMAGE ",bg='black',fg='white',font=('Courier',10),command=openfile11)
            buttonof.place(relx=0.40,rely=0.55)
            
        def foreditprofile():
            global infi1,infi2,infi3,infi4,infi5,infi6,infi7,infi8,infi9,infi10,con,cur,table,root
            table="staffs"
            a1=infi1.get()
            a2=infi2.get()
            a3=infi3.get()
            a4=infi4.get()
            a5=infi5.get()
            a6=infi6.get()
            a7=infi7.get()
            a8=infi8.get()
            a9=infi9.get()
            a10=infi10.get()
            
            mypass="root"
            mydatabase="original"
            con =pymysql.connect(host="localhost",user="root",password="root",database="original")
            cur=con.cursor()

            insertdata= "update  "+table+" set userid='"+a1+"', password='"+a2+"', name='"+a3+"',degree='"+a4+"', address='"+a6+"',fathername='"+a7+"', mothername='"+a8+"', mobileno='"+a9+"',otherability='"+a10+"' where registerno='"+a5+"'"
            try:
                cur.execute(insertdata)
                con.commit()
                messagebox.showinfo('Success',"your informations added")
            except Exception as a:
                print("error",a)
                messagebox.showinfo('Error',"can't add to database")
                
        def staffeditprofile():
            messagebox.showinfo(" WARNING",'If you are going to edit  then you have to edit all your details')
            global infi1,infi2,infi3,infi4,infi5,infi6,infi7,infi8,infi9,infi10,con,cur,table,root
            
            root=Tk()
            root.title("NEW LOGIN")
            root.minsize(width=600,height=600)
            root.geometry("700x600")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#028bfa")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="blue",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1,text =" EDIT PROFILE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)
            
            lbl1=Label(root, text="USER ID   :",bg='black',fg='white',font=('Courier',10))
            lbl1.place(relx=0.10,rely=0.30)
            infi1=Entry(root)
            infi1.place(relx=0.30,rely=0.30,relwidth=0.62)

            lbl2=Label(root, text="PASSWORD      :",bg='black',fg='white',font=('Courier',10))
            lbl2.place(relx=0.10,rely=0.35)
            infi2=Entry(root)
            infi2.place(relx=0.30,rely=0.35,relwidth=0.62)

            lbl3=Label(root, text="NAME          :",bg='black',fg='white',font=('Courier',10))
            lbl3.place(relx=0.10,rely=0.40)
            infi3=Entry(root)
            infi3.place(relx=0.30,rely=0.40,relwidth=0.62)

            lbl4=Label(root, text="DEGREE         :",bg='black',fg='white',font=('Courier',10))
            lbl4.place(relx=0.10,rely=0.45)
            infi4=Entry(root)
            infi4.place(relx=0.30,rely=0.45,relwidth=0.62)

            lbl5=Label(root, text="REGISTER NO      :",bg='black',fg='white',font=('Courier',10))
            lbl5.place(relx=0.10,rely=0.50)
            infi5=Entry(root)
            infi5.place(relx=0.30,rely=0.50,relwidth=0.62)

            lbl6=Label(root, text="ADDRESS       :",bg='black',fg='white',font=('Courier',10))
            lbl6.place(relx=0.10,rely=0.55)
            infi6=Entry(root)
            infi6.place(relx=0.30,rely=0.55,relwidth=0.62)

            lbl7=Label(root, text="FATHER'S NAME :",bg='black',fg='white',font=('Courier',10))
            lbl7.place(relx=0.10,rely=0.60)
            infi7=Entry(root)
            infi7.place(relx=0.30,rely=0.60,relwidth=0.62)

            lbl8=Label(root, text="MOTHER'S NAME :",bg='black',fg='white',font=('Courier',10))
            lbl8.place(relx=0.10,rely=0.65)
            infi8=Entry(root)
            infi8.place(relx=0.30,rely=0.65,relwidth=0.62)

            lbl9=Label(root, text="MOBILE NO     :",bg='black',fg='white',font=('Courier',10))
            lbl9.place(relx=0.10,rely=0.70)
            infi9=Entry(root)
            infi9.place(relx=0.30,rely=0.70,relwidth=0.62)

            lbl10=Label(root, text="OTHER ABILITY :",bg='black',fg='white',font=('Courier',10))
            lbl10.place(relx=0.10,rely=0.75)
            infi10=Entry(root)
            infi10.place(relx=0.30,rely=0.75,relwidth=0.62)

            

            upldbtn=Button(root, text=" NEXT>>> ",bg='black',fg='white',font=('Courier',10),command=nexte)
            upldbtn.place(relx=0.60,rely=0.80)

            submitbtn=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=foreditprofile)
            submitbtn.place(relx=0.40,rely=0.80)

        def anupu():
            global yourent,passent,stdent,subent
            send=yourent.get()
            print(send)
            password=passent.get()
            print(password)
            teach=stdent.get()
            print(teach)
            subject=subent.get()
            print(subject)
                
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = '%s'%(send)
            receiver_email ='%s'%(teach) 
            password ='%s'%(password)
            message = '%s'%(subject)
                
            try:
                print('HI')
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)
                    server.ehlo()  # Can be omitted
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                    messagebox.showinfo('SUCCESS',"MAIL SENT")
            except Exception as a:
                print('Hi')
                messagebox.showinfo('FAILED',"MAIL NOT SENT")
                print("error",a)
            
        def approve():
            global regentry
            reg=regentry.get()
            print(reg)
            my_connect = pymysql.connect(
            host="localhost",
            user="root", 
            passwd="root",
            database="original"
            )
            my_conn = my_connect.cursor()
            ####### end of connection ####
            try:
                my_conn.execute("UPDATE students inner join requestbox SET students.userid=requestbox.userid,students.password=requestbox.password,students.name=requestbox.name,students.class=requestbox.class,students.address=requestbox.address,students.fathername=requestbox.fathername,students.mothername=requestbox.mothername,students.mobileno=requestbox.mobileno WHERE students.registerno='"+reg+"'")
                my_connect.commit()
                print("scucces")
                messagebox.showinfo('SCUCCESS',"you approved your studnets information please sent mail to him\her for their updation")
                print(name)
                    
            except Exception as a:
                print("error",a)
                messagebox.showinfo('ERROR',"Failed to approve")

        def notacc():
            global regentry
            reg=regentry.get()
            my_connect = pymysql.connect(
            host="localhost",
            user="root", 
            passwd="root",
            database="original"
            )
            my_conn = my_connect.cursor()
            try:
                my_conn.execute("DELETE  FROM requestbox WHERE registerno='"+reg+"'")
                my_connect.commit()
                print("DELETED")
                messagebox.showinfo('DELETED',"you deleted the student approval please inform through mail for his reapproval")
            except Exception as a:
                print("error",a)
                messagebox.showinfo('FAILED',"faield to delete studnet data")
        def sentapp():
            global yourent,passent,stdent,subent
            root=Tk()
            root.title("send mail")
            root.minsize(width=600,height=600)
            root.geometry("500x500")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#00ff8c")
            Canvas1.pack(expand=True,fill=BOTH)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.18,relwidth=0.9,relheight=0.8)

            headlbl=Label(root,text="SEND MAIL",bg='black',fg='white',font=('Courier',17))
            headlbl.place(relx=0.40,rely=0.10)

            yourmail=Label(root,text="Your mailid   :",bg='black',fg='white',font=('Courier',12))
            yourmail.place(relx=0.15,rely=0.25)

            yourent=Entry(root)
            yourent.place(relx=0.45,rely=0.25,relwidth=0.30)

            password=Label(root,text="Password  :",bg='black',fg='white',font=('Courier',12))
            password.place(relx=0.15,rely=0.35)

            passent=Entry(root)
            passent.place(relx=0.45,rely=0.35,relwidth=0.30)

            stdmail=Label(root,text="Student mailid:",bg='black',fg='white',font=('Courier',12))
            stdmail.place(relx=0.15,rely=0.45)

            stdent=Entry(root)
            stdent.place(relx=0.45,rely=0.45,relwidth=0.30)

            sub=Label(root,text="Subject   :",bg='black',fg='white',font=('Courier',12))
            sub.place(relx=0.15,rely=0.55)

            subent=Entry(root)
            subent.place(relx=0.40,rely=0.55,relwidth=0.30,relheight=0.10)

            sentbtn=Button(root,text=" SENT ",bg='black',fg='white',font=('Courier',12),command=anupu)
            sentbtn.place(relx=0.35,rely=0.80)                
            
        def request():    
                
            def enterrequest():
                global regentry
                a3=regentry.get()
                my_connect = pymysql.connect(
                host="localhost",
                user="root", 
                passwd="root",
                database="original"
                )
                my_conn = my_connect.cursor()
                ####### end of connection ####
                my_conn.execute("SELECT * FROM requestbox WHERE registerno='"+a3+"'")
                name=my_conn.fetchone()
                print(name)
                    
                label1=Label(root,text="NAME          :",bg='black',fg='white',font=('Courier',12))
                label1.place(relx=0.46,rely=0.30)          
                labels1=Label(root,text=name[2],bg='black',fg='white',font=('Courier',12))
                labels1.place(relx=0.61,rely=0.30)

                label2=Label(root,text="CLASS         :",bg='black',fg='white',font=('Courier',12))
                label2.place(relx=0.46,rely=0.35)          
                labels2=Label(root,text=name[3],bg='black',fg='white',font=('Courier',12))
                labels2.place(relx=0.61,rely=0.35)

                label3=Label(root,text="REGISTER NO   :",bg='black',fg='white',font=('Courier',12))
                label3.place(relx=0.46,rely=0.40)          
                labels3=Label(root,text=name[4],bg='black',fg='white',font=('Courier',12))
                labels3.place(relx=0.61,rely=0.40)

                label4=Label(root,text="USER ID       :",bg='black',fg='white',font=('Courier',12))
                label4.place(relx=0.46,rely=0.45)          
                labels4=Label(root,text=name[0],bg='black',fg='white',font=('Courier',12))
                labels4.place(relx=0.61,rely=0.45)

                label5=Label(root,text="PASSWORD      :",bg='black',fg='white',font=('Courier',12))
                label5.place(relx=0.46,rely=0.50)          
                labels5=Label(root,text=name[1],bg='black',fg='white',font=('Courier',12))
                labels5.place(relx=0.61,rely=0.50)

                label6=Label(root,text="ADDRESS       :",bg='black',fg='white',font=('Courier',12))
                label6.place(relx=0.46,rely=0.55)          
                labels6=Label(root,text=name[5],bg='black',fg='white',font=('Courier',12))
                labels6.place(relx=0.61,rely=0.55)

                label7=Label(root,text="FATHERNAME    :",bg='black',fg='white',font=('Courier',12))
                label7.place(relx=0.46,rely=0.60)          
                labels7=Label(root,text=name[6],bg='black',fg='white',font=('Courier',12))
                labels7.place(relx=0.61,rely=0.60)

                label8=Label(root,text="MOTHERNAME    :",bg='black',fg='white',font=('Courier',12))
                label8.place(relx=0.46,rely=0.65)          
                labels8=Label(root,text=name[7],bg='black',fg='white',font=('Courier',12))
                labels8.place(relx=0.61,rely=0.65)

                label10=Label(root,text="MOBILE NO     :",bg='black',fg='white',font=('Courier',12))
                label10.place(relx=0.46,rely=0.70)          
                labels10=Label(root,text=name[8],bg='black',fg='white',font=('Courier',12))
                labels10.place(relx=0.61,rely=0.70)

                accept=Button(root,text= " ACCEPT ",bg='black',fg='white',font=('Courier',12),command=approve)
                accept.place(relx=0.45,rely=0.80)

                reject=Button(root,text=" REJECT ",bg='black',fg='white',font=('Courier',12),command=notacc)
                reject.place(relx=0.65,rely=0.80)

                mailapp=Button(root,text=" SENT MAIL ",bg='black',fg='white',font=('Courier',12),command=sentapp)
                mailapp.place(relx=0.25,rely=0.80)
                

                def writeTofile(data, filename):
                    global hello
                    # Convert binary data to proper format and write it on Hard Disk
                    with open(filename, 'wb') as file:
                        file.write(data)
                    print("Stored blob data into: ", filename, "\n")
                    hello=filename
                    print("the global file--->",hello)      
            
                def readBlobData(name):
                    global hello
                    try:                        
                        print('name-->',name)
                        sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                        cursor = sqliteConnection.cursor()
                        print("Connected to mysql")

                        sql_fetch_blob_query = """SELECT photo from requestbox where registerno = %s"""
                        cursor.execute(sql_fetch_blob_query, (name,))
                        
                        photo = cursor.fetchone()[0]                  

                        print("Storing employee image and resume on disk \n")
                        photoPath = "C:\\Users\\Hari\\Documents\\students\\" + name + ".png"
                           
                        writeTofile(photo, photoPath)
                        #filename1=writeTofile(hello)
                        print("path-->",hello)
                        w=h=150
                        imgpath=hello
                        ##you can re size the image by changing the value of width and height
                        v = Image.open(imgpath).resize((w,h), Image.ANTIALIAS)
                        logo = ImageTk.PhotoImage(v)

                        w1 = Label(root,image=logo,width = 200, height = 200)
                        w1.place(relx=0.15,rely=0.30)

                        root.mainloop()
                
                       

                        cursor.close()

                    except Exception as error:
                        print("Failed to read blob data from sqlite table", error)
                    finally:
                        if (sqliteConnection):
                            sqliteConnection.close()
                            print("sqlite connection is closed")

                        

                print("name--->",name[4])    
                readBlobData(name[4])

                #----
                
            global regentry            
            root=Tk()
            root.title("request approval")
            root.minsize(width=600,height=600)
            root.geometry("1100x1100")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#00ff8c")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="red",bd=5)
            headingFrame1.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1,text =" REQUEST APPROVAL ", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)

            reglbl=Label(root,text=" REGISTERNO :",bg='black',fg='white',font=('Courier',12))
            reglbl.place(relx=0.35,rely=0.21)
            regentry=Entry(root)
            regentry.place(relx=0.50,rely=0.21,relwidth=0.20)

            entbtn=Button(root,text=" ENTER ",bg='black',fg='white',font=('Courier',12),command=enterrequest)
            entbtn.place(relx=0.75,rely=0.21)
                         
            
            
        def entermarkforss():
            global regnoen,nameen,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
            def markquarterly():
                global regnoen,nameen,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
                table="studentsq"
                a1=regnoen.get()
                a2=nameen.get()
                q1=qtamilen.get()
                q2=qengen.get()
                q3=qmaten.get()
                q4=qscien.get()
                q5=qsocen.get()
                
                mypass="root"
                mydatabase="original"
                con =pymysql.connect(host="localhost",user="root",password="root",database="original")
                cur=con.cursor()

                insertdata= "INSERT INTO "+table+"(registerno,name,tamil,english,maths,science,social) values('"+a1+"','"+a2+"','"+q1+"','"+q2+"','"+q3+"','"+q4+"','"+q5+"')"
                try:
                    cur.execute(insertdata)
                    con.commit()
                    messagebox.showinfo('Success',"Marks are added")
                except Exception as a:
                    print("error",a)
                    messagebox.showinfo('Error',"can't add to database")
                    
            def markhalferly():
                global regnoen,nameon,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
                table="studentsh"
                a1=regnoen.get()
                a2=nameen.get()                
                h6=htamilen.get()
                h7=hengen.get()
                h8=hmaten.get()
                h9=hscien.get()
                h10=hsocen.get()

                mypass="root"
                mydatabase="original"
                con =pymysql.connect(host="localhost",user="root",password="root",database="original")
                cur=con.cursor()

                insertdata=" insert into "+table+"(registerno,name,tamil,english,maths,science,social) values('"+a1+"','"+a2+"','"+h6+"','"+h7+"','"+h8+"','"+h9+"','"+h10+"')" 
                try:
                    cur.execute(insertdata)
                    con.commit()
                    messagebox.showinfo('Success',"your informations added")
                except Exception as a:
                    print("error",a)
                    messagebox.showinfo('Error',"can't add to database")

            def markannual():
                global regnoen,nameon,qtamilen,qengen,qmaten,qscien,qsocen,htamilen,hengen,hmaten,hscien,hsocen,atamilen,aengen,amaten,ascien,asocen,con,cur,table,root
                table="studentsa"
                a1=regnoen.get()
                a2=nameen.get()
                an6=atamilen.get()
                an7=aengen.get()
                an8=amaten.get()
                an9=ascien.get()
                an10=asocen.get()

                mypass="root"
                mydatabase="original"
                con =pymysql.connect(host="localhost",user="root",password="root",database="original")
                cur=con.cursor()

                insertdata=" insert into "+table+"(registerno,name,tamil,english,maths,science,social) values('"+a1+"','"+a2+"','"+an6+"','"+an7+"','"+an8+"','"+an9+"','"+an10+"')" 
                try:
                    cur.execute(insertdata)
                    con.commit()
                    messagebox.showinfo('Success',"your informations added")
                except Exception as a:
                    print("error",a)
                    messagebox.showinfo('Error',"can't add to database")       

                
            root = Toplevel()
            root.title("staffs information")
            root.minsize(width=400,height=400)
            root.geometry("1100x1100")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#e32252")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="blue",bd=5)
            headingFrame1.place(relx=0.25,rely=0.03,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="MARKS OF STUDENTS", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.18,relwidth=0.9,relheight=0.8)

            regno=Label(root,text="REGISTER NO :",bg='black',fg='white',font=('Courier',10))
            regno.place(relx=0.30,rely=0.21)
            regnoen=Entry(root)
            regnoen.place(relx=0.40,rely=0.21,relwidth=0.22)

            nameno=Label(root,text="NAME       :",bg='black',fg='white',font=('Courier',10))
            nameno.place(relx=0.30,rely=0.25)
            nameen=Entry(root)
            nameen.place(relx=0.40,rely=0.25,relwidth=0.22)

            quarterlylbl=Label(root,text="QUARTERLY EXAM MARKS",bg='black',fg='blue',font=('Courier',15))
            quarterlylbl.place(relx=0.35,rely=0.30)

            qtamil=Label(root,text="TAMIL  :",bg='black',fg='white',font=('Courier',10))
            qtamil.place(relx=0.20,rely=0.34)
            qtamilen=Entry(root)
            qtamilen.place(relx=0.30,rely=0.34,relwidth=0.42)

            qeng=Label(root,text="ENGLISH :",bg='black',fg='white',font=('Courier',10))
            qeng.place(relx=0.20,rely=0.38)
            qengen=Entry(root)
            qengen.place(relx=0.30,rely=0.38,relwidth=0.42)

            qmat=Label(root,text="MATHS   :",bg='black',fg='white',font=('Courier',10))
            qmat.place(relx=0.20,rely=0.42)
            qmaten=Entry(root)
            qmaten.place(relx=0.30,rely=0.42,relwidth=0.42)

            qsci=Label(root,text="SCIENCE :",bg='black',fg='white',font=('Courier',10))
            qsci.place(relx=0.20,rely=0.46)
            qscien=Entry(root)
            qscien.place(relx=0.30,rely=0.46,relwidth=0.42)

            qsoc=Label(root,text="SOCIAL  :",bg='black',fg='white',font=('Courier',10))
            qsoc.place(relx=0.20,rely=0.50)
            qsocen=Entry(root)
            qsocen.place(relx=0.30,rely=0.50,relwidth=0.42)

            qsubmit=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=markquarterly)
            qsubmit.place(relx=0.80,rely=0.42)
            print("submit")


            halferly=Label(root,text="HALFEARLY EXAM MARKS",bg='black',fg='violet',font=('Courier',15))
            halferly.place(relx=0.35,rely=0.54)

            htamil=Label(root,text="TAMIL  :",bg='black',fg='white',font=('Courier',10))
            htamil.place(relx=0.20,rely=0.58)
            htamilen=Entry(root)
            htamilen.place(relx=0.30,rely=0.58,relwidth=0.42)

            heng=Label(root,text="ENGLISH :",bg='black',fg='white',font=('Courier',10))
            heng.place(relx=0.20,rely=0.62)
            hengen=Entry(root)
            hengen.place(relx=0.30,rely=0.62,relwidth=0.42)

            hmat=Label(root,text="MATHS   :",bg='black',fg='white',font=('Courier',10))
            hmat.place(relx=0.20,rely=0.66)
            hmaten=Entry(root)
            hmaten.place(relx=0.30,rely=0.66,relwidth=0.42)

            hsci=Label(root,text="SCIENCE :",bg='black',fg='white',font=('Courier',10))
            hsci.place(relx=0.20,rely=0.70)
            hscien=Entry(root)
            hscien.place(relx=0.30,rely=0.70,relwidth=0.42)

            hsoc=Label(root,text="SOCIAL  :",bg='black',fg='white',font=('Courier',10))
            hsoc.place(relx=0.20,rely=0.74)
            hsocen=Entry(root)
            hsocen.place(relx=0.30,rely=0.74,relwidth=0.42)

            hsubmit=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=markhalferly)
            hsubmit.place(relx=0.80,rely=0.66)

            annual=Label(root,text="ANNUALY EXAM MARKS",bg='black',fg='red',font=('Courier',15))
            annual.place(relx=0.39,rely=0.77)

            atamil=Label(root,text="TAMIL  :",bg='black',fg='white',font=('Courier',10))
            atamil.place(relx=0.20,rely=0.81)
            atamilen=Entry(root)
            atamilen.place(relx=0.30,rely=0.81,relwidth=0.42)

            aeng=Label(root,text="ENGLISH :",bg='black',fg='white',font=('Courier',10))
            aeng.place(relx=0.20,rely=0.84)
            aengen=Entry(root)
            aengen.place(relx=0.30,rely=0.84,relwidth=0.42)

            amat=Label(root,text="MATHS   :",bg='black',fg='white',font=('Courier',10))
            amat.place(relx=0.20,rely=0.87)
            amaten=Entry(root)
            amaten.place(relx=0.30,rely=0.87,relwidth=0.42)

            asci=Label(root,text="SCIENCE :",bg='black',fg='white',font=('Courier',10))
            asci.place(relx=0.20,rely=0.90)
            ascien=Entry(root)
            ascien.place(relx=0.30,rely=0.90,relwidth=0.42)

            asoc=Label(root,text="SOCIAL  :",bg='black',fg='white',font=('Courier',10))
            asoc.place(relx=0.20,rely=0.93)
            asocen=Entry(root)
            asocen.place(relx=0.30,rely=0.93,relwidth=0.42)

            asubmit=Button(root,text=" SUBMIT ",bg='black',fg='white',font=('Courier',10),command=markannual)
            asubmit.place(relx=0.80,rely=0.87)    
            
            
            
        global a1,a2,a3,con,cur,table,root
        a1=v1.get()
        a2=v2.get()
        a3=v3.get()
        mypass="root"
        mydatabase="original"
        con=pymysql.connect(host="localhost",user="root",password="root",database="original")
        cur=con.cursor()
        table="staffs"
        check="SELECT * FROM "+table+" WHERE userid='"+a1+"' AND password='"+a2+"'"
        try:
            cur.execute(check)
            con.commit()
            rowcount=cur.rowcount
            print(rowcount)
            #print("Hi")
        except Exception as a:
            print("dai",a)

        if(rowcount==1):
            print("hi")
            root = Toplevel()
            root.title("staffs information")
            root.minsize(width=400,height=400)
            root.geometry("1100x1100")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#22e345")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="red",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="STAFFS DATABASE", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)

            my_connect = pymysql.connect(
                host="localhost",
                user="root", 
                passwd="root",
                database="original"
                )
            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("SELECT * FROM staffs WHERE registerno='"+a3+"' AND password='"+a2+"'")
            name=my_conn.fetchone()
           
            print(name)
                        
            label1=Label(root,text="NAME          :",bg='black',fg='white',font=('Courier',12))
            label1.place(relx=0.46,rely=0.30)          
            labels1=Label(root,text=name[2],bg='black',fg='white',font=('Courier',12))
            labels1.place(relx=0.61,rely=0.30)

            label2=Label(root,text="DEGREEE       :",bg='black',fg='white',font=('Courier',12))
            label2.place(relx=0.46,rely=0.35)          
            labels2=Label(root,text=name[5],bg='black',fg='white',font=('Courier',12))
            labels2.place(relx=0.61,rely=0.35)

            label3=Label(root,text="REGISTER NO   :",bg='black',fg='white',font=('Courier',12))
            label3.place(relx=0.46,rely=0.40)          
            labels3=Label(root,text=name[3],bg='black',fg='white',font=('Courier',12))
            labels3.place(relx=0.61,rely=0.40)

            label4=Label(root,text="USER ID       :",bg='black',fg='white',font=('Courier',12))
            label4.place(relx=0.46,rely=0.45)          
            labels4=Label(root,text=name[0],bg='black',fg='white',font=('Courier',12))
            labels4.place(relx=0.61,rely=0.45)

            label5=Label(root,text="PASSWORD      :",bg='black',fg='white',font=('Courier',12))
            label5.place(relx=0.46,rely=0.50)          
            labels5=Label(root,text=name[1],bg='black',fg='white',font=('Courier',12))
            labels5.place(relx=0.61,rely=0.50)

            label6=Label(root,text="ADDRESS       :",bg='black',fg='white',font=('Courier',12))
            label6.place(relx=0.46,rely=0.55)          
            labels6=Label(root,text=name[4],bg='black',fg='white',font=('Courier',12))
            labels6.place(relx=0.61,rely=0.55)

            label7=Label(root,text="FATHERNAME    :",bg='black',fg='white',font=('Courier',12))
            label7.place(relx=0.46,rely=0.60)          
            labels7=Label(root,text=name[6],bg='black',fg='white',font=('Courier',12))
            labels7.place(relx=0.61,rely=0.60)

            label8=Label(root,text="MOTHERNAME    :",bg='black',fg='white',font=('Courier',12))
            label8.place(relx=0.46,rely=0.65)          
            labels8=Label(root,text=name[7],bg='black',fg='white',font=('Courier',12))
            labels8.place(relx=0.61,rely=0.65)

            label9=Label(root,text="MOBILE NO     :",bg='black',fg='white',font=('Courier',12))
            label9.place(relx=0.46,rely=0.70)          
            labels9=Label(root,text=name[8],bg='black',fg='white',font=('Courier',12))
            labels9.place(relx=0.61,rely=0.70)

            label10=Label(root,text="OTHER ABLTITY :",bg='black',fg='white',font=('Courier',12))
            label10.place(relx=0.46,rely=0.75)          
            labels10=Label(root,text=name[9],bg='black',fg='white',font=('Courier',12))
            labels10.place(relx=0.61,rely=0.75)

            seemarks=Button(root,text=" ENTER MARKS FOR STUDENTS ",bg='black',fg='white',font=('Courier',13),command=entermarkforss)
            seemarks.place(relx=0.15,rely=0.78)

            editprofile=Button(root,text=" EDIT PROFILE ",bg='black',fg='white',font=('Courier',13),command=staffeditprofile)
            editprofile.place(relx=0.57,rely=0.82)

            request=Button(root,text=" REQUEST APPROVAL ",bg='black',fg='white',font=('Courier',12),command=request)
            request.place(relx=0.17,rely=0.85)

            def writeTofile(data, filename):
                global hello
                # Convert binary data to proper format and write it on Hard Disk
                with open(filename, 'wb') as file:
                    file.write(data)
                print("Stored blob data into: ", filename, "\n")
                hello=filename
                print("the global file--->",hello)      
            
            def readBlobData(name):
                global hello
                try:
                    print('name-->',name)
                    sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                    cursor = sqliteConnection.cursor()
                    print("Connected to mysql")

                    sql_fetch_blob_query = """SELECT photo from staffs where registerno = %s"""
                    cursor.execute(sql_fetch_blob_query, (name,))
                    
                    photo = cursor.fetchone()[0]                  

                    print("Storing your image and resume on disk \n")
                    photoPath = "C:\\Users\\Hari\\Documents\\staffs\\" + name + ".png"
                       
                    writeTofile(photo, photoPath)
                    #filename1=writeTofile(hello)
                    print("path-->",hello)
                    w=h=150
                    imgpath=hello
                    ##you can re size the image by changing the value of width and height
                    v = Image.open(imgpath).resize((w,h), Image.ANTIALIAS)
                    logo = ImageTk.PhotoImage(v)

                    w1 = Label(root, image=logo,width = 200, height = 200)
                    w1.place(relx=0.15,rely=0.30)

##                    explanation = """hello !!!! python """
##
##                    w2 = Label(root,justify=LEFT,padx = 10,text=explanation)
##                    w2.pack(side="left")
                    root.mainloop()
                    
                   
##                labelFrame = Frame(root,bg='black')
##                labelFrame.place(relx=0.20,rely=0.50,relwidth=0.2,relheight=0.2)
                    
                    #w1.place(relx=0.20,rely=0.30,relwidth=0.2,relheight=0.2)
                   

                    cursor.close()

                except Exception as error:
                    print("Failed to read blob data from mysql table", error)
                finally:
                    if (sqliteConnection):
                        sqliteConnection.close()
                        print("mysql connection is closed")

                        

            print(name[3])    
            readBlobData(name[3])


            root.mainloop()        


            
        else:
            messagebox.showinfo("Not Matching",' Try again')
            
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    
    hdfrme1=Label(root,text="USER ID",bg='black', fg='white' )
    hdfrme1.place(relx=0.50,rely=0.54)
    hdfrme2=Label(root,text="PASSWORD",bg='black',fg='white')
    hdfrme2.place(relx=0.50,rely=0.62)
    hdfrme3=Label(root,text="REGISTER NO",bg='black',fg='white')
    hdfrme3.place(relx=0.50,rely=0.70)

    ent1=Entry(root,textvariable=v1)
    ent1.place(relx=0.50,rely=0.58)        
    ent2=Entry(root,textvariable=v2)
    ent2.place(relx=0.50,rely=0.66)
    ent3=Entry(root,textvariable=v3)
    ent3.place(relx=0.50,rely=0.74)
    
    bullet="\u2022"
    ent2.config(show=bullet)
    btns=Button(root,text=" ENTER ",bg='black',fg='white',command=ifcheck1)
    btns.place(relx=0.72,rely=0.63)
    btns1=Button(root,text=" NEW LOGIN ",bg='black',fg='white',command=newlogin1)
    btns1.place(relx=0.72,rely=0.56)
    
def principallogin():
    def ifcheck1():
        global a1,a2,con,cur,table,root,ent1
        a1=v1.get()
        a2=v2.get()
        print(a1)
        print(a2)
        mypass="root"
        mydatabase="original"
        con=pymysql.connect(host="localhost",user="root",password="root",database="original")
        cur=con.cursor()
        table="principal"
        check="SELECT * FROM "+table+" WHERE userid='"+a1+"' AND password='"+a2+"'"
        print(a1)
        print(a2)
        try:
            cur.execute(check)
            con.commit()
            rowcount=cur.rowcount
            print(rowcount)
            #print("Hi")
        except Exception as a:
            print("dai",a)

        if(rowcount==1):
            root = Toplevel()
            root.title("the headmaster")
            root.minsize(width=400,height=400)
            root.geometry("1200x1200")
            Canvas1 = Canvas(root)    
            Canvas1.config(bg="#49cbf2")
            Canvas1.pack(expand=True,fill=BOTH)                
            headingFrame1 = Frame(root,bg="red",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            headingLabel = Label(headingFrame1, text="THE HEADMASTER", bg='black', fg='white', font=('Courier',15))
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.7)

            my_connect = pymysql.connect(
                host="localhost",
                user="root", 
                passwd="root",
                database="original"
                )
            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("SELECT * FROM  principal where userid='"+a1+"' AND password='"+a2+"'")
            name=my_conn.fetchone()

            label1=Label(root,text="NAME          :",bg='black',fg='white',font=('Courier',12))
            label1.place(relx=0.36,rely=0.30)          
            labels1=Label(root,text=name[2],bg='black',fg='white',font=('Courier',12))
            labels1.place(relx=0.48,rely=0.30)

            label2=Label(root,text="DEGREEE       :",bg='black',fg='white',font=('Courier',12))
            label2.place(relx=0.36,rely=0.35)          
            labels2=Label(root,text=name[5],bg='black',fg='white',font=('Courier',12))
            labels2.place(relx=0.48,rely=0.35)

            label3=Label(root,text="REGISTER NO   :",bg='black',fg='white',font=('Courier',12))
            label3.place(relx=0.36,rely=0.40)          
            labels3=Label(root,text=name[3],bg='black',fg='white',font=('Courier',12))
            labels3.place(relx=0.48,rely=0.40)

            label4=Label(root,text="USER ID       :",bg='black',fg='white',font=('Courier',12))
            label4.place(relx=0.36,rely=0.45)          
            labels4=Label(root,text=name[0],bg='black',fg='white',font=('Courier',12))
            labels4.place(relx=0.48,rely=0.45)

            label5=Label(root,text="PASSWORD      :",bg='black',fg='white',font=('Courier',12))
            label5.place(relx=0.36,rely=0.50)          
            labels5=Label(root,text=name[1],bg='black',fg='white',font=('Courier',12))
            labels5.place(relx=0.48,rely=0.50)

            label6=Label(root,text="ADDRESS       :",bg='black',fg='white',font=('Courier',12))
            label6.place(relx=0.36,rely=0.55)          
            labels6=Label(root,text=name[4],bg='black',fg='white',font=('Courier',12))
            labels6.place(relx=0.48,rely=0.55)

            label7=Label(root,text="FATHERNAME    :",bg='black',fg='white',font=('Courier',12))
            label7.place(relx=0.36,rely=0.60)          
            labels7=Label(root,text=name[6],bg='black',fg='white',font=('Courier',12))
            labels7.place(relx=0.48,rely=0.60)

            label8=Label(root,text="MOTHERNAME    :",bg='black',fg='white',font=('Courier',12))
            label8.place(relx=0.36,rely=0.65)          
            labels8=Label(root,text=name[7],bg='black',fg='white',font=('Courier',12))
            labels8.place(relx=0.48,rely=0.65)

            def writeTofile(data, filename):
                global hello
                # Convert binary data to proper format and write it on Hard Disk
                with open(filename, 'wb') as file:
                    file.write(data)
                print("Stored blob data into: ", filename, "\n")
                hello=filename
                print("the global file--->",hello)      
            
            def readBlobData(name):
                global hello
                try:
                    print('name-->',name)
                    sqliteConnection =pymysql.connect(host="localhost",user="root",password="root",database="original")
                    cursor = sqliteConnection.cursor()
                    print("Connected to mysql")

                    sql_fetch_blob_query = """SELECT photo from principal where userid = %s"""
                    cursor.execute(sql_fetch_blob_query, (name,))
                    
                    photo = cursor.fetchone()[0]                  

                    print("Storing your image and resume on disk \n")
                    photoPath = "C:\\Users\\Hari\\Documents\\principal\\" + name + ".png"
                       
                    writeTofile(photo, photoPath)
                    #filename1=writeTofile(hello)
                    print("path-->",hello)
                    w=h=150
                    imgpath=hello
                    ##you can re size the image by changing the value of width and height
                    v = Image.open(imgpath).resize((w,h), Image.ANTIALIAS)
                    logo = ImageTk.PhotoImage(v)

                    w1 = Label(root, image=logo,width = 200, height = 200)
                    w1.place(relx=0.15,rely=0.30)

##                    explanation = """hello !!!! python """
##
##                    w2 = Label(root,justify=LEFT,padx = 10,text=explanation)
##                    w2.pack(side="left")
                    root.mainloop()
                    
                   
##                labelFrame = Frame(root,bg='black')
##                labelFrame.place(relx=0.20,rely=0.50,relwidth=0.2,relheight=0.2)
                    
                    #w1.place(relx=0.20,rely=0.30,relwidth=0.2,relheight=0.2)
                   

                    cursor.close()

                except Exception as error:
                    print("Failed to read blob data from mysql table", error)
                finally:
                    if (sqliteConnection):
                        sqliteConnection.close()
                        print("mysql connection is closed")

                        

            print(name[0])    
            readBlobData(name[0])
                

            
            
        else:
            messagebox.showinfo("Not Matching",' Try again')

            
    v1=StringVar()
    v2=StringVar()
    hdfrme1=Label(root,text="USER ID",bg='black', fg='white' )
    hdfrme1.place(relx=0.50,rely=0.80)
    hdfrme2=Label(root,text="PASSWORD",bg='black',fg='white')
    hdfrme2.place(relx=0.50,rely=0.88)

    ent1=Entry(root,textvariable=v1)  
    ent1.place(relx=0.50,rely=0.84)
        
    ent2=Entry(root,textvariable=v2)
    ent2.place(relx=0.50,rely=0.92)
    bullet="\u2022"
    ent2.config(show=bullet)
    btns=Button(root,text=" ENTER ",bg='black',fg='white',command=ifcheck1)
    btns.place(relx=0.72,rely=0.83)
    
    

            
        
    


root = Tk()
root.title("school database")
root.minsize(width=400,height=400)
root.geometry("700x600")

same=True
n=1.5
# Adding a background image
background_image =Image.open("E:\python\original.png")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#00f7ff",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="WELCOMEW TO\n SCHOOL DATABASE", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#student Button
btn1=Button(root,text="  STUDENT LOGIN  ",bg="red",fg="white",command=studentlogin)
btn1.place(relx=0.27,rely=0.33)

btn2=Button(root,text="  STAFFS LOGIN   ",bg="#FFBB00",fg="black",command=staffslogin)
btn2.place(relx=0.27,rely=0.54)

btn2=Button(root,text=" PRINCIPAL LOGIN ",bg="#40ff79",fg="black",command=principallogin)
btn2.place(relx=0.27,rely=0.80)

root.mainloop()
