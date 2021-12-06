import tkinter as tk
#

class CalculadoraTk:


    def __init__(self):
        self.jan = tk.Tk()
        
        self.f1= tk.Frame(self.jan)
        self.visor = tk.Entry(self.f1, width=23, justify="right")
        self.visor.insert(0,"0")
        self.visor.grid(row=0, column=1)        
             
        #botoes linha 1
        self.f2= tk.Frame(self.jan)
        
        self.bt7 =tk.Button(self.f2, text=("7"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt7.grid(row=1, column=0)

        
        self.bt8 =tk.Button(self.f2, text=("8"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt8.grid(row=1, column=1)

        
        self.bt9 =tk.Button(self.f2, text=("9"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt9.grid(row=1, column=2)

        
        self.btdv =tk.Button(self.f2, text=("/"),font=("verdana"),pady=6,padx=8, bg="blue")
        self.btdv.grid(row=1, column=3)

        #botoes linha 2
        
        self.bt4 =tk.Button(self.f2, text=("4"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt4.grid(row=2, column=0)

        
        self.bt5 =tk.Button(self.f2, text=("5"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt5.grid(row=2, column=1)

        
        self.bt6 =tk.Button(self.f2, text=("6"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt6.grid(row=2, column=2)

        
        self.btx =tk.Button(self.f2, text=("x"),font=("verdana"),pady=6,padx=7, bg="blue")
        self.btx.grid(row=2, column=3)

        #botoes linha 3
        
        self.bt1 =tk.Button(self.f2, text=("1"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt1.grid(row=3, column=0)

        
        self.bt2 =tk.Button(self.f2, text=("2"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt2.grid(row=3, column=1)

        
        self.bt3 =tk.Button(self.f2, text=("3"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt3.grid(row=3, column=2)

        
        self.btmenos =tk.Button(self.f2, text=("-"),font=("verdana"),pady=6,padx=8, bg="blue")
        self.btmenos.grid(row=3, column=3)

        #botoes linha 4
        
        self.btc =tk.Button(self.f2, text=("C"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.btc.grid(row=4, column=0)

        
        self.bt0 =tk.Button(self.f2, text=("0"),font=("verdana"),pady=6,padx=6, bg="blue")
        self.bt0.grid(row=4, column=1)

        
        self.btponto =tk.Button(self.f2, text=("."),font=("verdana"),pady=6,padx=7, bg="blue")
        self.btponto.grid(row=4, column=2)

        
        self.btmais =tk.Button(self.f2, text=("+"),font=("verdana"),pady=6,padx=5, bg="blue")
        self.btmais.grid(row=4, column=3)

        self.f3= tk.Frame(self.jan)
        self.btigual = tk.Button(self.f3, text=("="),font=("verdana"), padx=58, bg="blue")
        self.btigual.grid(row=0, column=1)
     

        self.f1.pack()
        self.f2.pack()
        self.f3.pack()
        self.jan.mainloop()

CalculadoraTk()