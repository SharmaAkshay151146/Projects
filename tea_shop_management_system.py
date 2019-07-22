from tkinter import *
from tkinter import font
from tkinter import messagebox
import random
import time
import datetime


class Coffee:
    def quit_program(self):
        q_exit = messagebox.askyesno("Quit Program","Do you want to quit ?")
        if q_exit > 0:
            root.quit()
            return 
    
    def reset(self):
        self.paid_tax.set("")
        self.sub_total.set("")
        self.total_cost.set("")
        self.cost_of_drinks.set("")
        self.cost_of_snacks.set("")
        self.service_charge.set("")
        self.txt_receipt.delete("1.0", END)
        self.t_masala_tea.set("0")
        self.t_ginger_tea.set("0")
        self.t_green_tea.set("0")
        self.t_normal_tea.set("0")
        self.t_samosa.set("0")
        self.t_banana_cake.set("0")
        self.t_veg_patty.set("0")
        self.t_paneer_patty.set("0")


        self.txt_masala_tea.configure(state=DISABLED)
        self.txt_ginger_tea.configure(state=DISABLED)
        self.txt_green_tea.configure(state=DISABLED)
        self.txt_normal_tea.configure(state=DISABLED)
        self.txt_samosa.configure(state=DISABLED)
        self.txt_banana_cake.configure(state=DISABLED)
        self.txt_veg_patty.configure(state=DISABLED)
        self.txt_paneer_patty.configure(state=DISABLED)

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)


    # ------------- Code for checkbox ---------------------------------------

    def display_checkbox(self):
        if self.var1.get() == 1:
            self.txt_masala_tea.configure(state=NORMAL)
        elif self.var1.get() == 0:
            self.txt_masala_tea.configure(state=DISABLED)
            self.t_masala_tea.set("0")
        if self.var2.get() == 1:
            self.txt_ginger_tea.configure(state=NORMAL)
        elif self.var2.get() == 0:
            self.txt_ginger_tea.configure(state=DISABLED)
            self.t_ginger_tea.set("0")
        if self.var3.get() == 1:
            self.txt_green_tea.configure(state=NORMAL)
        elif self.var3.get() == 0:
            self.txt_green_tea.configure(state=DISABLED)
            self.t_green_tea.set("0")
        if self.var4.get() == 1:
            self.txt_normal_tea.configure(state=NORMAL)
        elif self.var4.get() == 0:
            self.txt_normal_tea.configure(state=DISABLED)
            self.t_normal_tea.set("0")
        if self.var5.get() == 1:
            self.txt_samosa.configure(state=NORMAL)
        elif self.var5.get() == 0:
            self.txt_samosa.configure(state=DISABLED)
            self.t_samosa.set("0")
        if self.var6.get() == 1:
            self.txt_banana_cake.configure(state=NORMAL)
        elif self.var6.get() == 0:
            self.txt_banana_cake.configure(state=DISABLED)
            self.t_banana_cake.set("0")
        if self.var7.get() == 1:
            self.txt_veg_patty.configure(state=NORMAL)
        elif self.var7.get() == 0:
            self.txt_veg_patty.configure(state=DISABLED)
            self.t_veg_patty.set("0")
        if self.var8.get() == 1:
            self.txt_paneer_patty.configure(state=NORMAL)
        elif self.var8.get() == 0:
            self.txt_paneer_patty.configure(state=DISABLED)
            self.t_paneer_patty.set("0")


    def cost_of_items(self):
        item1 = float(self.t_masala_tea.get())
        item2 = float(self.t_ginger_tea.get())
        item3 = float(self.t_green_tea.get())
        item4 = float(self.t_normal_tea.get())

        item5 = float(self.t_samosa.get())
        item6 = float(self.t_banana_cake.get())
        item7 = float(self.t_veg_patty.get())
        item8 = float(self.t_paneer_patty.get())

        price_tea = (item1 * 17) + (item2 * 15) + (item3 * 12) + (item4 * 14)
        price_snacks = (item5 * 15) + (item6 * 30) + (item7 * 15) + (item8 * 25)

        price_drinks = "Rs. " + str('%.2f' % (price_tea))
        snacks_price = "Rs. " + str('%.2f' % (price_snacks))
        self.cost_of_snacks.set(snacks_price)
        self.cost_of_drinks.set(price_drinks)
        SC = "Rs. " + str('%.2f' % (5))
        self.service_charge.set(SC)

        service_charge = 5
        GST = 0.15

        if price_tea == 0 and price_snacks == 0:
            service_charge = 0
            GST = 0
            self.service_charge.set("Rs. 0.00")
            

        sub_total_of_item = "Rs. " + str('%.2f' % (price_tea + price_snacks + service_charge))
        self.sub_total.set(sub_total_of_item)
        Tax = "Rs. " + str('%.2f' %
                           ((price_tea + price_snacks + service_charge)*GST))
        self.paid_tax.set(Tax)
        TT = ((price_tea + price_snacks + service_charge)*GST)
        TC = "Rs. " + str('%.2f' %
                          (price_tea + price_snacks + service_charge + TT))
        self.total_cost.set(TC)


    def receipt(self):
        self.txt_receipt.delete("1.0", END)
        x = random.randint(10908, 500876)
        randomRef = str(x)
        self.receipt_ref.set("BILL" + randomRef)

        self.txt_receipt.insert(
            END, 'Receipt Ref:  '+self.receipt_ref.get()+" "+self.order_date.get()+"\n")
        self.txt_receipt.insert(
            END, 'Items '+'Quantity '+"Price \n\n")
        
        if self.t_masala_tea.get() == 0 and self.t_banana_cake.get() == 0 and self.t_ginger_tea.get() == 0 and self.t_green_tea.get() == 0 and self.t_normal_tea.get() == 0 and self.t_veg_patty.get() == 0 and self.t_samosa.get() == 0 and self.t_paneer_patty.get() == 0:
            self.service_charge.set("Rs. 0.00")
            self.total_cost.set("Rs. 0.00")
            self.paid_tax.set("Rs. 0.00")
            self.cost_of_drinks.set("Rs. 0.00")
            self.cost_of_snacks.set("Rs. 0.00")
            self.sub_total.set("Rs. 0.00")

        if self.t_masala_tea.get() > 0:
            self.txt_receipt.insert(END, 'Masala Tea: '+str(self.t_masala_tea.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_masala_tea.get()*17))+'\n')
        if self.t_ginger_tea.get() > 0:
            self.txt_receipt.insert(END, 'Ginger Tea: '+str(self.t_ginger_tea.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_ginger_tea.get()*15))+'\n')
        if self.t_green_tea.get() > 0:
            self.txt_receipt.insert(END, 'Green Tea: '+str(self.t_green_tea.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_green_tea.get()*12))+'\n')
        if self.t_normal_tea.get() > 0:
            self.txt_receipt.insert(END, 'Normal Tea: '+str(self.t_normal_tea.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_normal_tea.get()*14))+'\n')
        if self.t_samosa.get() > 0:
            self.txt_receipt.insert(END, 'Samosa: '+str(self.t_samosa.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_samosa.get()*15))+'\n')
        if self.t_banana_cake.get() > 0:
            self.txt_receipt.insert(END, 'Banana Cake: '+str(self.t_banana_cake.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_banana_cake.get()*30))+'\n')
        if self.t_veg_patty.get() > 0:
            self.txt_receipt.insert(END, 'Veg. Patty: '+str(self.t_veg_patty.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_veg_patty.get()*15))+'\n')
        if self.t_paneer_patty.get() > 0:
            self.txt_receipt.insert(END, 'Panner Patty: '+str(self.t_paneer_patty.get()) +
                                    ' '+str('Rs. %.2f' % (self.t_paneer_patty.get()*25))+'\n')

        self.txt_receipt.insert(
            END, '\nCost of Drinks:\t'+self.cost_of_drinks.get()+"\tTax Paid:\t" + self.paid_tax.get()+"\n")
        self.txt_receipt.insert(
            END, 'Cost of Snacks:\t'+self.cost_of_snacks.get()+"\tSub-Total:\t" + self.sub_total.get()+"\n")
        self.txt_receipt.insert(
            END, 'Service Charge:\t'+self.service_charge.get()+"\tTotal Cost:\t" + self.total_cost.get()+"\n")


    def __init__(self, root):

        root.geometry("1200x1024")
        root.title("Hogwards Cafe")
        root.configure(background='burlywood2')

        Top = Frame(root, width=1400, height=100, bd=10, relief="raise")
        Top.pack(side=TOP)

        f1 = Frame(root, width=500, height=250, bd=8, relief="raise")
        f1.pack(side=LEFT)

        f2 = Frame(root, width=500, height=250, bd=8, relief="raise")
        f2.pack(side=RIGHT)

        f1a = Frame(f1, width=500, height=250, bd=8, relief="raise")
        f1a.pack(side=TOP)

        f2a = Frame(f1, width=500, height=250, bd=6, relief="raise")
        f2a.pack(side=BOTTOM)

        ft2 = Frame(f2, width = 220, height = 125, bd = 12, relief = "raise")
        ft2.pack(side=TOP)
        fb2 = Frame(f2, width=220, height = 125, bd=16, relief = "raise")
        fb2.pack(side=BOTTOM)

        f1aa = Frame(f1a, width = 100, height = 165, bd = 16, relief = "raise")
        f1aa.pack(side = LEFT)
        f1ab = Frame(f1a, width = 100, height = 165, bd = 16, relief = "raise")
        f1ab.pack(side = RIGHT)

        f2aa = Frame(f2a, width = 100, height = 165, bd = 14, relief = "raise")
        f2aa.pack(side = LEFT)

        f2ab = Frame(f2a, width = 100, height = 165, bd = 14, relief = "raise")
        f2ab.pack(side = RIGHT)

        Top.configure(background="burlywood1")
        f1.configure(background="burlywood1")
        f2.configure(background="burlywood1")

        label_info = Label(Top, font=('San Serif', 50, 'bold'), text="Chai Pradesh Tea & Snacks Management", bd=10, height=2)
        label_info.grid(row=0, column=0)


        # Variables for drinks
        self.var1 = IntVar(value=0)
        self.var2 = IntVar(value=0)
        self.var3 = IntVar(value=0)
        self.var4 = IntVar(value=0)


        # Text variables for drinks
        self.t_masala_tea = IntVar(value=0)
        self.t_ginger_tea = IntVar(value=0)
        self.t_green_tea = IntVar(value=0)
        self.t_normal_tea = IntVar(value=0)

        # Variables for food
        self.var5 = IntVar(value=0)
        self.var6 = IntVar(value=0)
        self.var7 = IntVar(value=0)
        self.var8 = IntVar(value=0)


        # Text variables for food
        self.t_samosa = IntVar(value=0)
        self.t_banana_cake = IntVar(value=0)
        self.t_veg_patty = IntVar(value=0)
        self.t_paneer_patty = IntVar(value=0)
        
        

        # Other variables
        self.order_date = StringVar(value=time.strftime("%d/%m/%Y"))
        self.receipt_ref = StringVar()
        self.paid_tax = StringVar()
        self.sub_total = StringVar()
        self.total_cost = StringVar()
        self.cost_of_snacks = StringVar()
        self.cost_of_drinks = StringVar()
        self.service_charge = StringVar()

        # Left hand frame is f1aa
        # --------------------------- Drinks --------------------------------------
        self.masala_tea = Checkbutton(f1aa, text="Masala Tea     \t", variable=self.var1, onvalue=1, command=self.display_checkbox,
                                 offvalue=0, font=('San Serif', 22, 'bold')).grid(row=0, column=0, sticky=W)
        self.ginger_tea = Checkbutton(f1aa, text="Ginger Tea \t", variable=self.var2, onvalue=1, command=self.display_checkbox,
                                    offvalue=0, font=('San Serif', 22, 'bold')).grid(row=1, column=0, sticky=W)
        self.green_tea = Checkbutton(f1aa, text="Green Tea \t", variable=self.var3, onvalue=1,command=self.display_checkbox, offvalue=0, font=('San Serif', 22, 'bold')).grid(row=2, column=0, sticky = W)
        self.normal_tea = Checkbutton(f1aa, text="Regular Tea\t", variable=self.var4, onvalue=1,
                                      command=self.display_checkbox, offvalue=0, font=('San Serif', 22, 'bold')).grid(row=3, column=0, sticky=W)

        # Right hand frame is f1ab
        # --------------------------- Snacks --------------------------------------
        self.Samosa = Checkbutton(f1ab, text="Samosa    \t", variable=self.var5, onvalue=1,command=self.display_checkbox, offvalue=0, font=('San Serif', 22, 'bold')).grid(row=0, column=0, sticky = W)
        self.banana_cake = Checkbutton(f1ab, text="Banana Cake\t", variable=self.var6, onvalue=1,command=self.display_checkbox, offvalue=0, font=('San Serif', 22, 'bold')).grid(row=1, column=0, sticky = W)
        self.veg_patty = Checkbutton(f1ab, text="Veg Patty\t", variable=self.var7, onvalue=1,command=self.display_checkbox, offvalue=0, font=('San Serif', 22, 'bold')).grid(row=2, column=0, sticky = W)
        self.paneer_patty = Checkbutton(f1ab, text="Paneer Patty\t", variable=self.var8, onvalue=1,
                                        command=self.display_checkbox, offvalue=0, font=('San Serif', 22, 'bold')).grid(row=3, column=0, sticky=W)
        
        
        # ------------- Widget for Drinks --------------------
        
        self.txt_masala_tea = Entry(f1aa, font=('San Serif', 22, 'bold'), bd=8,
                                    width=6, textvariable=self.t_masala_tea, justify='left', state=DISABLED)
        self.txt_masala_tea.grid(row=0,column=1)
        self.txt_ginger_tea = Entry(f1aa, font=('San Serif', 22, 'bold'), bd = 8, width = 6,textvariable = self.t_ginger_tea, justify='left', state=DISABLED)
        self.txt_ginger_tea.grid(row=1,column=1)
        self.txt_green_tea = Entry(f1aa, font=('San Serif', 22, 'bold'), bd=8,
                                   width=6, textvariable=self.t_green_tea, justify='left', state=DISABLED)
        self.txt_green_tea.grid(row=2, column=1)
        self.txt_normal_tea = Entry(f1aa, font=('San Serif', 22, 'bold'), bd = 8, width = 6,textvariable = self.t_normal_tea,justify='left', state=DISABLED)
        self.txt_normal_tea.grid(row=3,column=1)

        
        # ------------- Entry for Snacks ------------------
        
        self.txt_samosa = Entry(f1ab, font=('San Serif', 22, 'bold'), bd=8,
                                width=6, textvariable=self.t_samosa, justify='left', state=DISABLED)
        self.txt_samosa.grid(row=0,column=1)
        self.txt_banana_cake = Entry(f1ab, font=('San Serif', 22, 'bold'), bd = 8, width = 6,textvariable = self.t_banana_cake,justify='left', state=DISABLED)
        self.txt_banana_cake.grid(row=1,column=1)
        self.txt_veg_patty = Entry(f1ab, font=('San Serif', 22, 'bold'), bd = 8, width = 6,textvariable = self.t_veg_patty,justify='left', state=DISABLED)
        self.txt_veg_patty.grid(row=2,column=1)
        self.txt_paneer_patty = Entry(f1ab, font=('San Serif', 22, 'bold'), bd=8,
                                      width=6, textvariable=self.t_paneer_patty, justify='left', state=DISABLED)
        self.txt_paneer_patty.grid(row=3,column=1)
        

        # ---------------------- Item Information ----------------------
        self.label_receipt = Label(ft2, font=('San Serif', 14, 'bold'),text = "Receipt", bd=2, anchor='w')
        self.label_receipt.grid(row=0, column=0, sticky=W)
        self.txt_receipt = Text(ft2, font=('San Serif', 11, 'bold'), bd = 8, width = 50, height=16)
        self.txt_receipt.grid(row=1,column=0)

        # -------------------- Cost of Item Info --------------
        self.label_cost_of_drinks = Label(f2aa, font=('San Serif', 16, 'bold'), text="Cost of Drinks", bd=8)
        self.label_cost_of_drinks.grid(row=0,column=0,sticky=W)
        self.txt_cost_of_drinks = Entry(f2aa, font=('San Serif', 16, 'bold'), bd=8, textvariable=self.cost_of_drinks,justify='left')
        self.txt_cost_of_drinks.grid(row=0, column=1, sticky=W)

        self.label_cost_of_snacks = Label(f2aa, font=('San Serif', 16, 'bold'), text="Cost of snacks", bd=8)
        self.label_cost_of_snacks.grid(row=1,column=0,sticky=W)
        self.txt_cost_of_snacks = Entry(f2aa, font=('San Serif', 16, 'bold'), bd=8, textvariable=self.cost_of_snacks,justify='left')
        self.txt_cost_of_snacks.grid(row=1, column=1, sticky=W)

        self.label_service_charge = Label(f2aa, font=('San Serif', 16, 'bold'), text="Service charge", bd=8)
        self.label_service_charge.grid(row=2,column=0,sticky=W)
        self.txt_service_charge = Entry(f2aa, font=('San Serif', 16, 'bold'), bd=8, textvariable=self.service_charge,justify='left')
        self.txt_service_charge.grid(row=2, column=1, sticky=W)


        # ------------------ Price Info ------------------------
        self.label_tax = Label(f2ab, font=('San Serif', 16, 'bold'), text="Tax", bd=8)
        self.label_tax.grid(row=0,column=0,sticky=W)
        self.txt_tax = Entry(f2ab, font=('San Serif', 16, 'bold'), bd=8,textvariable=self.paid_tax, justify='left')
        self.txt_tax.grid(row=0, column=1, sticky=W)

        self.label_price = Label(f2ab, font=('San Serif', 16, 'bold'), text="Price", bd=8)
        self.label_price.grid(row=1,column=0,sticky=W)
        self.txt_price = Entry(f2ab, font=('San Serif', 16, 'bold'), bd=8,textvariable=self.sub_total, justify='left')
        self.txt_price.grid(row=1, column=1, sticky=W)

        self.label_sum_total = Label(f2ab, font=('San Serif', 16, 'bold'), text="Sum Total", bd=8)
        self.label_sum_total.grid(row=2,column=0,sticky=W)
        self.txt_sum_total = Entry(f2ab, font=('San Serif', 16, 'bold'), bd=8, textvariable=self.total_cost, justify='left')
        self.txt_sum_total.grid(row=2, column=1, sticky=W)

        # -------------------- Buttons ------------------------
        self.btn_total = Button(fb2, padx=14, pady=1,bd = 4, fg='black', font=('San Serif', 14, 'bold'), width = 5, text = 'Total',command=self.cost_of_items).grid(row=0, column=0)
        self.btn_receipt = Button(fb2, padx=14, pady=1, bd = 4, fg='black', font=('San Serif', 14, 'bold'), width = 5, text = 'Receipt',command=self.receipt).grid(row=0, column=1)
        self.btn_reset = Button(fb2, padx=14, pady=1, bd = 4, fg='black', font=('San Serif', 14, 'bold'), width = 5, text = 'Reset', command = self.reset).grid(row=0, column=2)
        self.btn_quit = Button(fb2, padx=14, pady=1, bd=4, fg='black', font=('San Serif', 14, 'bold'), width=5, text='Quit', command=self.quit_program).grid(row=0, column=3)

root = Tk()

coffee_shop = Coffee(root)

root.mainloop()
