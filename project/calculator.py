from tkinter import *

def butten1():
    text.config(state= NORMAL)
    text.insert(END, "1")
    text.config(state= DISABLED)
def butten2():
    text.config(state= NORMAL)
    text.insert(END, "2")
    text.config(state= DISABLED)
def butten3():
    text.config(state= NORMAL)
    text.insert(END, "3")
    text.config(state= DISABLED)
def butten4():
    text.config(state= NORMAL)
    text.insert(END, "4")
    text.config(state= DISABLED)
def butten5():
    text.config(state= NORMAL)
    text.insert(END, "5")
    text.config(state= DISABLED)
def butten6():
    text.config(state= NORMAL)
    text.insert(END, "6")
    text.config(state= DISABLED)
def butten7():
    text.config(state= NORMAL)
    text.insert(END, "7")
    text.config(state= DISABLED)
def butten8():
    text.config(state= NORMAL)
    text.insert(END, "8")
    text.config(state= DISABLED)
def butten9():
    text.config(state= NORMAL)
    text.insert(END, "9")
    text.config(state= DISABLED)
def butten0():
    text.config(state= NORMAL)
    text.insert(END, "0")
    text.config(state= DISABLED)
def buttenPlus():
    text.config(state= NORMAL)
    text.insert(END, "+")
    text.config(state= DISABLED)
def buttenMinus():
    text.config(state= NORMAL)
    text.insert(END, "-")
    text.config(state= DISABLED)
def buttenMulti():
    text.config(state= NORMAL)
    text.insert(END, "*")
    text.config(state= DISABLED)
def buttenDiv():
    text.config(state= NORMAL)
    text.insert(END, "/")
    text.config(state= DISABLED)
def buttenLeft():
    text.config(state= NORMAL)
    text.insert(END, "(")
    text.config(state= DISABLED)
def buttenRight():
    text.config(state= NORMAL)
    text.insert(END, ")")
    text.config(state= DISABLED)
def buttenEq():
    text.config(state= NORMAL)
    num = text.get(0.0, END)
    text.delete(1.0, END)
    num = num[:-1]
    allowedCharacters = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','(',')','.']
    valid = [i in allowedCharacters for i in num]
    if all(valid) == True:
        num = eval(num)
        text.insert(END,str(num))
        text.config(state= DISABLED)
    else:
        print("error")
        text.insert(END, "Error")
        text.config(state= DISABLED)
def buttenCC():
    text.config(state= NORMAL)
    text.delete(1.0, END)
    text.config(state= DISABLED)
def buttenDot():
    text.config(state= NORMAL)
    text.insert(END, ".")
    text.config(state= DISABLED)
def buttenDel():
    text.config(state= NORMAL)
    length = len(text.get(0.0, END))
    length -= 2
    length = "1." + str(length)
    text.delete(str(length), END)
    text.config(state= DISABLED)

window = Tk()

window.title("Calculator")
window.geometry("320x400")

#icon = PhotoImage(file="project\\img\\x.gif")
#window.iconphoto(True,icon)
window.config(background='#000')

text = Text(window, wrap="none",font=('Times New Roman',13,'bold'))
text.place(x=20, y=60)
text.config(width="30")
text.config(height="2")
#text.insert(INSERT,"test")
text.config(state= DISABLED)


btn1 = Button(window, text="1", command = butten1)
btn1.place(x=15, y=110)
btn1.config(font=("Helvetica", 18))
btn1.config(width="3")
btn1.config(height="1")

btn2 = Button(window, text="2", command = butten2)
btn2.place(x=75, y=110)
btn2.config(font=("Helvetica", 18))
btn2.config(width="3")
btn2.config(height="1")

btn3 = Button(window, text="3", command = butten3)
btn3.place(x=135, y=110)
btn3.config(font=("Helvetica", 18))
btn3.config(width="3")
btn3.config(height="1")

btn4 = Button(window, text="4", command = butten4)
btn4.place(x=15, y=170)
btn4.config(font=("Helvetica", 18))
btn4.config(width="3")
btn4.config(height="1")

btn5 = Button(window, text="5", command = butten5)
btn5.place(x=75, y=170)
btn5.config(font=("Helvetica", 18))
btn5.config(width="3")
btn5.config(height="1")

btn6 = Button(window, text="6", command = butten6)
btn6.place(x=135, y=170)
btn6.config(font=("Helvetica", 18))
btn6.config(width="3")
btn6.config(height="1")

btn7 = Button(window, text="7", command = butten7)
btn7.place(x=15, y=230)
btn7.config(font=("Helvetica", 18))
btn7.config(width="3")
btn7.config(height="1")

btn8 = Button(window, text="8", command = butten8)
btn8.place(x=75, y=230)
btn8.config(font=("Helvetica", 18))
btn8.config(width="3")
btn8.config(height="1")

btn9 = Button(window, text="9", command = butten9)
btn9.place(x=135, y=230)
btn9.config(font=("Helvetica", 18))
btn9.config(width="3")
btn9.config(height="1")

btn0 = Button(window, text="0", command = butten0)
btn0.place(x=75, y=290)
btn0.config(font=("Helvetica", 18))
btn0.config(width="3")
btn0.config(height="1")

btnPlus = Button(window, text="+", command = buttenPlus)
btnPlus.place(x=195, y=110)
btnPlus.config(font=("Helvetica", 18))
btnPlus.config(width="3")
btnPlus.config(height="1")

btnMinus = Button(window, text="-", command = buttenMinus)
btnMinus.place(x=195, y=170)
btnMinus.config(font=("Helvetica", 18))
btnMinus.config(width="3")
btnMinus.config(height="1")

btnMulti = Button(window, text="*", command = buttenMulti)
btnMulti.place(x=195, y=230)
btnMulti.config(font=("Helvetica", 18))
btnMulti.config(width="3")
btnMulti.config(height="1")

btnDiv = Button(window, text="/", command = buttenDiv)
btnDiv.place(x=255, y=170)
btnDiv.config(font=("Helvetica", 18))
btnDiv.config(width="3")
btnDiv.config(height="1")

btnlft = Button(window, text="(", command = buttenLeft)
btnlft.place(x=202, y=290)
btnlft.config(font=("Helvetica", 11))
btnlft.config(width="1")
btnlft.config(height="2")

btnRgh = Button(window, text=")", command = buttenRight)
btnRgh.place(x=222, y=290)
btnRgh.config(font=("Helvetica", 11))
btnRgh.config(width="1")
btnRgh.config(height="2")

btnEQ = Button(window, text="=", command = buttenEq)
btnEQ.place(x=255, y=230)
btnEQ.config(font=("Helvetica", 18))
btnEQ.config(width="3")
btnEQ.config(height="1")

btnCC = Button(window, text="C", command = buttenCC)
btnCC.place(x=10, y=10)
btnCC.config(font=("Helvetica", 15))
btnCC.config(width="3")
btnCC.config(height="1")

btnDot = Button(window, text=".", command = buttenDot)
btnDot.place(x=135, y=290)
btnDot.config(font=("Helvetica", 18))
btnDot.config(width="3")
btnDot.config(height="1")

btnDel = Button(window, text="←", command = buttenDel)
btnDel.place(x=255, y=110)
btnDel.config(font=("Helvetica", 18))
btnDel.config(width="3")
btnDel.config(height="1")

window.mainloop()