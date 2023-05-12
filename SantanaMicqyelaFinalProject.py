'''
Sandwhich maker app
Micqyela Santana-Perez
The purpose of this program is to order a sandwhich.
'''

from tkinter import *

#create instance
sandwhich = Tk()
#size the window
sandwhich.geometry("500x400")
#set background image define
bg = PhotoImage(file='C:/Users/micqy/OneDrive/Desktop/FinalProject/sandwhich_photo.png')
#create label
bg_label = Label(sandwhich, image=bg)
bg_label.place(x=0,y=0)
#name window
sandwhich.title("Sandwhich Time!")
#create a frame
first_frame = Frame(sandwhich)
first_frame.pack(pady=20)



#function for start button
def start_order():
    window=Tk()
    window.title("Customize Sandwhich")
    window.geometry('400x400')
  
 
    # for scrolling vertically
    yscrollbar = Scrollbar(window)
    yscrollbar.pack(side = RIGHT, fill = Y)
    
    label = Label(window,
              text = "Select all ingredients :  ",
              font = ("Times New Roman", 10), 
              padx = 10, pady = 10)
    label.pack()
    list = Listbox(window, selectmode = "multiple", 
               yscrollcommand = yscrollbar.set)


# Widget expands horizontally and 
# vertically by assigning both to
# fill option
    list.pack(padx = 10, pady = 10,
         expand = FALSE, fill = "both")
  
    x =["White Bread", "Wheat Bread", "Ham", "Turkey", "Bacon",
    "Chicken", "Lettuce", "Tomato", "Onion", "Green Peppers",
    "American Cheese", "Provolone Cheese", "Mayo", "Mustard", "Ranch"]
  
    for each_item in range(len(x)):
      
        list.insert(END, x[each_item])
        list.itemconfig(each_item, bg = "green")
  
    # Attach listbox to vertical scrollbar
    yscrollbar.config(command = list.yview)

    def submit():
        print("You have ordered: ")
        print(list.curselection())

     #create submit button
    submitButton = Button(window, text="Submit", command = submit)
    submitButton.pack()

    window.mainloop()
    


#create order button
StartOrderBtn = Button(sandwhich, text="Start a order", command=start_order) 
StartOrderBtn.pack()


#exit button
endBtn = Button(sandwhich, text='Exit', command= sandwhich.destroy)
endBtn.pack()


#execute
sandwhich.mainloop()