from tkinter import *

calculation = ""
def add_to_calculation(symbol):
    global calculation
    calculation += symbol
    text.delete(1.0 , "end")
    text.insert(1.0 , calculation)

def eval_calculation():
    global calculation
    calculation = str(eval(calculation))
    text.delete(1.0 , "end")
    text.insert(1.0 , calculation)
    # print(calculation)

def clear_screen():
    global calculation
    calculation = ""
    text.delete(1.0 , "end")
    text.insert(1.0 , calculation)


root = Tk()
root.geometry("370x390")
root.title("Calculator")

text = Text(root , height=2 , width= 20 , font = ("Arial" , 24))
text.grid(columnspan=5)

btn1 = Button(root , text = "1" , command= lambda : add_to_calculation("1") , width=5 , font= ("arial") , padx=10 , pady=10)
btn1.grid(row = 2 , column=1)

btn2 = Button(root , text = "2" , command= lambda : add_to_calculation("2") , width=5 , font= ("arial") , padx=10 , pady=10)
btn2.grid(row = 2 , column=2)

btn3 = Button(root , text = "3" , command= lambda : add_to_calculation("3") , width=5 , font= ("arial") , padx=10 , pady=10)
btn3.grid(row = 2 , column=3)

btn4 = Button(root , text = " + " , command= lambda : add_to_calculation(" + ") , width=5 , font= ("arial") , padx=10 , pady=10)
btn4.grid(row = 2 , column=4)

btn5 = Button(root , text = " 4 " , command= lambda : add_to_calculation("4") , width=5 , font= ("arial") , padx=10 , pady=10)
btn5.grid(row = 3 , column=1)

btn6 = Button(root , text = " 5 " , command= lambda : add_to_calculation("5") , width=5 , font= ("arial") , padx=10 , pady=10)
btn6.grid(row = 3 , column=2)

btn7 = Button(root , text = "6" , command= lambda : add_to_calculation("6") , width=5 , font= ("arial") , padx=10 , pady=10)
btn7.grid(row = 3 , column=3)

btn8 = Button(root , text = " - " , command= lambda : add_to_calculation(" - ") , width=5 , font= ("arial") , padx=10 , pady=10)
btn8.grid(row = 3 , column=4)

btn9 = Button(root , text = "7" , command= lambda : add_to_calculation("7") , width=5 , font= ("arial") , padx=10 , pady=10)
btn9.grid(row =  4, column=1)

btn10 = Button(root , text = "8" , command= lambda : add_to_calculation("8") , width=5 , font= ("arial") , padx=10 , pady=10)
btn10.grid(row = 4 , column=2)

btn11 = Button(root , text = "9" , command= lambda : add_to_calculation("9") , width=5 , font= ("arial") , padx=10 , pady=10)
btn11.grid(row = 4 , column=3)

btn12 = Button(root , text = " * " , command= lambda : add_to_calculation(" * ") , width=5 , font= ("arial") , padx=10 , pady=10)
btn12.grid(row = 4 , column=4)

btn13 = Button(root , text = "0" , command= lambda : add_to_calculation("0") , width=5 , font= ("arial") , padx=10 , pady=10)
btn13.grid(row = 5 , column=2)

btn14 = Button(root , text = "(" , command=lambda : add_to_calculation("(") , width=5 , font= ("arial") , padx=10 , pady=10)
btn14.grid(row = 5 , column=1)

btn15 = Button(root , text = ")" , command=lambda : add_to_calculation(")") , width=5 , font= ("arial") , padx=10 , pady=10)
btn15.grid(row = 5 , column=3)

btn16 = Button(root , text = " / " , command= lambda : add_to_calculation(" / ") , width=5 , font= ("arial") , padx=10 , pady=10)
btn16.grid(row = 5 , column=4)

btn17 = Button(root , text = "CLEAR" , command=clear_screen , width= 14 , font= ("arial") , padx=10 , pady=10)
btn17.grid(row = 6 , column=3 , columnspan=3)

btn18 = Button(root , text = " = " , command=eval_calculation , width=13 , font= ("arial") , padx=10 , pady=10)
btn18.grid(row = 6 , column=1 , columnspan=2)

root.mainloop()

