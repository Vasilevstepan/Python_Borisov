from random import randint
from tkinter import filedialog as fd
from tkinter import *

def Calculation():

    num1 = txt_num1.get()
    num2 = txt_num2.get()

    while not(num1.isdigit() and num2.isdigit()):
        print("Вы вводите не числа, введите пожалуйста что-нибудь нормальное")
        num1 = (input("Введите первое число:"))        
        num2 = (input("Введите второе число:"))
    
    num1 = int(num1)
    num2 = int(num2)
    num3 = ""
    massage = txt_operation.get()
    operation = massage

    if operation == '+':
        num3 = num1 + num2  
        label_result_num['text'] = num3
    elif operation == '-':
        num3 = num1 - num2  
        label_result_num['text'] = num3
    elif operation == '*':
        num3 = num1 * num2
        label_result_num['text'] = num3


    elif operation == '/':
        if num2 == 0:
            print('Делить на 0 нельзя')
        else:
            num3 = num1 / num2
            label_result_num['text'] = num3

    else:
        print('Вы еще не ввели оперцию')


def Choice_File():
    n = 0
    s = []
    for i in range(20):
        s.append(randint(-100,100))
    for i in range(3): 
        with open (f"file{n}.txt", "w+") as f:
            f.write(f"{s}")
            f.close()
            n+= n + 1
    file_path = fd.askopenfilename()

    if file_path:
        with open (file_path, "r") as f:
            lines = f.readlines()
            if lines:                 
                numbers = [int(x) for x in lines[0].split(',') if x.strip().isdigit()] 
                if numbers:
                    arith = sum(numbers) / len(numbers)
                    label_result_num['text'] = arith
                else:
                    print("Файл не содержит чисел.")
            else:
                print("Файл пустой.")
    else:
        print("Файл не выбран.")

def WarCat():
    class Cat:
        cat_count = 0
        def __init__(self,name,age,toy):
            self.name = name
            self.age = age
            self.toy = toy
            Cat.cat_count += 1
        def display(self):
            print(f"Вашу кошку зовут {self.name}, ей {self.age} года и ее любимая игрушка {self.toy}")

    cat1 = Cat("Pusha", 3, "Mini-cat")
    cat2 = Cat("Kitty", 4, "Ball")


    class War_cat(Cat):
        def __init__(self,name,age,toy,weapon):
            Cat.__init__(self,name,age,toy)
            self.weapon = weapon
        def display(self):
            print(f"Вашу кошку зовут {self.name}, ей {self.age} года и ее любимая игрушка {self.toy} в ее арсенала {self.weapon}")
        def display_count(self):
            print(f"Всего кошек {Cat.cat_count}")

    cat1 = War_cat("Pusha", 3, "Mini-cat", 'knife')
    cat2 = War_cat("Kitty", 4, "Ball", "gun")

    cat2.display()
    cat1.display()
    cat2.display_count()

window = Tk()
window.geometry("700x500")
window.title("Графический интерфейс")

label_result = Label(window,text="Ваш результат: ",font='Arial 15')
label_result.grid(column=14, row=0)

label_result_num = Label(font='Arial 15')
label_result_num.grid(column=15, row=0)

cal_but = Button(window, text='Посчитать числа', command=Calculation,font='Arial 15',bg='light blue')
choicef_but = Button(window, text='Выбрать файл для записи', command=Choice_File,font='Arial 15',bg='light blue')
warCat_but = Button(window, text='Унаследованные боевые кошки', command=WarCat,font='Arial 15',bg='light blue')



txt_num1 = Entry(window,width=20)
txt_num2 = Entry(window,width=20)
txt_operation = Entry(window,width=20)

lbl3 = Label(window,text="Введите первое число",font='Arial 15')
txt_num1.grid(column=10,row=1)
lbl3.grid(column=10,row=0)


lbl4 = Label(window,text="Введите второе число",font='Arial 15')
txt_num2.grid(column=10,row=3)
lbl4.grid(column=10,row=2)
txt_operation.grid(column=10,row=5)

lbl5 = Label(window,text='''
    Выберите операцию:
    + - сложение
    - - вычетание
    / - деление
    * - умножение
    ''',font='Arial 15')
lbl5.grid(column=10,row=4)



cal_but.grid(column=10,row=6)

lbl1 = Label(window,text="Выбрать файл через проводник",font='Arial 15')
lbl1.grid(column=13,row=0)
choicef_but.grid(column=13,row=1)


window.mainloop()