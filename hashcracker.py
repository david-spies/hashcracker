import hashlib
import time
from tkinter import font
import tkinter as tk
from tkinter import *
from tkinter import filedialog

root = tk.Tk()
root.title('Hash Cracker')
root.geometry("620x400+620+220")
root.configure(background='#dedcdc')
root.iconbitmap('icons/pyc.ico')
root.grid_columnconfigure(0, weight=1)


heading = Label(root, text="                        ", font=("", 20, "bold"), bg="steelblue").grid(column=1, row=0, padx=80, pady=2) 

Label(root, text="☐☐☐ Hash Cracker ☐☐☐", font=('Courier', 10), fg="green", bg="#dedcdc").grid(column=1, row=0, padx=4, pady=2)

# instructions
instructions = tk.Label(root, text=" Enter a SHA string & decrypt the hash ", font=('Courier', 10), relief=SUNKEN, anchor=CENTER)
instructions.grid(column=1, row=1, padx=52, pady=4)

def removeInfo1(event):
    pass_sha.delete(0, 'end') # left mouse click clears entry box info 
    return None

def removeInfo2(event):    
    wordlist.delete(0, 'end') # left mouse click clears entry box info
    return None

data1 = StringVar()
pass_sha = Entry(root, textvariable=data1, font=('Courier', 10), width=64)
pass_sha.grid(column=1, row=2, padx=52, pady=8)
pass_sha.insert(0, 'Enter Hash: ') # enter secure hash algorithm string
pass_sha.bind('<Button-1>', removeInfo1)

data2 = StringVar()
wordlist = Entry(root, textvariable=data2, font=('Courier', 10), width=64)
wordlist.grid(column=1, row=3, padx=52, pady=8)
wordlist.insert(1, 'Enter Wordlist Location: ') # enter location to wordlist
wordlist.bind('<Button-1>', removeInfo2)


def get_data_256():
    pass_sha = data1.get()
    wordlist = data2.get()
        
    # Counts the number of decrypt attempts
    counter = 1
        
    try:  # try / except block to handle exceptions        
        pass_file = open(wordlist, 'r') # reads wordlist file                

    except:   # if incorrect file loctaion entered
        print('In except block')
        textbox = Label(root, text='File Not Found', font=('arial', 10), fg='red', bd=4, relief=RAISED, anchor=CENTER)
        textbox.grid(column=1, row=5, padx=4, pady=2)  

    for password in pass_file:
            hash_obj = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
            start = time.time()
            print('Trying password %d ------> %s ' % (counter, password.strip()))            
            counter += 1
            end = time.time()
            t_time = end - start
            day = time.strftime('%A')
            time_zone = time.strftime('%Z')
            
        
            if hash_obj == pass_sha:            
                textbox = Label(root, text=('Password Found! Password is : %s ' % password), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=6, pady=2)
                textbox = Label(root, text=('Total Running Time : ', t_time, 'seconds'), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=7, pady=2)
                textbox = Label(root, text=(time_zone + ' ' + day), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=8, pady=2)
                time.sleep(3)
                break

    else:
        textbox = Label(root, text=('Password Not Found'), font=('arial', 10), fg='red', bd=4, relief=SUNKEN, anchor=CENTER)
        textbox.grid(column=1, row=5)


def get_data_384():
    pass_sha = data1.get()
    wordlist = data2.get()
        
    # Counts the number of decrypt attempts
    counter = 1
        
    try:  # try / except block to handle exceptions        
        pass_file = open(wordlist, 'r') # reads wordlist file                

    except:   # if incorrect file loctaion entered
        print('In except block')
        textbox = Label(root, text='File Not Found', font=('arial', 10), fg='red', bd=4, relief=RAISED, anchor=CENTER)
        textbox.grid(column=1, row=5, padx=4, pady=2)  

    for password in pass_file:
            hash_obj = hashlib.sha384(password.strip().encode('utf-8')).hexdigest()
            start = time.time()
            print('Trying password %d ------> %s ' % (counter, password.strip()))            
            counter += 1
            end = time.time()
            t_time = end - start
            day = time.strftime('%A')
            time_zone = time.strftime('%Z')
            
        
            if hash_obj == pass_sha:            
                textbox = Label(root, text=('Password Found! Password is : %s ' % password), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=6, pady=2)
                textbox = Label(root, text=('Total Running Time : ', t_time, 'seconds'), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=7, pady=2)
                textbox = Label(root, text=(time_zone + ' ' + day), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=8, pady=2)
                time.sleep(3)
                break

    else:
        textbox = Label(root, text=('Password Not Found'), font=('arial', 10), fg='red', bd=4, relief=SUNKEN, anchor=CENTER)
        textbox.grid(column=1, row=5)


def get_data_512():
    pass_sha = data1.get()
    wordlist = data2.get()
        
    # Counts the number of decrypt attempts
    counter = 1
        
    try:  # try / except block to handle exceptions        
        pass_file = open(wordlist, 'r') # reads wordlist file                

    except:   # if incorrect file loctaion entered
        print('In except block')
        textbox = Label(root, text='File Not Found', font=('arial', 10), fg='red', bd=4, relief=RAISED, anchor=CENTER)
        textbox.grid(column=1, row=5, padx=4, pady=2)  

    for password in pass_file:
            hash_obj = hashlib.sha512(password.strip().encode('utf-8')).hexdigest()
            start = time.time()
            print('Trying password %d ------> %s ' % (counter, password.strip()))            
            counter += 1
            end = time.time()
            t_time = end - start
            day = time.strftime('%A')
            time_zone = time.strftime('%Z')
            
        
            if hash_obj == pass_sha:            
                textbox = Label(root, text=('Password Found! Password is : %s ' % password), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=6, pady=2)
                textbox = Label(root, text=('Total Running Time : ', t_time, 'seconds'), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=7, pady=2)
                textbox = Label(root, text=(time_zone + ' ' + day), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
                textbox.grid(column=1, row=8, pady=2)
                time.sleep(3)
                break

    else:
        textbox = Label(root, text=('Password Not Found'), font=('arial', 10), fg='red', bd=4, relief=SUNKEN, anchor=CENTER)
        textbox.grid(column=1, row=5)
  

frame = LabelFrame(root, text="", relief=RAISED, padx=8, pady=4, bg='#bbbbbb')
frame.grid(column=1, row=4, padx=2, pady=2)

button1 = tk.Button(frame, text="Decrypt sha256", font=('gigi', 10), fg="green", command=get_data_256)
button1.config()
button1.grid(column=1, row=4, padx=2, pady=2)

button2 = tk.Button(frame, text="Decrypt sha384", font=('gigi', 10), fg="green", command=get_data_384)
button2.config()
button2.grid(column=2, row=4, padx=2, pady=2)

button3 = tk.Button(frame, text="Decrypt sha512", font=('gigi', 10), fg="green", command=get_data_512)
button3.config()
button3.grid(column=3, row=4, padx=2, pady=2)

status = Label(root, text='Hash Cracker: David Spies', font=('Courier', 9), bd=1, relief=SUNKEN, anchor=CENTER)
status.grid(column=1, row=9, padx=4, pady=40) 
                
root.mainloop()
