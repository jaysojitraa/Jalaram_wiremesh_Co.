""""

"""

# Import Modules
import tkinter as tk
from tkinter import *
from datetime import date
import re
import random
import string
import time
import os
import sys
##import pymysql
#import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from math import *
from tkinter.colorchooser import *




#### Main Frame ####

def close(event):
    
    sys.exit()


from tkinter import *      
     
j = Tk()

img = PhotoImage(file="image.png")
label1 = Label( j, image = img)
label1.place(x = -870,y = -300)

j.geometry("200x300")
j.attributes('-fullscreen',True)


j.configure(bg='Black')
j.title("Jᴀʟᴀʀᴀᴍ Wɪʀᴇᴍᴇsʜ Cᴏ.")









ax= '''Jalaram Wire Mesh Co.'''







ay=Label(j,text = ax,font=("Kokila",50),fg='white',bg="#E83135" ,borderwidth = 5,takefocus=0).place(x=385, y=100)
  






### Main_program 1 ###


def Wire_mesh_Costing():
    j.destroy()
    
    root=tk.Tk()
    root.geometry("1200x550")
    root.state("zoomed")
    root.configure(bg='#D8EDEC')
    canvas = Canvas(root, width=2000, height=2000,bg='#D8EDEC')
    canvas.pack()
    canvas.create_rectangle(2, 2, 1175, 530)

    # Default Date

    today = date.today()
    dt1 = str(today)
    dt = StringVar(root, value=dt1)


    ######## image as background ##########



    options = [
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]


    options1 = [
                "Option 1",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]
    options2 = [
                "Option 2",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]
    options3 = [
                "Option 3",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]
    options4 = [
                "Option 4",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]
    options5 = [
                "Option 5",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]
    options6 = [
                "Option 6",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]
    options7 = [
                "Option 7",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]
    options8 = [
                "Option 8",
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]

              
    # datatype of menu text
    clicked1 = StringVar()
    clicked2 = StringVar()
    clicked3 = StringVar()
    clicked4 = StringVar()
    clicked5 = StringVar()
    clicked6 = StringVar()
    clicked7 = StringVar()
    clicked8 = StringVar()
    clicked9 = StringVar()
    clicked10 = StringVar()
    clicked11 = StringVar()
    clicked12 = StringVar()
    clicked13 = StringVar()
    clicked14 = StringVar()
    clicked15 = StringVar()
    clicked16 = StringVar()
    clicked20 = StringVar()
    clicked21 = StringVar()


    clicked1.set("Option 1")
    clicked3.set("Option 2")
    clicked5.set("Option 3")
    clicked7.set("Option 4")
    clicked9.set("Option 5")
    clicked11.set("Option 6")
    clicked13.set("Option 7")
    clicked15.set("Option 8")
    clicked20.set("Parties")
              

    OptionMenu( root , clicked1 , *options1 ).place(x=10, y = 550)
    Entry(root,textvariable = clicked2,takefocus=0  ).place(x=10, y = 580)
    OptionMenu( root , clicked3 , *options2 ).place(x=200, y = 550)
    Entry(root,textvariable = clicked4,takefocus=0  ).place(x=200, y = 580)
    OptionMenu( root , clicked5 , *options3 ).place(x=390, y = 550)
    Entry(root,textvariable = clicked6,takefocus=0  ).place(x=390, y = 580)
    OptionMenu( root , clicked7 , *options4 ).place(x=580, y = 550)
    Entry(root,textvariable = clicked8,takefocus=0  ).place(x=580, y = 580)
    OptionMenu( root , clicked9 , *options5 ).place(x=770, y = 550)
    Entry(root,textvariable = clicked10,takefocus=0  ).place(x=770, y = 580)
    OptionMenu( root , clicked11 , *options6 ).place(x=960, y = 550)
    Entry(root,textvariable = clicked12,takefocus=0  ).place(x=960, y = 580)
    OptionMenu( root , clicked13 , *options7 ).place(x=1150, y = 550)
    Entry(root,textvariable = clicked14,takefocus=0  ).place(x=1150, y = 580)
    OptionMenu( root , clicked15 , *options8 ).place(x=1340, y = 550)
    Entry(root,textvariable = clicked16,takefocus=0  ).place(x=1340, y = 580)



    # declaring string variable        
    Sr_Number_var=tk.StringVar()
    Date_var=tk.StringVar()
    Party_Name_var=tk.StringVar()
    Warp_MESH_var=tk.StringVar()
    Weft_MESH_var=tk.StringVar()
    Warp_DIAMETER_var=tk.StringVar()
    Weft_DIAMETER_var=tk.StringVar()
    Warp_GRADE_var=tk.StringVar()
    Weft_GRADE_var=tk.StringVar()
    WIDTH_1_var=tk.StringVar()
    WIDTH_2_var=tk.StringVar()
    WIDTH_3_var=tk.StringVar()
    LENGTH_1_var=tk.StringVar()
    LENGTH_2_var=tk.StringVar()
    LENGTH_3_var=tk.StringVar()
    Warp_WIRE_RATE_var=tk.StringVar()
    Weft_WIRE_RATE_var=tk.StringVar()
    RPM_var=tk.StringVar()
    EFFICIENCY_var=tk.StringVar()
    SCRAPE_PERCENTAGE_var=tk.StringVar()
    SELL_RATE_var=tk.StringVar()

   

    def calculate():
        # Variables
            
        Sr_Number=int(Sr_Number_var.get())
        Date=str(dt.get())
        Party_Name=Party_Name_var.get()
        Warp_MESH=float(Warp_MESH_var.get())
        Weft_MESH=float(Weft_MESH_var.get())
        Warp_DIAMETER=float(Warp_DIAMETER_var.get())
        Weft_DIAMETER=float(Weft_DIAMETER_var.get())
        Warp_GRADE=Warp_GRADE_var.get()
        Weft_GRADE=Weft_GRADE_var.get()
        WIDTH_1=float(WIDTH_1_var.get())
        WIDTH_2=float(WIDTH_2_var.get())
        WIDTH_3=float(WIDTH_3_var.get())
        LENGTH_1=float(LENGTH_1_var.get())
        LENGTH_2=float(LENGTH_2_var.get())
        LENGTH_3=float(LENGTH_3_var.get())
        Warp_WIRE_RATE=float(Warp_WIRE_RATE_var.get())
        Weft_WIRE_RATE=float(Weft_WIRE_RATE_var.get())
        RPM=float(RPM_var.get())
        EFFICIENCY=float(EFFICIENCY_var.get())
        SCRAPE_PERCENTAGE=float(SCRAPE_PERCENTAGE_var.get())
        SELL_RATE=float(SELL_RATE_var.get())
        

        
        ### Formulas ###
        
        Sqft_1 = WIDTH_1*LENGTH_1*10.764
        Sqft_2 = WIDTH_2*LENGTH_2*10.764
        Sqft_3 = WIDTH_3*LENGTH_3*10.764

        Sqmtr_1 = WIDTH_1*LENGTH_1
        Sqmtr_2 = WIDTH_2*LENGTH_2
        Sqmtr_3 = WIDTH_3*LENGTH_3

        Warp_Wire_Quantity =(((Warp_DIAMETER*Warp_DIAMETER*0.493*Warp_MESH)/2)*((WIDTH_1*LENGTH_1)+(WIDTH_2*LENGTH_2)+(WIDTH_3*LENGTH_3)))*(1+(SCRAPE_PERCENTAGE/100))

        Weft_Wire_Quantity =(((Weft_DIAMETER*Weft_DIAMETER*0.493*Weft_MESH)/2)*((WIDTH_1*LENGTH_1)+(WIDTH_2*LENGTH_2)+(WIDTH_3*LENGTH_3)))*(1+(SCRAPE_PERCENTAGE/100))

        Total_Wire_Quantity = Warp_Wire_Quantity+Weft_Wire_Quantity

        RM_Wire_Value =(Warp_Wire_Quantity*Warp_WIRE_RATE)+(Weft_Wire_Quantity*Weft_WIRE_RATE)

        FG_Value = (Sqft_1+Sqft_2+Sqft_3)*SELL_RATE

        Diff_Value = (FG_Value)-(RM_Wire_Value)

        totalsqft=Sqft_1+Sqft_2+Sqft_3

        RM_Value_Per_Sqft = RM_Wire_Value/totalsqft

        Diff_per_Sqft =  SELL_RATE-RM_Value_Per_Sqft

        Linear_production_per_day = ((RPM*60*24)/(39.37*Weft_MESH))*(EFFICIENCY/100)

        Diff_percentage = (Diff_per_Sqft/RM_Value_Per_Sqft)*100

        Wire_Weight_per_Sq_meter = ((Warp_DIAMETER*Warp_DIAMETER*0.493*Warp_MESH)/2)+((Weft_DIAMETER*Weft_DIAMETER*0.493*Weft_MESH)/2)

        Production_sq_mtr_per_day_1 = (LENGTH_1/Linear_production_per_day)*1.14*WIDTH_1
        Production_sq_mtr_per_day_2 = (LENGTH_2/Linear_production_per_day)*1.14*WIDTH_2
        Production_sq_mtr_per_day_3 = (LENGTH_3/Linear_production_per_day)*1.14*WIDTH_3

        Diff_per_day_1 = (Linear_production_per_day*WIDTH_1*10.764)*Diff_per_Sqft
        Diff_per_day_2 = (Linear_production_per_day*WIDTH_2*10.764)*Diff_per_Sqft
        Diff_per_day_3 = (Linear_production_per_day*WIDTH_3*10.764)*Diff_per_Sqft


        Total_number_of_day = (LENGTH_1+LENGTH_2+LENGTH_3)/(Linear_production_per_day)
        ##

        # OutPuts
        
        one=Label(root, text="        Warp Wire Qty  :           " + str(round(Warp_Wire_Quantity))+ " Kg ",font=("Arial", 12),bg='#00CC98', width=40, anchor="w",borderwidth=2, relief="solid")
        one.place(x=800, y=10)
        two=Label(root, text="        Weft Wire Qty  :            " + str(round(Weft_Wire_Quantity))+ " Kg ", font=("Arial", 12),bg='#00CC98', width=40, anchor="w",borderwidth=2, relief="solid")
        two.place(x=800, y=35)
        three=Label(root, text="        Total Wire Quantity  :    " + str(round(Total_Wire_Quantity))+ " Kg ",font=("Arial", 12),bg='#00CC98', width=40, anchor="w",borderwidth=2, relief="solid")
        three.place(x=800, y=60)
        four=Label(root, text="        RM Wire Value  :  Rs  " + str(round(RM_Wire_Value)),font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        four.place(x=800, y=85)
        five=Label(root, text="        FG Value  :            Rs  " + str(round(FG_Value)),font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        five.place(x=800, y=110)
        six=Label(root, text="        Diff Value  :           Rs  " + str(round(Diff_Value)),font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        six.place(x=800, y=135)
        seven=Label(root, text="        Sell Rate  :                   Rs  " + str(SELL_RATE),font=("Arial", 12),bg='#FFCCE7', width=40, anchor="w",borderwidth=2, relief="solid")
        seven.place(x=800, y=160)
        eight=Label(root, text="        RM Value Per Sqft  :   Rs  "+ str(round(RM_Value_Per_Sqft,2)),font=("Arial", 12),bg='#FFCCE7', width=40, anchor="w",borderwidth=2, relief="solid")
        eight.place(x=800, y=185)
        nine=Label(root, text="        Diff per Sqft  :              Rs  "+ str(round(Diff_per_Sqft,2)),font=("Arial", 12),bg='#FFCCE7', width=40, anchor="w",borderwidth=2, relief="solid")
        nine.place(x=800, y=210)
        ten=Label(root, text="        Diff percentage  :                    "+ str(round(Diff_percentage))+ " % ",font=("Arial", 12),bg='#898989', width=40, anchor="w",borderwidth=2, relief="solid")
        ten.place(x=800, y=235)
        eleven=Label(root, text="        Wire Weight per Sq meter  :  " + str(round(Wire_Weight_per_Sq_meter,2))+ " Kg ",bg='#898989',font=("Arial", 12), width=40, anchor="w",borderwidth=2, relief="solid")
        eleven.place(x=800, y=260)
        twelve=Label(root, text="         Diff per day 1  :    Rs  " + str(round(Diff_per_day_1)),font=("Arial", 12),bg='#C58C79', width=40, anchor="w",borderwidth=2, relief="solid")
        twelve.place(x=800, y=285)
        thirteen=Label(root, text="        Diff per day 2  :     Rs  " + str(round(Diff_per_day_2)),font=("Arial", 12),bg='#C58C79', width=40, anchor="w",borderwidth=2, relief="solid")
        thirteen.place(x=800, y=310)
        fourteen=Label(root, text="        Diff per day 3  :     Rs  " + str(round(Diff_per_day_3)),font=("Arial", 12),bg='#C58C79', width=40, anchor="w",borderwidth=2, relief="solid")
        fourteen.place(x=800, y=335)
        fifteen=Label(root, text="        Total Squarefoot :   "+ str(round(totalsqft))+ " SqFt ",font=("Arial", 12), width=40, anchor="w",borderwidth=2, relief="solid")
        fifteen.place(x=800, y=360)
        sixteen=Label(root, text="        Total number of days  :    "+ str(round(Total_number_of_day,0)) ,bg='#0088FC',font=("Arial", 12), width=40, anchor="w",borderwidth=2, relief="solid")
        sixteen.place(x=800, y=385)



    def Save():
        Sr_Number=int(Sr_Number_var.get())
        Date=dt.get()
        Party_Name=Party_Name_var.get()
        Warp_MESH=float(Warp_MESH_var.get())
        Weft_MESH=float(Weft_MESH_var.get())
        Warp_DIAMETER=float(Warp_DIAMETER_var.get())
        Weft_DIAMETER=float(Weft_DIAMETER_var.get())
        Warp_GRADE=Warp_GRADE_var.get()
        Weft_GRADE=Weft_GRADE_var.get()
        WIDTH_1=float(WIDTH_1_var.get())
        WIDTH_2=float(WIDTH_2_var.get())
        WIDTH_3=float(WIDTH_3_var.get())
        LENGTH_1=float(LENGTH_1_var.get())
        LENGTH_2=float(LENGTH_2_var.get())
        LENGTH_3=float(LENGTH_3_var.get())
        Warp_WIRE_RATE=float(Warp_WIRE_RATE_var.get())
        Weft_WIRE_RATE=float(Weft_WIRE_RATE_var.get())
        RPM=float(RPM_var.get())
        EFFICIENCY=float(EFFICIENCY_var.get())
        SCRAPE_PERCENTAGE=float(SCRAPE_PERCENTAGE_var.get())
        SELL_RATE=float(SELL_RATE_var.get())        

        Sqft_1 = WIDTH_1*LENGTH_1*10.764
        Sqft_2 = WIDTH_2*LENGTH_2*10.764
        Sqft_3 = WIDTH_3*LENGTH_3*10.764

        Sqmtr_1 = WIDTH_1*LENGTH_1
        Sqmtr_2 = WIDTH_2*LENGTH_2
        Sqmtr_3 = WIDTH_3*LENGTH_3

        Warp_Wire_Quantity =(((Warp_DIAMETER*Warp_DIAMETER*0.493*Warp_MESH)/2)*((WIDTH_1*LENGTH_1)+(WIDTH_2*LENGTH_2)+(WIDTH_3*LENGTH_3)))*(1+(SCRAPE_PERCENTAGE/100))

        Weft_Wire_Quantity =(((Weft_DIAMETER*Weft_DIAMETER*0.493*Weft_MESH)/2)*((WIDTH_1*LENGTH_1)+(WIDTH_2*LENGTH_2)+(WIDTH_3*LENGTH_3)))*(1+(SCRAPE_PERCENTAGE/100))

        Total_Wire_Quantity = Warp_Wire_Quantity+Weft_Wire_Quantity

        RM_Wire_Value =(Warp_Wire_Quantity*Warp_WIRE_RATE)+(Weft_Wire_Quantity*Weft_WIRE_RATE)

        FG_Value = (Sqft_1+Sqft_2+Sqft_3)*SELL_RATE

        Diff_Value = (FG_Value)-(RM_Wire_Value)

        totalsqft=Sqft_1+Sqft_2+Sqft_3

        RM_Value_Per_Sqft = RM_Wire_Value/totalsqft

        Diff_per_Sqft =  SELL_RATE-RM_Value_Per_Sqft

        Linear_production_per_day = ((RPM*60*24)/(39.37*Weft_MESH))*(EFFICIENCY/100)

        Diff_percentage = (Diff_per_Sqft/RM_Value_Per_Sqft)*100

        Wire_Weight_per_Sq_meter = ((Warp_DIAMETER*Warp_DIAMETER*0.493*Warp_MESH)/2)+((Weft_DIAMETER*Weft_DIAMETER*0.493*Weft_MESH)/2)

        Production_sq_mtr_per_day_1 = (LENGTH_1/Linear_production_per_day)*1.14*WIDTH_1
        Production_sq_mtr_per_day_2 = (LENGTH_2/Linear_production_per_day)*1.14*WIDTH_2
        Production_sq_mtr_per_day_3 = (LENGTH_3/Linear_production_per_day)*1.14*WIDTH_3

        Diff_per_day_1 = (Linear_production_per_day*WIDTH_1*10.764)*Diff_per_Sqft
        Diff_per_day_2 = (Linear_production_per_day*WIDTH_2*10.764)*Diff_per_Sqft
        Diff_per_day_3 = (Linear_production_per_day*WIDTH_3*10.764)*Diff_per_Sqft


        Total_number_of_day = (LENGTH_1+LENGTH_2+LENGTH_3)/(Linear_production_per_day)

        connection = pymysql.connect(host="localhost", user="root", password="0000")
        cursor = connection.cursor()
        a=cursor.execute("SHOW DATABASES LIKE 'Jalaram'")

        b=str(round(Warp_Wire_Quantity))
        c=str(round(Weft_Wire_Quantity))
        d=str(round(Total_Wire_Quantity))
        e=str(round(RM_Wire_Value))
        f=str(round(FG_Value))
        g=str(round(Diff_Value))
        h=str(SELL_RATE)
        i=str(round(RM_Value_Per_Sqft,2))
        j=str(round(Diff_per_Sqft,2))
        k=str(round(Diff_percentage))
        l=str(round(Wire_Weight_per_Sq_meter,2))
        m=str(round(Diff_per_day_1))
        n=str(round(Diff_per_day_2))
        o=str(round(Diff_per_day_3))
        p=str(round(totalsqft))
        q=str(round(Total_number_of_day,0))

        cursor.execute("use Jalaram;")
        insertJalaram="INSERT INTO Jalaram VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(Sr_Number,
        Date,Party_Name,Warp_MESH,Weft_MESH,Warp_DIAMETER,Weft_DIAMETER,Warp_GRADE,Weft_GRADE,Warp_WIRE_RATE,Weft_WIRE_RATE,SELL_RATE,i,j,
        l,WIDTH_1,WIDTH_2,WIDTH_3, LENGTH_1,LENGTH_2,LENGTH_3,                                                                                                                                                                                                                                        
        RPM,EFFICIENCY,SCRAPE_PERCENTAGE,
        b,c,d,e,f,g,q,k,
        m,n,o,p)
        cursor.execute(insertJalaram)
        connection.commit()

    tk.Button(root,text = 'Save',fg='black',bg='#32DE84' ,borderwidth = 5,takefocus=0,command = Save).place(x=615, y=230)

        
    #title        
     
    root.title("--Jᴀʟᴀʀᴀᴍ Wɪʀᴇᴍᴇsʜ Cᴏ.-->>>> WireMesh_Costing")
    ##

    #labels and entry

    Sr_Number_label = tk.Label(root,text='Sr Number', width=20 ,bg='#FFFF9F', anchor="w")
    Sr_Number_label.place(x=5, y=5)
    Sr_Number_entry = tk.Entry(root,textvariable = Sr_Number_var , font=('calibre',10,'normal'))
    Sr_Number_entry.place(x=150, y=5)


    Date_label = tk.Label(root,text='Date',bg='#FFC39B', width=20, anchor="w")
    Date_label.place(x=5, y=30)
    Date_entry = tk.Entry(root,textvariable =dt,takefocus=0 , font=('calibre',10,'normal'))
    Date_entry.place(x=150, y=30)

    Party_Name_label = tk.Label(root,text='Party Name',bg='#FFFF9F', width=20, anchor="w")
    Party_Name_label.place(x=5, y=55)
    Party_Name_entry = tk.Entry(root,textvariable =Party_Name_var , font=('calibre',10,'normal'))
    Party_Name_entry.place(x=150, y=55)

    Warp_MESH_label = tk.Label(root,text='Warp MESH',bg='#FFC39B', width=20, anchor="w")
    Warp_MESH_label.place(x=5, y=80)
    Warp_MESH_entry = tk.Entry(root,textvariable =Warp_MESH_var , font=('calibre',10,'normal'))
    Warp_MESH_entry.place(x=150, y=80)

    Weft_MESH_label = tk.Label(root,text='Weft MESH',bg='#FFFF9F', width=20, anchor="w")
    Weft_MESH_label.place(x=5, y=105)
    Weft_MESH_entry = tk.Entry(root,textvariable =Weft_MESH_var , font=('calibre',10,'normal'))
    Weft_MESH_entry.place(x=150, y=105)

    Warp_DIAMETER_label = tk.Label(root,text='Warp DIAMETER',bg='#FFC39B', width=20, anchor="w")
    Warp_DIAMETER_label.place(x=5, y=130)
    Warp_DIAMETER_entry = tk.Entry(root,textvariable =Warp_DIAMETER_var , font=('calibre',10,'normal'))
    Warp_DIAMETER_entry.place(x=150, y=130)

    Weft_DIAMETER_label = tk.Label(root,text='Weft DIAMETER',bg='#FFFF9F', width=20, anchor="w")
    Weft_DIAMETER_label.place(x=5, y=155)
    Weft_DIAMETER_entry = tk.Entry(root,textvariable =Weft_DIAMETER_var , font=('calibre',10,'normal'))
    Weft_DIAMETER_entry.place(x=150, y=155)

    Warp_GRADE_label = tk.Label(root,text='Warp GRADE',bg='#FFC39B', width=20, anchor="w")
    Warp_GRADE_label.place(x=5, y=180)
    Warp_GRADE_entry = tk.Entry(root,textvariable =Warp_GRADE_var , font=('calibre',10,'normal'))
    Warp_GRADE_entry.place(x=150, y=180)

    Weft_GRADE_label = tk.Label(root,text='Weft GRADE',bg='#FFFF9F', width=20, anchor="w")
    Weft_GRADE_label.place(x=5, y=205)
    Weft_GRADE_entry = tk.Entry(root,textvariable =Weft_GRADE_var , font=('calibre',10,'normal'))
    Weft_GRADE_entry.place(x=150, y=205)

    WIDTH_1_label = tk.Label(root,text='WIDTH-1 (in meter)',bg='#FFC39B', width=20, anchor="w")
    WIDTH_1_label.place(x=5, y=230)
    WIDTH_1_entry = tk.Entry(root,textvariable = WIDTH_1_var , font=('calibre',10,'normal'))
    WIDTH_1_entry.place(x=150, y=230)

    WIDTH_2_label = tk.Label(root,text='WIDTH-2 (in meter)',bg='#FFFF9F', width=20, anchor="w")
    WIDTH_2_label.place(x=5, y=255)
    WIDTH_2_entry = tk.Entry(root,textvariable =WIDTH_2_var , font=('calibre',10,'normal'))
    WIDTH_2_entry.place(x=150, y=255)

    WIDTH_3_label = tk.Label(root,text='WIDTH-3 (in meter)',bg='#FFC39B', width=20, anchor="w")
    WIDTH_3_label.place(x=5, y=280)
    WIDTH_3_entry = tk.Entry(root,textvariable = WIDTH_3_var , font=('calibre',10,'normal'))
    WIDTH_3_entry.place(x=150, y=280)

    LENGTH_1_label = tk.Label(root,text='LENGTH-1 (in meter)',bg='#FFFF9F', width=20, anchor="w")
    LENGTH_1_label.place(x=5, y=305)
    LENGTH_1_entry = tk.Entry(root,textvariable =LENGTH_1_var , font=('calibre',10,'normal'))
    LENGTH_1_entry.place(x=150, y=305)

    LENGTH_2_label = tk.Label(root,text='LENGTH-2 (in meter)',bg='#FFC39B', width=20, anchor="w")
    LENGTH_2_label.place(x=5, y=330)
    LENGTH_2_entry = tk.Entry(root,textvariable =LENGTH_2_var , font=('calibre',10,'normal'))
    LENGTH_2_entry.place(x=150, y=330)


    LENGTH_3_label = tk.Label(root,text='LENGTH-3 (in meter)',bg='#FFFF9F', width=20, anchor="w")
    LENGTH_3_label.place(x=5, y=355)
    LENGTH_3_entry = tk.Entry(root,textvariable =LENGTH_3_var , font=('calibre',10,'normal'))
    LENGTH_3_entry.place(x=150, y=355)

    Warp_WIRE_RATE_label = tk.Label(root,text='Warp WIRE RATE',bg='#FFC39B', width=20, anchor="w")
    Warp_WIRE_RATE_label.place(x=5, y=380)
    Warp_WIRE_RATE_entry = tk.Entry(root,textvariable =Warp_WIRE_RATE_var , font=('calibre',10,'normal'))
    Warp_WIRE_RATE_entry.place(x=150, y=380)

    Weft_WIRE_RATE_label = tk.Label(root,text='Weft WIRE RATE',bg='#FFFF9F', width=20, anchor="w")
    Weft_WIRE_RATE_label.place(x=5, y=405)
    Weft_WIRE_RATE_entry = tk.Entry(root,textvariable =Weft_WIRE_RATE_var , font=('calibre',10,'normal'))
    Weft_WIRE_RATE_entry.place(x=150, y=405)

    RPM_label = tk.Label(root,text='RPM',bg='#FFC39B', width=20, anchor="w")
    RPM_label.place(x=5, y=430)
    RPM_entry = tk.Entry(root,textvariable =RPM_var , font=('calibre',10,'normal'))
    RPM_entry.place(x=150, y=430)

    EFFICIENCY_label = tk.Label(root,text='EFFICIENCY',bg='#FFFF9F', width=20, anchor="w")
    EFFICIENCY_label.place(x=5, y=455)
    EFFICIENCY_entry = tk.Entry(root,textvariable =EFFICIENCY_var , font=('calibre',10,'normal'))
    EFFICIENCY_entry.place(x=150, y=455)

    SCRAPE_PERCENTAGE_label = tk.Label(root,text='SCRAPE PERCENTAGE',bg='#FFC39B', width=20, anchor="w")
    SCRAPE_PERCENTAGE_label.place(x=5, y=480)
    SCRAPE_PERCENTAGE_entry = tk.Entry(root,textvariable =SCRAPE_PERCENTAGE_var , font=('calibre',10,'normal'))
    SCRAPE_PERCENTAGE_entry.place(x=150, y=480)

    SELL_RATE_label = tk.Label(root,text='SELL RATE',bg='#FFFF9F', width=20, anchor="w")
    SELL_RATE_label.place(x=5, y=505)
    SELL_RATE_entry = tk.Entry(root,textvariable =SELL_RATE_var , font=('calibre',10,'normal'))
    SELL_RATE_entry.place(x=150, y=505)

    ##






    '''create table Jalaram(Sr_No bigint primary key , Date date,Party_Name varchar(50) , Warp_Mesh bigint not null , Weft_Mesh bigint not null , 
    Warp_Diameter decimal(10,3)not null , Weft_Diameter decimal(10,3) not null , Warp_Grade varchar(20), Weft_Grade varchar(20)  ,
    Warp_Wire_Rate bigint not null, Weft_Wire_Rate bigint not null , Sell_Rate_Rs bigint not null,
    RM_Value_Per_SqFt_Rs decimal(10,2) not null ,Difference_per_Sqft_Rs decimal(10,2) not null , Wire_Weight_per_SqMtr_Kg  decimal(10,2) not null ,
    Width_1 decimal(10,2) not null ,Width_2 decimal(10,2) not null,Width_3 decimal(10,2) not null, 
    Length_1 bigint not null,Length_2 bigint not null , Length_3 bigint not null ,
    RPM bigint not null, Efficiency bigint not null ,
    Scrape_percentage decimal(10,2) not null , 
    Warp_Wire_Qty_Kg bigint not null , Weft_Wire_Qty_Kg bigint not null, Total_Wire_Qty_Kg bigint not null , 
    RM_Wire_Value_Rs bigint not null , FG_Value_Rs bigint not null , Difference_Value_Rs bigint not null,
    Total_No_of_Days bigint not null,
    Diff_Percentage decimal(10,2) not null,
    Diff_per_day_1_Rs bigint not null , Diff_per_day_2_Rs bigint not null , Diff_per_day_3_Rs bigint not null , 
    Total_Sqft bigint not null);'''


    def RM_Value_Per_Sqft():
        Sr_Number=int(Sr_Number_var.get())
        Date=dt.get()
        Party_Name=Party_Name_var.get()
        Warp_MESH=float(Warp_MESH_var.get())
        Weft_MESH=float(Weft_MESH_var.get())
        Warp_DIAMETER=float(Warp_DIAMETER_var.get())
        Weft_DIAMETER=float(Weft_DIAMETER_var.get())
        Warp_GRADE=Warp_GRADE_var.get()
        Weft_GRADE=Weft_GRADE_var.get()
        WIDTH_1=float(WIDTH_1_var.get())
        WIDTH_2=float(WIDTH_2_var.get())
        WIDTH_3=float(WIDTH_3_var.get())
        LENGTH_1=float(LENGTH_1_var.get())
        LENGTH_2=float(LENGTH_2_var.get())
        LENGTH_3=float(LENGTH_3_var.get())
        Warp_WIRE_RATE=float(Warp_WIRE_RATE_var.get())
        Weft_WIRE_RATE=float(Weft_WIRE_RATE_var.get())
        RPM=float(RPM_var.get())
        EFFICIENCY=float(EFFICIENCY_var.get())
        SCRAPE_PERCENTAGE=float(SCRAPE_PERCENTAGE_var.get())        

        Sqft_1 = WIDTH_1*LENGTH_1*10.764
        Sqft_2 = WIDTH_2*LENGTH_2*10.764
        Sqft_3 = WIDTH_3*LENGTH_3*10.764

        Sqmtr_1 = WIDTH_1*LENGTH_1
        Sqmtr_2 = WIDTH_2*LENGTH_2
        Sqmtr_3 = WIDTH_3*LENGTH_3

        Warp_Wire_Quantity =(((Warp_DIAMETER*Warp_DIAMETER*0.493*Warp_MESH)/2)*((WIDTH_1*LENGTH_1)+(WIDTH_2*LENGTH_2)+(WIDTH_3*LENGTH_3)))*(1+(SCRAPE_PERCENTAGE/100))

        Weft_Wire_Quantity =(((Weft_DIAMETER*Weft_DIAMETER*0.493*Weft_MESH)/2)*((WIDTH_1*LENGTH_1)+(WIDTH_2*LENGTH_2)+(WIDTH_3*LENGTH_3)))*(1+(SCRAPE_PERCENTAGE/100))

        Total_Wire_Quantity = Warp_Wire_Quantity+Weft_Wire_Quantity

        RM_Wire_Value =(Warp_Wire_Quantity*Warp_WIRE_RATE)+(Weft_Wire_Quantity*Weft_WIRE_RATE)


        totalsqft=Sqft_1+Sqft_2+Sqft_3

        RM_Value_Per_Sqft = RM_Wire_Value/totalsqft



        
        f=Label(root, text="RM Value Per Sqft  :   Rs  "+ str(round(RM_Value_Per_Sqft,2)) ,font=("Arial", 12),bg='#2F9576',anchor=CENTER)
        f.place(x=525, y=185)
        
    tk.Button(root,text = 'Calculate_RM_Value_Per_Sqft',fg='black',bg='#E9E1CB' ,borderwidth = 5,takefocus=0,command = RM_Value_Per_Sqft).place(x=540, y=300)


    def Showall():


        r = tk.Tk()
        r.state("zoomed")
        r.geometry("1920x800")
        r.title("Jalaram Data")

        connect = mysql.connector.connect(host="localhost",user="root", passwd="0000",
          database="Jalaram")

        conn = connect.cursor()
        conn.execute("SELECT * FROM Jalaram ORDER BY Sr_No;")
        

        tree=ttk.Treeview(r,height=30)
        tree['show'] = 'headings'

        s = ttk.Style(r)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica',11))
        s.configure("Treeview.Heading", foreground='red',font=('Helvetica', 8,"bold"))

        # Define number of columns
        tree["columns"]=("Sr_Number","Date","Party_Name","Warp_MESH","Weft_MESH","Warp_DIA","Weft_DIA","Warp_GRADE"
                         ,"Weft_GRADE","Warp_WIRE_RATE","Weft_WIRE_RATE"
                         ,"SELL_RATE","RM_Value_Per_Sqft"
                         ,"Diff_per_Sqft","Wire_Weight_per_Sq_meter","WIDTH_1","WIDTH_2","WIDTH_3","LENGTH_1","LENGTH_2"
                         ,"LENGTH_3","RPM","EFFICIENCY","SCRAPE_PERCENTAGE","Warp_Wire_Quantity","Weft_Wire_Quantity"
                         ,"Total_Wire_Quantity","RM_Wire_Value","FG_Value","Diff_Value","Total_number_of_day","Diff_percentage"
                         ,"Diff_per_day_1","Diff_per_day_2","Diff_per_day_3"
                         ,"Total_SqFt")

        #Assign the width,minwidth and anchor to the respective columns
        tree.column("Sr_Number", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("Date", width=100, minwidth=100,anchor=tk.CENTER)
        tree.column("Party_Name", width=200, minwidth=200,anchor=tk.CENTER)
        tree.column("Warp_MESH", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_MESH", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_DIA", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_DIA", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_GRADE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_GRADE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_WIRE_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_WIRE_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("SELL_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Value_Per_Sqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_Sqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Wire_Weight_per_Sq_meter", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RPM", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("EFFICIENCY", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("SCRAPE_PERCENTAGE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Wire_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_number_of_day", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_SqFt", width=75, minwidth=75,anchor=tk.CENTER)

        #Assign the heading names to the respective columns
        tree.heading("Sr_Number", text="Sr No",anchor=tk.CENTER)
        tree.heading("Date", text="Date",anchor=tk.CENTER)
        tree.heading("Party_Name", text="Party Name",anchor=tk.CENTER)
        tree.heading("Warp_MESH", text="Warp Mesh",anchor=tk.CENTER)
        tree.heading("Weft_MESH", text="Weft Mesh",anchor=tk.CENTER)
        tree.heading("Warp_DIA", text="Warp Dia",anchor=tk.CENTER)
        tree.heading("Weft_DIA", text="Weft Dia",anchor=tk.CENTER)
        tree.heading("Warp_GRADE", text="Warp Grade",anchor=tk.CENTER)
        tree.heading("Weft_GRADE", text="Weft Grade",anchor=tk.CENTER)
        tree.heading("Warp_WIRE_RATE", text="Warp RATE",anchor=tk.CENTER)
        tree.heading("Weft_WIRE_RATE", text="Weft RATE",anchor=tk.CENTER)
        tree.heading("SELL_RATE", text="Sell Rate",anchor=tk.CENTER)
        tree.heading("RM_Value_Per_Sqft", text="RM/Sqft",anchor=tk.CENTER)
        tree.heading("Diff_per_Sqft", text="Diff/Sqft",anchor=tk.CENTER)
        tree.heading("Wire_Weight_per_Sq_meter", text="Wire_Wgt/SqMtr",anchor=tk.CENTER)
        tree.heading("WIDTH_1", text="WIDTH 1",anchor=tk.CENTER)
        tree.heading("WIDTH_2", text="WIDTH 2",anchor=tk.CENTER)
        tree.heading("WIDTH_3", text="WIDTH 3",anchor=tk.CENTER)
        tree.heading("LENGTH_1", text="LENGTH 1",anchor=tk.CENTER)
        tree.heading("LENGTH_2", text="LENGTH 2",anchor=tk.CENTER)
        tree.heading("LENGTH_3", text="LENGTH 3",anchor=tk.CENTER)
        tree.heading("RPM", text="RPM",anchor=tk.CENTER)
        tree.heading("EFFICIENCY", text="EFFI",anchor=tk.CENTER)
        tree.heading("SCRAPE_PERCENTAGE", text="SCRAPE %",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Quantity", text="Warp Qty",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Quantity", text="Weft Qty",anchor=tk.CENTER)
        tree.heading("Total_Wire_Quantity", text="Total Qty",anchor=tk.CENTER)
        tree.heading("RM_Wire_Value", text="RM Value",anchor=tk.CENTER)
        tree.heading("FG_Value", text="FG Value",anchor=tk.CENTER)
        tree.heading("Diff_Value", text="Diff Value",anchor=tk.CENTER)
        tree.heading("Total_number_of_day", text="Total Days",anchor=tk.CENTER)
        tree.heading("Diff_percentage", text="Diff %",anchor=tk.CENTER)
        tree.heading("Diff_per_day_1", text="Diff/day 1",anchor=tk.CENTER)
        tree.heading("Diff_per_day_2", text="Diff/day 2",anchor=tk.CENTER)
        tree.heading("Diff_per_day_3", text="Diff/day 3",anchor=tk.CENTER)
        tree.heading("Total_SqFt", text="Total SqFt",anchor=tk.CENTER)

        i = 0
        for ro in conn:
            if ro[0]%2==0:
                
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34],ro[35]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34],ro[35]),tags=("odd",))
            i = i + 1
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="white",background="black")

        hsb = ttk.Scrollbar(r,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(r,orient="vertical",)
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)

        tree.pack()

        def delete_data(tree):
            selected_item=tree.selection()[0]
            
            uid=tree.item(selected_item)['values'][0]
            del_query="DELETE FROM Jalaram WHERE Sr_No=%s"
            sel_data=(uid,)
            conn.execute(del_query,sel_data)
            connect.commit()
            tree.delete(selected_item)
            mb.showinfo("Success","Entry Deleted")

        deletebutton = tk.Button(r,text="delete",command=lambda:delete_data(tree))
        deletebutton.configure(font =('calibri', 14, 'bold'), bg = 'red',fg='white')
        deletebutton.place(x=300,y=670)        
        r.bind("<Escape>", lambda x: r.destroy())  
        r.mainloop()

          
    def sort():


        r = tk.Tk()
        r.state("zoomed")
        r.geometry("1920x800")
        r.title("SORTING DATA")

        connect = mysql.connector.connect(host="localhost",user="root", passwd="0000",
          database="Jalaram")

        conn = connect.cursor()

        while True:
            if clicked3.get() == "Option 2" and clicked4.get()=="" :
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get()) +'"' + ";" )
                    break
            if clicked5.get() == "Option 3" and clicked6.get()=="" :
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+";")                                                                               
                    break
            if clicked7.get() == "Option 4" and clicked8.get()=="" :
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+";")
                    break
            if clicked9.get() == "Option 5" and clicked10.get()=="" :                                                                                                                                                                                                                                                                             
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+" AND "+clicked7.get() + "=" + '"' + str(clicked8.get()) + '"'+";")
                    break
            if clicked11.get() == "Option 6" and clicked12.get()=="" :
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+" AND "+clicked7.get() + "=" + '"' + str(clicked8.get()) + '"'+ " AND "+clicked9.get() + "=" + '"' + str(clicked10.get()) + '"'+ ";")
                    break
            if clicked13.get() == "Option 7" and clicked14.get()=="" :
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+" AND "+clicked7.get() + "=" + '"' + str(clicked8.get()) + '"'+ " AND "+clicked9.get() + "=" + '"' + str(clicked10.get()) + '"'+" AND "+clicked11.get() + "=" + '"' + str(clicked12.get()) + '"'+ ";")                                                                                                                                                                                                                                                                                                                                  
                    break
            if clicked15.get() == "Option 8" and clicked16.get()=="" :
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+" AND "+clicked7.get() + "=" + '"' + str(clicked8.get()) + '"'+ " AND "+clicked9.get() + "=" + '"' + str(clicked10.get()) + '"'+" AND "+clicked11.get() + "=" + '"' + str(clicked12.get()) + '"'+" AND "+clicked13.get() + "=" + '"' + str(clicked14.get()) + '"'+";")
                    break
            else:
                    conn.execute("SELECT * FROM Jalaram WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+" AND "+clicked7.get() + "=" + '"' + str(clicked8.get()) + '"'+ " AND "+clicked9.get() + "=" + '"' + str(clicked10.get()) + '"'+" AND "+clicked11.get() + "=" + '"' + str(clicked12.get()) + '"'+" AND "+clicked13.get() + "=" + '"' + str(clicked14.get()) + '"'+" AND "+clicked15.get() + "=" + '"' + str(clicked16.get()) + '"'+";")

        tree=ttk.Treeview(r,height=30)
        tree['show'] = 'headings'

        s = ttk.Style(r)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica',11))
        s.configure("Treeview.Heading", foreground='red',font=('Helvetica', 8,"bold"))

        # Define number of columns
        tree["columns"]=("Sr_Number","Date","Party_Name","Warp_MESH","Weft_MESH","Warp_DIA","Weft_DIA","Warp_GRADE"
                         ,"Weft_GRADE","Warp_WIRE_RATE","Weft_WIRE_RATE"
                         ,"SELL_RATE","RM_Value_Per_Sqft"
                         ,"Diff_per_Sqft","Wire_Weight_per_Sq_meter","WIDTH_1","WIDTH_2","WIDTH_3","LENGTH_1","LENGTH_2"
                         ,"LENGTH_3","RPM","EFFICIENCY","SCRAPE_PERCENTAGE","Warp_Wire_Quantity","Weft_Wire_Quantity"
                         ,"Total_Wire_Quantity","RM_Wire_Value","FG_Value","Diff_Value","Total_number_of_day","Diff_percentage"
                         ,"Diff_per_day_1","Diff_per_day_2","Diff_per_day_3"
                         ,"Total_SqFt")

        #Assign the width,minwidth and anchor to the respective columns
        tree.column("Sr_Number", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("Date", width=100, minwidth=100,anchor=tk.CENTER)
        tree.column("Party_Name", width=200, minwidth=200,anchor=tk.CENTER)
        tree.column("Warp_MESH", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_MESH", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_DIA", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_DIA", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_GRADE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_GRADE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_WIRE_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_WIRE_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("SELL_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Value_Per_Sqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_Sqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Wire_Weight_per_Sq_meter", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RPM", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("EFFICIENCY", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("SCRAPE_PERCENTAGE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Wire_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_number_of_day", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_SqFt", width=75, minwidth=75,anchor=tk.CENTER)

        #Assign the heading names to the respective columns
        tree.heading("Sr_Number", text="Sr No",anchor=tk.CENTER)
        tree.heading("Date", text="Date",anchor=tk.CENTER)
        tree.heading("Party_Name", text="Party Name",anchor=tk.CENTER)
        tree.heading("Warp_MESH", text="Warp Mesh",anchor=tk.CENTER)
        tree.heading("Weft_MESH", text="Weft Mesh",anchor=tk.CENTER)
        tree.heading("Warp_DIA", text="Warp Dia",anchor=tk.CENTER)
        tree.heading("Weft_DIA", text="Weft Dia",anchor=tk.CENTER)
        tree.heading("Warp_GRADE", text="Warp Grade",anchor=tk.CENTER)
        tree.heading("Weft_GRADE", text="Weft Grade",anchor=tk.CENTER)
        tree.heading("Warp_WIRE_RATE", text="Warp RATE",anchor=tk.CENTER)
        tree.heading("Weft_WIRE_RATE", text="Weft RATE",anchor=tk.CENTER)
        tree.heading("SELL_RATE", text="Sell Rate",anchor=tk.CENTER)
        tree.heading("RM_Value_Per_Sqft", text="RM/Sqft",anchor=tk.CENTER)
        tree.heading("Diff_per_Sqft", text="Diff/Sqft",anchor=tk.CENTER)
        tree.heading("Wire_Weight_per_Sq_meter", text="Wire_Wgt/SqMtr",anchor=tk.CENTER)
        tree.heading("WIDTH_1", text="WIDTH 1",anchor=tk.CENTER)
        tree.heading("WIDTH_2", text="WIDTH 2",anchor=tk.CENTER)
        tree.heading("WIDTH_3", text="WIDTH 3",anchor=tk.CENTER)
        tree.heading("LENGTH_1", text="LENGTH 1",anchor=tk.CENTER)
        tree.heading("LENGTH_2", text="LENGTH 2",anchor=tk.CENTER)
        tree.heading("LENGTH_3", text="LENGTH 3",anchor=tk.CENTER)
        tree.heading("RPM", text="RPM",anchor=tk.CENTER)
        tree.heading("EFFICIENCY", text="EFFI",anchor=tk.CENTER)
        tree.heading("SCRAPE_PERCENTAGE", text="SCRAPE %",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Quantity", text="Warp Qty",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Quantity", text="Weft Qty",anchor=tk.CENTER)
        tree.heading("Total_Wire_Quantity", text="Total Qty",anchor=tk.CENTER)
        tree.heading("RM_Wire_Value", text="RM Value",anchor=tk.CENTER)
        tree.heading("FG_Value", text="FG Value",anchor=tk.CENTER)
        tree.heading("Diff_Value", text="Diff Value",anchor=tk.CENTER)
        tree.heading("Total_number_of_day", text="Total Days",anchor=tk.CENTER)
        tree.heading("Diff_percentage", text="Diff %",anchor=tk.CENTER)
        tree.heading("Diff_per_day_1", text="Diff/day 1",anchor=tk.CENTER)
        tree.heading("Diff_per_day_2", text="Diff/day 2",anchor=tk.CENTER)
        tree.heading("Diff_per_day_3", text="Diff/day 3",anchor=tk.CENTER)
        tree.heading("Total_SqFt", text="Total SqFt",anchor=tk.CENTER)

        i = 0
        for ro in conn:
            if ro[0]%2==0:
                
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34],ro[35]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34],ro[35]),tags=("odd",))
            i = i + 1
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="white",background="black")

        hsb = ttk.Scrollbar(r,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(r,orient="vertical",)
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)

        tree.pack()

        def delete_data(tree):
            selected_item=tree.selection()[0]
            
            uid=tree.item(selected_item)['values'][0]
            del_query="DELETE FROM Jalaram WHERE Sr_No=%s"
            sel_data=(uid,)
            conn.execute(del_query,sel_data)
            connect.commit()
            tree.delete(selected_item)
            mb.showinfo("Success","Entry Deleted")

        deletebutton = tk.Button(r,text="delete",command=lambda:delete_data(tree))
        deletebutton.configure(font =('calibri', 14, 'bold'), bg = 'red',fg='white')
        deletebutton.place(x=300,y=670)        
        r.bind("<Escape>", lambda x: r.destroy())  
        r.mainloop()

    options = [
                
                "Sr_No",
                "Date",
                "Party_Name",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Warp_Wire_Rate",
                "Weft_Wire_Rate",
                "Sell_Rate_Rs",
                "RM_Value_Per_SqFt_Rs",
                "Wire_Weight_per_SqMtr_Kg",
                "Diff_per_day_1_Rs",
                "Diff_per_day_2_Rs",
                "Diff_per_day_3_Rs",
              
            ]

    clicked0 = StringVar()
    clicked0.set("Order by")
    OptionMenu( root , clicked0 , *options ).place(x=1285, y = 300)



    def order():


        r = tk.Tk()
        r.state("zoomed")
        r.geometry("1920x800")
        r.title("ORDERING DATA")

        connect = mysql.connector.connect(host="localhost",user="root", passwd="0000",
          database="Jalaram")

        conn = connect.cursor()

        conn.execute("SELECT * FROM Jalaram ORDER BY " + clicked0.get() + ";")

        tree=ttk.Treeview(r,height=30)
        tree['show'] = 'headings'

        s = ttk.Style(r)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica',11))
        s.configure("Treeview.Heading", foreground='red',font=('Helvetica', 8,"bold"))

        # Define number of columns
        tree["columns"]=("Sr_Number","Date","Party_Name","Warp_MESH","Weft_MESH","Warp_DIA","Weft_DIA","Warp_GRADE"
                         ,"Weft_GRADE","Warp_WIRE_RATE","Weft_WIRE_RATE"
                         ,"SELL_RATE","RM_Value_Per_Sqft"
                         ,"Diff_per_Sqft","Wire_Weight_per_Sq_meter","WIDTH_1","WIDTH_2","WIDTH_3","LENGTH_1","LENGTH_2"
                         ,"LENGTH_3","RPM","EFFICIENCY","SCRAPE_PERCENTAGE","Warp_Wire_Quantity","Weft_Wire_Quantity"
                         ,"Total_Wire_Quantity","RM_Wire_Value","FG_Value","Diff_Value","Total_number_of_day","Diff_percentage"
                         ,"Diff_per_day_1","Diff_per_day_2","Diff_per_day_3"
                         ,"Total_SqFt")

        #Assign the width,minwidth and anchor to the respective columns
        tree.column("Sr_Number", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("Date", width=100, minwidth=100,anchor=tk.CENTER)
        tree.column("Party_Name", width=200, minwidth=200,anchor=tk.CENTER)
        tree.column("Warp_MESH", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_MESH", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_DIA", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_DIA", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_GRADE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_GRADE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_WIRE_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_WIRE_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("SELL_RATE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Value_Per_Sqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_Sqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Wire_Weight_per_Sq_meter", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("WIDTH_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("LENGTH_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RPM", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("EFFICIENCY", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("SCRAPE_PERCENTAGE", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_Wire_Quantity", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Wire_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_number_of_day", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Diff_per_day_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Total_SqFt", width=75, minwidth=75,anchor=tk.CENTER)

        #Assign the heading names to the respective columns
        tree.heading("Sr_Number", text="Sr No",anchor=tk.CENTER)
        tree.heading("Date", text="Date",anchor=tk.CENTER)
        tree.heading("Party_Name", text="Party Name",anchor=tk.CENTER)
        tree.heading("Warp_MESH", text="Warp Mesh",anchor=tk.CENTER)
        tree.heading("Weft_MESH", text="Weft Mesh",anchor=tk.CENTER)
        tree.heading("Warp_DIA", text="Warp Dia",anchor=tk.CENTER)
        tree.heading("Weft_DIA", text="Weft Dia",anchor=tk.CENTER)
        tree.heading("Warp_GRADE", text="Warp Grade",anchor=tk.CENTER)
        tree.heading("Weft_GRADE", text="Weft Grade",anchor=tk.CENTER)
        tree.heading("Warp_WIRE_RATE", text="Warp RATE",anchor=tk.CENTER)
        tree.heading("Weft_WIRE_RATE", text="Weft RATE",anchor=tk.CENTER)
        tree.heading("SELL_RATE", text="Sell Rate",anchor=tk.CENTER)
        tree.heading("RM_Value_Per_Sqft", text="RM/Sqft",anchor=tk.CENTER)
        tree.heading("Diff_per_Sqft", text="Diff/Sqft",anchor=tk.CENTER)
        tree.heading("Wire_Weight_per_Sq_meter", text="Wire_Wgt/SqMtr",anchor=tk.CENTER)
        tree.heading("WIDTH_1", text="WIDTH 1",anchor=tk.CENTER)
        tree.heading("WIDTH_2", text="WIDTH 2",anchor=tk.CENTER)
        tree.heading("WIDTH_3", text="WIDTH 3",anchor=tk.CENTER)
        tree.heading("LENGTH_1", text="LENGTH 1",anchor=tk.CENTER)
        tree.heading("LENGTH_2", text="LENGTH 2",anchor=tk.CENTER)
        tree.heading("LENGTH_3", text="LENGTH 3",anchor=tk.CENTER)
        tree.heading("RPM", text="RPM",anchor=tk.CENTER)
        tree.heading("EFFICIENCY", text="EFFI",anchor=tk.CENTER)
        tree.heading("SCRAPE_PERCENTAGE", text="SCRAPE %",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Quantity", text="Warp Qty",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Quantity", text="Weft Qty",anchor=tk.CENTER)
        tree.heading("Total_Wire_Quantity", text="Total Qty",anchor=tk.CENTER)
        tree.heading("RM_Wire_Value", text="RM Value",anchor=tk.CENTER)
        tree.heading("FG_Value", text="FG Value",anchor=tk.CENTER)
        tree.heading("Diff_Value", text="Diff Value",anchor=tk.CENTER)
        tree.heading("Total_number_of_day", text="Total Days",anchor=tk.CENTER)
        tree.heading("Diff_percentage", text="Diff %",anchor=tk.CENTER)
        tree.heading("Diff_per_day_1", text="Diff/day 1",anchor=tk.CENTER)
        tree.heading("Diff_per_day_2", text="Diff/day 2",anchor=tk.CENTER)
        tree.heading("Diff_per_day_3", text="Diff/day 3",anchor=tk.CENTER)
        tree.heading("Total_SqFt", text="Total SqFt",anchor=tk.CENTER)

        i = 0
        for ro in conn:
            if ro[0]%2==0:
                
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34],ro[35]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34],ro[35]),tags=("odd",))
            i = i + 1
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="white",background="black")

        hsb = ttk.Scrollbar(r,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(r,orient="vertical",)
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)

        tree.pack()

        def delete_data(tree):
            selected_item=tree.selection()[0]
            
            uid=tree.item(selected_item)['values'][0]
            del_query="DELETE FROM Jalaram WHERE Sr_No=%s"
            sel_data=(uid,)
            conn.execute(del_query,sel_data)
            connect.commit()
            tree.delete(selected_item)
            mb.showinfo("Success","Entry Deleted")

        deletebutton = tk.Button(r,text="delete",command=lambda:delete_data(tree))
        deletebutton.configure(font =('calibri', 14, 'bold'), bg = 'red',fg='white')
        deletebutton.place(x=300,y=670)        
        r.bind("<Escape>", lambda x: r.destroy())  
        r.mainloop()
    tk.Button(root,text = 'Order Data',fg='black',bg='#0088FC' ,borderwidth = 5,takefocus=0,command = order).place(x=1295, y=350)
    tk.Button(root,text = 'Sort Data',fg='black',bg='#0088FC' ,borderwidth = 5,takefocus=0,command = sort).place(x=700, y=700)
    tk.Button(root,text = 'Show_All',fg='black',bg='#0088FC' ,borderwidth = 5,takefocus=0,command = Showall).place(x=700, y=230)
    #submit button
    def enter_button(event):
        calculate()

    root.bind('<Return>', enter_button)
    root.bind('<Control-o>', close)

    sub_btn=tk.Button(root,text = 'Calculate',fg='black',bg='red' ,borderwidth = 5,takefocus=0,command = calculate).place(x=500, y=230)
    
    root.mainloop()

Button(j,text = 'WireMesh Costing',font=("Kokila",20),fg='black',bg='#5CB4F3' ,borderwidth = 10,takefocus=0,command = Wire_mesh_Costing).place(x=350, y=500)

#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

def Yellow_Card() :
    j.destroy()    
    root=tk.Tk()
    root.geometry("1200x550")
    root.state("zoomed")
    root.configure(bg='#EDE8DF')

    canvas = Canvas(root, width=2000, height=2000,bg='#EDE8DF')
    canvas.pack()
    canvas.create_rectangle(2, 2, 1175, 530)

    root.title('''--Jᴀʟᴀʀᴀᴍ Wɪʀᴇᴍᴇsʜ Cᴏ.-->>>>YELLOW CARD''')



    today = date.today()
    dt1 = str(today)
    dt = StringVar(root, value=dt1)


    options = [
                "Program_No",
                "Machine_No",
                "Date",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Wgt_Diff_per_SqMtr",

              
            ]
              
    options1 = [
                "Option 1",
                "Program_No",
                "Machine_No",
                "Date",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Wgt_Diff_per_SqMtr",

              
            ]
    options2 = [
                "Option 2",
                "Program_No",
                "Machine_No",
                "Date",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Wgt_Diff_per_SqMtr",

              
            ]
    options3 = [
                "Option 3",
                "Program_No",
                "Machine_No",
                "Date",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Wgt_Diff_per_SqMtr",

              
            ]
    options4 = [
                "Option 4",
                "Program_No",
                "Machine_No",
                "Date",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Wgt_Diff_per_SqMtr",

              
            ]
    options5 = [
                "Option 5",
                "Program_No",
                "Machine_No",
                "Date",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Wgt_Diff_per_SqMtr",

              
            ]

    # datatype of menu text
    clicked1 = StringVar()
    clicked2 = StringVar()
    clicked3 = StringVar()
    clicked4 = StringVar()
    clicked5 = StringVar()
    clicked6 = StringVar()
    clicked7 = StringVar()
    clicked8 = StringVar()
    clicked9 = StringVar()
    clicked10 = StringVar()





    clicked1.set("Option 1")
    clicked3.set("Option 2")
    clicked5.set("Option 3")
    clicked7.set("Option 4")
    clicked9.set("Option 5")


              

    OptionMenu( root , clicked1 , *options1 ).place(x=10, y = 550)
    Entry(root,textvariable = clicked2,takefocus=0  ).place(x=10, y = 580)
    OptionMenu( root , clicked3 , *options2 ).place(x=200, y = 550)
    Entry(root,textvariable = clicked4,takefocus=0  ).place(x=200, y = 580)
    OptionMenu( root , clicked5 , *options3 ).place(x=390, y = 550)
    Entry(root,textvariable = clicked6,takefocus=0  ).place(x=390, y = 580)
    OptionMenu( root , clicked7 , *options4 ).place(x=580, y = 550)
    Entry(root,textvariable = clicked8,takefocus=0  ).place(x=580, y = 580)
    OptionMenu( root , clicked9 , *options5 ).place(x=770, y = 550)
    Entry(root,textvariable = clicked10,takefocus=0  ).place(x=770, y = 580)





    Machine_No_var = tk.StringVar()
    Program_No_var = tk.StringVar()
    Warp_Mesh_var=tk.StringVar()
    Weft_Mesh_var=tk.StringVar()
    Warp_Dia_var=tk.StringVar()
    Weft_Dia_var=tk.StringVar()
    Warp_Grade_var=tk.StringVar()
    Weft_Grade_var=tk.StringVar()
    Length_1_var=tk.StringVar()
    Length_2_var=tk.StringVar()
    Length_3_var=tk.StringVar()
    Width_1_var=tk.StringVar()
    Width_2_var=tk.StringVar()
    Width_3_var=tk.StringVar()
    Actual_Wgt_var=tk.StringVar()
    Warp_Wire_Price_var=tk.StringVar()
    Weft_Wire_Price_var=tk.StringVar()
    Scrap_var=tk.StringVar()
    Sell_Rate_var=tk.StringVar()


    Program_No_label = tk.Label(root,text='Program No', width=20 ,bg='#E0BBE4', anchor="w")
    Program_No_label.place(x=5, y=5)
    Program_No_entry = tk.Entry(root,textvariable = Program_No_var , font=('calibre',10,'normal'))
    Program_No_entry.place(x=150, y=5)


    Machine_No_label = tk.Label(root,text='Machine No',bg='#9FF2FF', width=20, anchor="w")
    Machine_No_label.place(x=5, y=30)
    Machine_No_entry = tk.Entry(root,textvariable = Machine_No_var , font=('calibre',10,'normal'))
    Machine_No_entry.place(x=150, y=30)

    Date_label = tk.Label(root,text='Date',bg='#E0BBE4', width=20, anchor="w")
    Date_label.place(x=5, y=55)
    Date_entry = tk.Entry(root,textvariable = dt,takefocus=0 , font=('calibre',10,'normal'))
    Date_entry.place(x=150, y=55)

    Warp_Mesh_label = tk.Label(root,text='Warp Mesh', width=20 ,bg='#9FF2FF', anchor="w")
    Warp_Mesh_label.place(x=5, y=80)
    Warp_Mesh_entry = tk.Entry(root,textvariable = Warp_Mesh_var , font=('calibre',10,'normal'))
    Warp_Mesh_entry.place(x=150, y=80)

    Weft_Mesh_label = tk.Label(root,text='Weft Mesh',bg='#E0BBE4', width=20, anchor="w")
    Weft_Mesh_label.place(x=5, y=105)
    Weft_Mesh_entry = tk.Entry(root,textvariable = Weft_Mesh_var , font=('calibre',10,'normal'))
    Weft_Mesh_entry.place(x=150, y=105)

    Warp_Dia_label = tk.Label(root,text='Warp Diameter',bg='#9FF2FF', width=20, anchor="w")
    Warp_Dia_label.place(x=5, y=130)
    Warp_Dia_entry = tk.Entry(root,textvariable = Warp_Dia_var , font=('calibre',10,'normal'))
    Warp_Dia_entry.place(x=150, y=130)

    Weft_Dia_label = tk.Label(root,text='Weft Diameter',bg='#E0BBE4', width=20, anchor="w")
    Weft_Dia_label.place(x=5, y=155)
    Weft_Dia_entry = tk.Entry(root,textvariable = Weft_Dia_var , font=('calibre',10,'normal'))
    Weft_Dia_entry.place(x=150, y=155)


    Warp_Grade_label = tk.Label(root,text='Warp Grade',bg='#9FF2FF', width=20, anchor="w")
    Warp_Grade_label.place(x=5, y=180)
    Warp_Grade_entry = tk.Entry(root,textvariable = Warp_Grade_var , font=('calibre',10,'normal'))
    Warp_Grade_entry.place(x=150, y=180)

    Weft_Grade_label = tk.Label(root,text='Weft Grade',bg='#E0BBE4', width=20, anchor="w")
    Weft_Grade_label.place(x=5, y=205)
    Weft_Grade_entry = tk.Entry(root,textvariable = Weft_Grade_var , font=('calibre',10,'normal'))
    Weft_Grade_entry.place(x=150, y=205)

    Width_1_label = tk.Label(root,text='Width 1',bg='#9FF2FF', width=20, anchor="w")
    Width_1_label.place(x=5, y=230)
    Width_1_entry = tk.Entry(root,textvariable = Width_1_var, font=('calibre',10,'normal'))
    Width_1_entry.place(x=150, y=230)

    Width_2_label = tk.Label(root,text='Width 2',bg='#E0BBE4', width=20, anchor="w")
    Width_2_label.place(x=5, y=255)
    Width_2_entry = tk.Entry(root,textvariable = Width_2_var , font=('calibre',10,'normal'))
    Width_2_entry.place(x=150, y=255)

    Width_3_label = tk.Label(root,text='Width 3',bg='#9FF2FF', width=20, anchor="w")
    Width_3_label.place(x=5, y=280)
    Width_3_entry = tk.Entry(root,textvariable = Width_3_var , font=('calibre',10,'normal'))
    Width_3_entry.place(x=150, y=280)

    Length_1_label = tk.Label(root,text='Length 1',bg='#E0BBE4', width=20, anchor="w")
    Length_1_label.place(x=5, y=305)
    Length_1_entry = tk.Entry(root,textvariable =Length_1_var , font=('calibre',10,'normal'))
    Length_1_entry.place(x=150, y=305)

    Length_2_label = tk.Label(root,text='Length 2',bg='#9FF2FF', width=20, anchor="w")
    Length_2_label.place(x=5, y=330)
    Length_2_entry = tk.Entry(root,textvariable =Length_2_var , font=('calibre',10,'normal'))
    Length_2_entry.place(x=150, y=330)

    Length_3_label = tk.Label(root,text='Length 3',bg='#E0BBE4', width=20, anchor="w")
    Length_3_label.place(x=5, y=355)
    Length_3_entry = tk.Entry(root,textvariable =Length_3_var , font=('calibre',10,'normal'))
    Length_3_entry.place(x=150, y=355)

    Actual_Wgt_label = tk.Label(root,text='Actual Wgt',bg='#9FF2FF', width=20, anchor="w")
    Actual_Wgt_label.place(x=5, y=380)
    Actual_Wgt_entry = tk.Entry(root,textvariable = Actual_Wgt_var , font=('calibre',10,'normal'))
    Actual_Wgt_entry.place(x=150, y=380)

    Warp_Wire_Price_label = tk.Label(root,text='Warp Wire Price in Kg',bg='#E0BBE4', width=20, anchor="w")
    Warp_Wire_Price_label.place(x=5, y=405)
    Warp_Wire_Price_entry = tk.Entry(root,textvariable = Warp_Wire_Price_var , font=('calibre',10,'normal'))
    Warp_Wire_Price_entry.place(x=150, y=405)

    Weft_Wire_Price_label = tk.Label(root,text='Weft Wire Price in Kg',bg='#9FF2FF', width=20, anchor="w")
    Weft_Wire_Price_label.place(x=5, y=430)
    Weft_Wire_Price_entry = tk.Entry(root,textvariable = Weft_Wire_Price_var , font=('calibre',10,'normal'))
    Weft_Wire_Price_entry.place(x=150, y=430)

    Sell_Rate_label = tk.Label(root,text='Sell Rate',bg='#E0BBE4', width=20, anchor="w")
    Sell_Rate_label.place(x=5, y=455)
    Sell_Rate_entry = tk.Entry(root,textvariable =Sell_Rate_var , font=('calibre',10,'normal'))
    Sell_Rate_entry.place(x=150, y=455)

    Scrap_label = tk.Label(root,text='Scrap in Kg',bg='#9FF2FF', width=20, anchor="w")
    Scrap_label.place(x=5, y=480)
    Scrap_entry = tk.Entry(root,textvariable = Scrap_var , font=('calibre',10,'normal'))
    Scrap_entry.place(x=150, y=480)




    def calculate():
        Machine_No=int(Machine_No_var.get())
        Program_No=str(Program_No_var.get())
        Date=dt.get()
        Warp_Mesh=float(Warp_Mesh_var.get())
        Weft_Mesh=float(Weft_Mesh_var.get())
        Warp_Dia=float(Warp_Dia_var.get())
        Weft_Dia=float(Weft_Dia_var.get())
        Warp_Grade=str(Warp_Grade_var.get())
        Weft_Grade=str(Weft_Grade_var.get())
        Width_1=float(Width_1_var.get())
        Width_2=float(Width_2_var.get())
        Width_3=float(Width_3_var.get())
        Length_1=float(Length_1_var.get())
        Length_2=float(Length_2_var.get())
        Length_3=float(Length_3_var.get())
        Warp_Wire_Price=float(Warp_Wire_Price_var.get())
        Weft_Wire_Price=float(Weft_Wire_Price_var.get())
        Actual_Wgt=float(Actual_Wgt_var.get())
        Scrap=float(Scrap_var.get())
        Sell_Rate=float(Sell_Rate_var.get())
       
        
                
        
        ##FORMULA

        Warp_Wire_Wgt_per_Sqmtr = ((Warp_Dia*Warp_Dia*0.493*Warp_Mesh)/2)

        Weft_Wire_Wgt_per_Sqmtr  =((Weft_Dia*Weft_Dia*0.493*Weft_Mesh)/2)

        Formula_Wire_Wgt = Warp_Wire_Wgt_per_Sqmtr + Weft_Wire_Wgt_per_Sqmtr

        Actual_Wgt_per_SqMtr= (Actual_Wgt)/(Width_1*Length_1+Width_2*Length_2+Width_3*Length_3)

        Wgt_Diff_per_SqMtr = Formula_Wire_Wgt - Actual_Wgt_per_SqMtr

        Warp_Wire_Wgt =((Warp_Dia*Warp_Dia*0.493*Warp_Mesh)/2)*((Width_1*Length_1)+(Width_2*Length_2)+(Width_3*Length_3))

        Weft_Wire_Wgt =((Weft_Dia*Weft_Dia*0.493*Weft_Mesh)/2)*((Width_1*Length_1)+(Width_2*Length_2)+(Width_3*Length_3))

        Total_Wire_Wgt = Warp_Wire_Wgt + Weft_Wire_Wgt


        totalsqft = ((Width_1*Length_1)+(Width_2*Length_2)+(Width_3*Length_3))*10.764 

        Actual_Warp_Wire_Wgt_per_SqMtr = (((Warp_Wire_Wgt_per_Sqmtr)/(Formula_Wire_Wgt))*((Actual_Wgt_per_SqMtr)))/1.04
        
        Actual_Weft_Wire_Wgt_per_SqMtr = Actual_Wgt_per_SqMtr - Actual_Warp_Wire_Wgt_per_SqMtr

        Actual_Warp_Dia = sqrt((Actual_Warp_Wire_Wgt_per_SqMtr*2)/ (0.493*Warp_Mesh))

        Actual_Weft_Dia = sqrt((Actual_Weft_Wire_Wgt_per_SqMtr*2)/ (0.493*Weft_Mesh))


        Avg_Actual_Dia =  sqrt((Actual_Wgt_per_SqMtr)/ (0.493*Warp_Mesh))


        Warp_Wire_Cost =  Warp_Wire_Price * (Actual_Warp_Wire_Wgt_per_SqMtr/10.764)+(Scrap*Weft_Wire_Price)/(totalsqft*2)
        
        Weft_Wire_Cost =  Weft_Wire_Price * (Actual_Weft_Wire_Wgt_per_SqMtr/10.764)+(Scrap*Weft_Wire_Price)/(totalsqft*2)

        Wire_Cost_per_Sqft = Warp_Wire_Cost+Weft_Wire_Cost

        Scrap_Percentage = (Scrap*100)/ (Actual_Wgt+Scrap)

        RM_Value = (Actual_Wgt+Scrap)*(Weft_Wire_Price)

        FG_Value = Sell_Rate*totalsqft

        FG_Diff_Value = FG_Value - RM_Value

        FG_Percentage = (FG_Diff_Value / RM_Value)*100

        Actual_Wgt_per_400_sqft =  (Actual_Wgt/totalsqft)*400

        
        one=Label(root, text="        Formula Wire Wt  :           " + str(round(Formula_Wire_Wgt,3))+ " Kg ",font=("Arial", 12),bg='#FFDAB3', width=40, anchor="w",borderwidth=2, relief="solid")
        one.place(x=800, y=10)
        two=Label(root, text="        Actual Wt per SqMtr  :      " + str(round(Actual_Wgt_per_SqMtr,3))+ " Kg ", font=("Arial", 12),bg='#FFDAB3', width=40, anchor="w",borderwidth=2, relief="solid")
        two.place(x=800, y=35)
        three=Label(root, text="        Wgt Diff per SqMtr  :          " + str(round(Wgt_Diff_per_SqMtr,3))+ " Kg ",font=("Arial", 12),bg='#FFDAB3', width=40, anchor="w",borderwidth=2, relief="solid")
        three.place(x=800, y=60)
        four=Label(root, text="        Actual Warp Dia  :  " + str(round(Actual_Warp_Dia,3))+ " mm ",font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        four.place(x=800, y=85)
        five=Label(root, text="        Actual Weft Dia  :    " + str(round(Actual_Weft_Dia,3))+ " mm ",font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        five.place(x=800, y=110)

        sixteen=Label(root, text="        Avg Actual Dia  :    " + str(round(Avg_Actual_Dia,3))+ " mm ",font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        sixteen.place(x=800, y=135)

        six=Label(root, text="        Warp Wire Cost  :    Rs    " + str(round(Warp_Wire_Cost,3)),font=("Arial", 12),bg='#F6E1EA', width=40, anchor="w",borderwidth=2, relief="solid")
        six.place(x=800, y=160)

        eight=Label(root, text="       Weft Wire Cost  :       Rs    " + str(round(Weft_Wire_Cost,3)),font=("Arial", 12),bg='#F6E1EA', width=40, anchor="w",borderwidth=2, relief="solid")
        eight.place(x=800, y=210)

        nine=Label(root, text="       Wire Cost per Sqft  : Rs    " + str(round(Wire_Cost_per_Sqft,3)),font=("Arial", 12),bg='#F6E1EA', width=40, anchor="w",borderwidth=2, relief="solid")
        nine.place(x=800, y=185)
        seven=Label(root, text="        Scrap Percentage  :  " + str(round(Scrap_Percentage,3))+ " % ",font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        seven.place(x=800, y=235)

        
        ten=Label(root, text="        Total Sqft  : Rs     " + str(round(totalsqft)),font=("Arial", 12),bg='#C8E0FD', width=40, anchor="w",borderwidth=2, relief="solid")
        ten.place(x=800, y=260)    

        eleven=Label(root, text="        RM Value :  Rs     " + str(round(RM_Value)),font=("Arial", 12),bg='#8FC883', width=40, anchor="w",borderwidth=2, relief="solid")
        eleven.place(x=800, y=285)

        twelve=Label(root, text="        FG Value  :  Rs    " + str(round(FG_Value)),font=("Arial", 12),bg='#8FC883', width=40, anchor="w",borderwidth=2, relief="solid")
        twelve.place(x=800, y=310)    


        thirteen=Label(root, text="        FG Diff Value  :   Rs    " + str(round(FG_Diff_Value)),font=("Arial", 12),bg='#8FC883', width=40, anchor="w",borderwidth=2, relief="solid")
        thirteen.place(x=800, y=335)

        fourteen=Label(root, text="        FG_Percentage  :  " + str(round(FG_Percentage))+ " % ",font=("Arial", 12),bg='#FFFDD1', width=40, anchor="w",borderwidth=2, relief="solid")
        fourteen.place(x=800, y=360)


        fifteen=Label(root, text="        Actual Wgt per 400 Sqft :   Rs   " + str(round(Actual_Wgt_per_400_sqft,2)),font=("Arial", 12),bg='#FFFDD1', width=40, anchor="w",borderwidth=2, relief="solid")
        fifteen.place(x=800, y=385)



    sub_btn = tk.Button(root,text = 'Calculate',fg='black',bg='red' ,borderwidth = 5,takefocus=0,command = calculate).place(x=400, y=230)



    def Save():
        Machine_No=int(Machine_No_var.get())
        Program_No=str(Program_No_var.get())
        Date=dt.get()
        Warp_Mesh=float(Warp_Mesh_var.get())
        Weft_Mesh=float(Weft_Mesh_var.get())
        Warp_Dia=float(Warp_Dia_var.get())
        Weft_Dia=float(Weft_Dia_var.get())
        Warp_Grade=str(Warp_Grade_var.get())
        Weft_Grade=str(Weft_Grade_var.get())
        Width_1=float(Width_1_var.get())
        Width_2=float(Width_2_var.get())
        Width_3=float(Width_3_var.get())
        Length_1=float(Length_1_var.get())
        Length_2=float(Length_2_var.get())
        Length_3=float(Length_3_var.get())
        Warp_Wire_Price=float(Warp_Wire_Price_var.get())
        Weft_Wire_Price=float(Weft_Wire_Price_var.get())
        Actual_Wgt=float(Actual_Wgt_var.get())
        Scrap=float(Scrap_var.get())
        Sell_Rate=float(Sell_Rate_var.get())
       
        
                
        
        ##FORMULA

        Warp_Wire_Wgt_per_Sqmtr = ((Warp_Dia*Warp_Dia*0.493*Warp_Mesh)/2)

        Weft_Wire_Wgt_per_Sqmtr  =((Weft_Dia*Weft_Dia*0.493*Weft_Mesh)/2)

        Formula_Wire_Wgt = Warp_Wire_Wgt_per_Sqmtr + Weft_Wire_Wgt_per_Sqmtr

        Actual_Wgt_per_SqMtr= (Actual_Wgt)/(Width_1*Length_1+Width_2*Length_2+Width_3*Length_3)

        Wgt_Diff_per_SqMtr = Formula_Wire_Wgt - Actual_Wgt_per_SqMtr

        Warp_Wire_Wgt =((Warp_Dia*Warp_Dia*0.493*Warp_Mesh)/2)*((Width_1*Length_1)+(Width_2*Length_2)+(Width_3*Length_3))

        Weft_Wire_Wgt =((Weft_Dia*Weft_Dia*0.493*Weft_Mesh)/2)*((Width_1*Length_1)+(Width_2*Length_2)+(Width_3*Length_3))

        Total_Wire_Wgt = Warp_Wire_Wgt + Weft_Wire_Wgt


        totalsqft = ((Width_1*Length_1)+(Width_2*Length_2)+(Width_3*Length_3))*10.764 

        Actual_Warp_Wire_Wgt_per_SqMtr = (((Warp_Wire_Wgt_per_Sqmtr)/(Formula_Wire_Wgt))*((Actual_Wgt_per_SqMtr)))/1.04
        
        Actual_Weft_Wire_Wgt_per_SqMtr = Actual_Wgt_per_SqMtr - Actual_Warp_Wire_Wgt_per_SqMtr

        Actual_Warp_Dia = sqrt((Actual_Warp_Wire_Wgt_per_SqMtr*2)/ (0.493*Warp_Mesh))

        Actual_Weft_Dia = sqrt((Actual_Weft_Wire_Wgt_per_SqMtr*2)/ (0.493*Weft_Mesh))

        Warp_Wire_Cost =  Warp_Wire_Price * (Actual_Warp_Wire_Wgt_per_SqMtr/10.764)+(Scrap*Weft_Wire_Price)/(totalsqft*2)
        
        Weft_Wire_Cost =  Weft_Wire_Price * (Actual_Weft_Wire_Wgt_per_SqMtr/10.764)+(Scrap*Weft_Wire_Price)/(totalsqft*2)

        Wire_Cost_per_Sqft = Warp_Wire_Cost+Weft_Wire_Cost

        Scrap_Percentage = (Scrap*100)/ (Actual_Wgt+Scrap)

        RM_Value = (Actual_Wgt+Scrap)*(Weft_Wire_Price)

        FG_Value = Sell_Rate*totalsqft

        FG_Diff_Value = FG_Value - RM_Value

        FG_Percentage = (FG_Diff_Value / RM_Value)*100

        Actual_Wgt_per_400_sqft =  (Actual_Wgt/totalsqft)*400

        Avg_Actual_Dia =  sqrt((Actual_Wgt_per_SqMtr)/ (0.493*Warp_Mesh))

        connection = pymysql.connect(host="localhost", user="root", password="0000")
        cursor = connection.cursor()
        a=cursor.execute("SHOW DATABASES LIKE 'Jalaram'")

        cursor.execute("use Jalaram;")
        insertYellow="INSERT INTO Yellow VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(Program_No,
        Machine_No,Date,Warp_Mesh,Weft_Mesh,Warp_Dia,Weft_Dia,Warp_Grade,Weft_Grade,Actual_Wgt,Warp_Wire_Price,Weft_Wire_Price,Scrap,Formula_Wire_Wgt,Actual_Wgt_per_SqMtr,
        Wgt_Diff_per_SqMtr,Avg_Actual_Dia,Actual_Warp_Dia,Actual_Weft_Dia,Wire_Cost_per_Sqft,Scrap_Percentage,Sell_Rate,totalsqft,RM_Value,FG_Value,FG_Diff_Value,FG_Percentage,Actual_Wgt_per_400_sqft,
        Warp_Wire_Cost,Weft_Wire_Cost,Width_1,Width_2,Width_3, Length_1,Length_2,Length_3)
        cursor.execute(insertYellow)
        connection.commit()                                                                                                                                                                                                    
        
    tk.Button(root,text = 'Save',fg='black',bg='#32DE84' ,borderwidth = 5,takefocus=0,command = Save).place(x=515, y=230)









    def Showall():


        r = tk.Tk()
        r.state("zoomed")
        r.geometry("1920x800")
        r.title("Jalaram Data")

        connect = mysql.connector.connect(host="localhost",user="root", passwd="0000",
          database="Jalaram")

        conn = connect.cursor()
        conn.execute("SELECT * FROM Yellow ;")
        

        tree=ttk.Treeview(r,height=30)
        tree['show'] = 'headings'

        s = ttk.Style(r)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica',11))
        s.configure("Treeview.Heading", foreground='red',font=('Helvetica', 8,"bold"))

        # Define number of columns
        tree["columns"]=("Program_No","Machine_No","Date","Warp_Mesh","Weft_Mesh","Warp_Dia","Weft_Dia","Warp_Grade"
                         ,"Weft_Grade","Actual_Wgt","Warp_Wire_Price"
                         ,"Weft_Wire_Price","Scrap","Formula_Wire_Wgt","Actual_Wgt_per_SqMtr"
                         ,"Wgt_Diff_per_SqMtr","Avg_Actual_Dia","Actual_Warp_Dia","Actual_Weft_Dia","Wire_Cost_per_Sqft","Scrap_Percentage"
                         ,"Sell_Rate","totalsqft","RM_Value","FG_Value","FG_Diff_Value","FG_Percentage","Actual_Wgt_per_400_sqft"
                         ,"Warp_Wire_Cost","Weft_Wire_Cost"
                         ,"Width_1","Width_2","Width_3", "Length_1","Length_2","Length_3")

        #Assign the width,minwidth and anchor to the respective columns
        
        tree.column("Program_No", width=55, minwidth=55,anchor=tk.CENTER)
        tree.column("Machine_No", width=55, minwidth=55,anchor=tk.CENTER)
        tree.column("Date", width=100, minwidth=100,anchor=tk.CENTER)    
        tree.column("Warp_Mesh", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Mesh", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Grade", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Grade", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Wire_Price", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Price", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Scrap", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Formula_Wire_Wgt", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt_per_SqMtr", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Wgt_Diff_per_SqMtr", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Avg_Actual_Dia", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Actual_Warp_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Weft_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Wire_Cost_per_Sqft", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Scrap_Percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Sell_Rate", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("totalsqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Diff_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt_per_400_sqft",width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Warp_Wire_Cost", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Cost", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_3", width=75, minwidth=75,anchor=tk.CENTER)

                        


        #Assign the heading names to the respective columns
        
        tree.heading("Program_No", text="Prog No",anchor=tk.CENTER)
        tree.heading("Machine_No", text="Mach No",anchor=tk.CENTER)
        tree.heading("Date", text="Date",anchor=tk.CENTER)
        tree.heading("Warp_Mesh", text="Warp Mesh",anchor=tk.CENTER)
        tree.heading("Weft_Mesh", text="Weft Mesh",anchor=tk.CENTER)
        tree.heading("Warp_Dia", text="Warp Dia",anchor=tk.CENTER)
        tree.heading("Weft_Dia", text="Weft Dia",anchor=tk.CENTER)
        tree.heading("Warp_Grade", text="Warp Grade",anchor=tk.CENTER)
        tree.heading("Weft_Grade", text="Weft Grade",anchor=tk.CENTER)
        tree.heading("Actual_Wgt", text="Actual Wgt",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Price", text="Weft Price",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Price", text="Warp Price",anchor=tk.CENTER)
        tree.heading("Scrap", text="Scrap (Kg)",anchor=tk.CENTER)
        tree.heading("Formula_Wire_Wgt", text="Formula Wgt",anchor=tk.CENTER)
        tree.heading("Actual_Wgt_per_SqMtr", text="Actual Wgt per SqMtr",anchor=tk.CENTER)
        tree.heading("Wgt_Diff_per_SqMtr",text="Wgt Diff per SqMtr",anchor=tk.CENTER)
        tree.heading("Avg_Actual_Dia",text="Avg Actual Dia",anchor=tk.CENTER)
        tree.heading("Actual_Warp_Dia", text="Actual Warp Dia",anchor=tk.CENTER)
        tree.heading("Actual_Weft_Dia", text="Actual Weft Dia",anchor=tk.CENTER)
        tree.heading("Wire_Cost_per_Sqft", text="Wire Cost per Sqft",anchor=tk.CENTER)
        tree.heading("Scrap_Percentage", text="Scrap %",anchor=tk.CENTER)
        tree.heading("Sell_Rate", text="Sell Rate",anchor=tk.CENTER)
        tree.heading("totalsqft", text="Total Sqft",anchor=tk.CENTER)
        tree.heading("RM_Value", text="RM Value",anchor=tk.CENTER)
        tree.heading("FG_Value", text="FG_Value",anchor=tk.CENTER)
        tree.heading("FG_Diff_Value", text="FG Diff Value",anchor=tk.CENTER)
        tree.heading("FG_Percentage", text="FG %",anchor=tk.CENTER)
        tree.heading("Actual_Wgt_per_400_sqft", text="Actual Wgt (400sqft)",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Cost", text="Warp Cost",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Cost", text="Weft Cost",anchor=tk.CENTER)
        tree.heading("Width_1", text="Width 1",anchor=tk.CENTER)
        tree.heading("Width_2", text="Width 2",anchor=tk.CENTER)
        tree.heading("Width_3", text="Width 3",anchor=tk.CENTER)
        tree.heading("Length_1", text="Length 1",anchor=tk.CENTER)
        tree.heading("Length_2", text="Length 2",anchor=tk.CENTER)
        tree.heading("Length_3", text="Length 3",anchor=tk.CENTER)
        



        i = 0
        for ro in conn:
            if ro[0]%2==0:
                
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34]),tags=("odd",))
            i = i + 1
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="white",background="black")

        hsb = ttk.Scrollbar(r,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(r,orient="vertical",)
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)

        tree.pack()

        def delete_data(tree):
            selected_item=tree.selection()[0]
            
            uid=tree.item(selected_item)['values'][0]
            del_query="DELETE FROM Yellow WHERE Program_No=%s"
            sel_data=(uid,)
            conn.execute(del_query,sel_data)
            connect.commit()
            tree.delete(selected_item)
            

        deletebutton = tk.Button(r,text="delete",command=lambda:delete_data(tree))
        deletebutton.configure(font =('calibri', 14, 'bold'), bg = 'red',fg='white')
        deletebutton.place(x=300,y=670)        
        r.bind("<Escape>", lambda x: r.destroy())  
        r.mainloop()

    tk.Button(root,text = 'Show_All',fg='black',bg='#0088FC' ,borderwidth = 5,takefocus=0,command = Showall).place(x=600, y=230)

    ####

    def sort():


        r = tk.Tk()
        r.state("zoomed")
        r.geometry("1920x800")
        r.title("SORTING DATA")

        connect = mysql.connector.connect(host="localhost",user="root", passwd="0000",
          database="Jalaram")

        conn = connect.cursor()

        while True:
            if clicked3.get() == "Option 2" and clicked4.get()=="" :
                    conn.execute("SELECT * FROM yellow WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get()) +'"' + ";" )
                    break
            if clicked5.get() == "Option 3" and clicked6.get()=="" :
                    conn.execute("SELECT * FROM yellow WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+";")                                                                               
                    break
            if clicked7.get() == "Option 4" and clicked8.get()=="" :
                    conn.execute("SELECT * FROM yellow WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+";")
                    break
            if clicked9.get() == "Option 5" and clicked10.get()=="" :                                                                                                                                                                                                                                                                             
                    conn.execute("SELECT * FROM yellow WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+" AND "+clicked7.get() + "=" + '"' + str(clicked8.get()) + '"'+";")
                    break
            else:
                    conn.execute("SELECT * FROM yellow WHERE " + clicked1.get() + "=" + '"' + str(clicked2.get())+'"' +" AND "+ clicked3.get() + "=" + '"' + str(clicked4.get()) + '"'+ " AND " +clicked5.get() + "=" + '"' + str(clicked6.get()) + '"'+" AND "+clicked7.get() + "=" + '"' + str(clicked8.get()) + '"'+ " AND "+clicked9.get() + "=" + '"' + str(clicked10.get()) + '"'+" AND "+clicked11.get() + "=" + '"' + str(clicked12.get()) + '"'+" AND "+clicked13.get() + "=" + '"' + str(clicked14.get()) + '"'+" AND "+clicked15.get() + "=" + '"' + str(clicked16.get()) + '"'+";")

        tree=ttk.Treeview(r,height=30)
        tree['show'] = 'headings'

        s = ttk.Style(r)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica',11))
        s.configure("Treeview.Heading", foreground='red',font=('Helvetica', 8,"bold"))

        # Define number of columns
        tree["columns"]=("Program_No","Machine_No","Date","Warp_Mesh","Weft_Mesh","Warp_Dia","Weft_Dia","Warp_Grade"
                         ,"Weft_Grade","Actual_Wgt","Warp_Wire_Price"
                         ,"Weft_Wire_Price","Scrap","Formula_Wire_Wgt","Actual_Wgt_per_SqMtr"
                         ,"Wgt_Diff_per_SqMtr","Actual_Warp_Dia","Actual_Weft_Dia","Wire_Cost_per_Sqft","Scrap_Percentage"
                         ,"Sell_Rate","totalsqft","RM_Value","FG_Value","FG_Diff_Value","FG_Percentage","Actual_Wgt_per_400_sqft"
                         ,"Warp_Wire_Cost","Weft_Wire_Cost"
                         ,"Width_1","Width_2","Width_3", "Length_1","Length_2","Length_3")

        #Assign the width,minwidth and anchor to the respective columns
        
        tree.column("Program_No", width=55, minwidth=55,anchor=tk.CENTER)
        tree.column("Machine_No", width=55, minwidth=55,anchor=tk.CENTER)
        tree.column("Date", width=100, minwidth=100,anchor=tk.CENTER)    
        tree.column("Warp_Mesh", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Mesh", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Grade", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Grade", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Wire_Price", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Price", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Scrap", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Formula_Wire_Wgt", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt_per_SqMtr", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Wgt_Diff_per_SqMtr", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Actual_Warp_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Weft_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Wire_Cost_per_Sqft", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Scrap_Percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Sell_Rate", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("totalsqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Diff_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt_per_400_sqft",width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Warp_Wire_Cost", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Cost", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_3", width=75, minwidth=75,anchor=tk.CENTER)

                        


        #Assign the heading names to the respective columns
        
        tree.heading("Program_No", text="Prog No",anchor=tk.CENTER)
        tree.heading("Machine_No", text="Mach No",anchor=tk.CENTER)
        tree.heading("Date", text="Date",anchor=tk.CENTER)
        tree.heading("Warp_Mesh", text="Warp Mesh",anchor=tk.CENTER)
        tree.heading("Weft_Mesh", text="Weft Mesh",anchor=tk.CENTER)
        tree.heading("Warp_Dia", text="Warp Dia",anchor=tk.CENTER)
        tree.heading("Weft_Dia", text="Weft Dia",anchor=tk.CENTER)
        tree.heading("Warp_Grade", text="Warp Grade",anchor=tk.CENTER)
        tree.heading("Weft_Grade", text="Weft Grade",anchor=tk.CENTER)
        tree.heading("Actual_Wgt", text="Actual Wgt",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Price", text="Weft Price",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Price", text="Warp Price",anchor=tk.CENTER)
        tree.heading("Scrap", text="Scrap (Kg)",anchor=tk.CENTER)
        tree.heading("Formula_Wire_Wgt", text="Formula Wgt",anchor=tk.CENTER)
        tree.heading("Actual_Wgt_per_SqMtr", text="Actual Wgt per SqMtr",anchor=tk.CENTER)
        tree.heading("Wgt_Diff_per_SqMtr",text="Wgt Diff per SqMtr",anchor=tk.CENTER)
        tree.heading("Actual_Warp_Dia", text="Actual Warp Dia",anchor=tk.CENTER)
        tree.heading("Actual_Weft_Dia", text="Actual Weft Dia",anchor=tk.CENTER)
        tree.heading("Wire_Cost_per_Sqft", text="Wire Cost per Sqft",anchor=tk.CENTER)
        tree.heading("Scrap_Percentage", text="Scrap %",anchor=tk.CENTER)
        tree.heading("Sell_Rate", text="Sell Rate",anchor=tk.CENTER)
        tree.heading("totalsqft", text="Total Sqft",anchor=tk.CENTER)
        tree.heading("RM_Value", text="RM Value",anchor=tk.CENTER)
        tree.heading("FG_Value", text="FG_Value",anchor=tk.CENTER)
        tree.heading("FG_Diff_Value", text="FG Diff Value",anchor=tk.CENTER)
        tree.heading("FG_Percentage", text="FG %",anchor=tk.CENTER)
        tree.heading("Actual_Wgt_per_400_sqft", text="Actual Wgt (400sqft)",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Cost", text="Warp Cost",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Cost", text="Weft Cost",anchor=tk.CENTER)
        tree.heading("Width_1", text="Width 1",anchor=tk.CENTER)
        tree.heading("Width_2", text="Width 2",anchor=tk.CENTER)
        tree.heading("Width_3", text="Width 3",anchor=tk.CENTER)
        tree.heading("Length_1", text="Length 1",anchor=tk.CENTER)
        tree.heading("Length_2", text="Length 2",anchor=tk.CENTER)
        tree.heading("Length_3", text="Length 3",anchor=tk.CENTER)
        



        i = 0
        for ro in conn:
            if ro[0]%2==0:
                
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34]),tags=("odd",))
            i = i + 1
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="white",background="black")

        hsb = ttk.Scrollbar(r,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(r,orient="vertical",)
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)

        tree.pack()

        def delete_data(tree):
            selected_item=tree.selection()[0]
            
            uid=tree.item(selected_item)['values'][0]
            del_query="DELETE FROM Jalaram WHERE Sr_No=%s"
            sel_data=(uid,)
            conn.execute(del_query,sel_data)
            connect.commit()
            tree.delete(selected_item)
            mb.showinfo("Success","Entry Deleted")

        deletebutton = tk.Button(r,text="delete",command=lambda:delete_data(tree))
        deletebutton.configure(font =('calibri', 14, 'bold'), bg = 'red',fg='white')
        deletebutton.place(x=300,y=670)        
        r.bind("<Escape>", lambda x: r.destroy())  
        r.mainloop()

    options = [
                "Program_No",
                "Machine_No",
                "Date",
                "Warp_Mesh",
                "Weft_Mesh",
                "Warp_Diameter",
                "Weft_Diameter",
                "Warp_Grade",
                "Weft_Grade",
                "Wgt_Diff_per_SqMtr",

              
            ]


    clicked0 = StringVar()
    clicked0.set("Order by")
    OptionMenu( root , clicked0 , *options ).place(x=1285, y = 300)



    def order():


        r = tk.Tk()
        r.state("zoomed")
        r.geometry("1920x800")
        r.title("ORDERING DATA")

        connect = mysql.connector.connect(host="localhost",user="root", passwd="0000",
          database="Jalaram")

        conn = connect.cursor()

        
        
        conn.execute("SELECT * FROM Yellow ORDER BY " + clicked0.get() + ";")

        tree=ttk.Treeview(r,height=30)
        tree['show'] = 'headings'

        s = ttk.Style(r)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica',11))
        s.configure("Treeview.Heading", foreground='red',font=('Helvetica', 8,"bold"))

        # Define number of columns
        tree["columns"]=("Program_No","Machine_No","Date","Warp_Mesh","Weft_Mesh","Warp_Dia","Weft_Dia","Warp_Grade"
                         ,"Weft_Grade","Actual_Wgt","Warp_Wire_Price"
                         ,"Weft_Wire_Price","Scrap","Formula_Wire_Wgt","Actual_Wgt_per_SqMtr"
                         ,"Wgt_Diff_per_SqMtr","Actual_Warp_Dia","Actual_Weft_Dia","Wire_Cost_per_Sqft","Scrap_Percentage"
                         ,"Sell_Rate","totalsqft","RM_Value","FG_Value","FG_Diff_Value","FG_Percentage","Actual_Wgt_per_400_sqft"
                         ,"Warp_Wire_Cost","Weft_Wire_Cost"
                         ,"Width_1","Width_2","Width_3", "Length_1","Length_2","Length_3")

        #Assign the width,minwidth and anchor to the respective columns
        
        tree.column("Program_No", width=55, minwidth=55,anchor=tk.CENTER)
        tree.column("Machine_No", width=55, minwidth=55,anchor=tk.CENTER)
        tree.column("Date", width=100, minwidth=100,anchor=tk.CENTER)    
        tree.column("Warp_Mesh", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Mesh", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Grade", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Grade", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Warp_Wire_Price", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Price", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Scrap", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Formula_Wire_Wgt", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt_per_SqMtr", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Wgt_Diff_per_SqMtr", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Actual_Warp_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Weft_Dia", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Wire_Cost_per_Sqft", width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Scrap_Percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Sell_Rate", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("totalsqft", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("RM_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Diff_Value", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("FG_Percentage", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Actual_Wgt_per_400_sqft",width=75, minwidth=120,anchor=tk.CENTER)
        tree.column("Warp_Wire_Cost", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Weft_Wire_Cost", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Width_3", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_1", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_2", width=75, minwidth=75,anchor=tk.CENTER)
        tree.column("Length_3", width=75, minwidth=75,anchor=tk.CENTER)

                        


        #Assign the heading names to the respective columns
        
        tree.heading("Program_No", text="Prog No",anchor=tk.CENTER)
        tree.heading("Machine_No", text="Mach No",anchor=tk.CENTER)
        tree.heading("Date", text="Date",anchor=tk.CENTER)
        tree.heading("Warp_Mesh", text="Warp Mesh",anchor=tk.CENTER)
        tree.heading("Weft_Mesh", text="Weft Mesh",anchor=tk.CENTER)
        tree.heading("Warp_Dia", text="Warp Dia",anchor=tk.CENTER)
        tree.heading("Weft_Dia", text="Weft Dia",anchor=tk.CENTER)
        tree.heading("Warp_Grade", text="Warp Grade",anchor=tk.CENTER)
        tree.heading("Weft_Grade", text="Weft Grade",anchor=tk.CENTER)
        tree.heading("Actual_Wgt", text="Actual Wgt",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Price", text="Weft Price",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Price", text="Warp Price",anchor=tk.CENTER)
        tree.heading("Scrap", text="Scrap (Kg)",anchor=tk.CENTER)
        tree.heading("Formula_Wire_Wgt", text="Formula Wgt",anchor=tk.CENTER)
        tree.heading("Actual_Wgt_per_SqMtr", text="Actual Wgt per SqMtr",anchor=tk.CENTER)
        tree.heading("Wgt_Diff_per_SqMtr",text="Wgt Diff per SqMtr",anchor=tk.CENTER)
        tree.heading("Actual_Warp_Dia", text="Actual Warp Dia",anchor=tk.CENTER)
        tree.heading("Actual_Weft_Dia", text="Actual Weft Dia",anchor=tk.CENTER)
        tree.heading("Wire_Cost_per_Sqft", text="Wire Cost per Sqft",anchor=tk.CENTER)
        tree.heading("Scrap_Percentage", text="Scrap %",anchor=tk.CENTER)
        tree.heading("Sell_Rate", text="Sell Rate",anchor=tk.CENTER)
        tree.heading("totalsqft", text="Total Sqft",anchor=tk.CENTER)
        tree.heading("RM_Value", text="RM Value",anchor=tk.CENTER)
        tree.heading("FG_Value", text="FG_Value",anchor=tk.CENTER)
        tree.heading("FG_Diff_Value", text="FG Diff Value",anchor=tk.CENTER)
        tree.heading("FG_Percentage", text="FG %",anchor=tk.CENTER)
        tree.heading("Actual_Wgt_per_400_sqft", text="Actual Wgt (400sqft)",anchor=tk.CENTER)
        tree.heading("Warp_Wire_Cost", text="Warp Cost",anchor=tk.CENTER)
        tree.heading("Weft_Wire_Cost", text="Weft Cost",anchor=tk.CENTER)
        tree.heading("Width_1", text="Width 1",anchor=tk.CENTER)
        tree.heading("Width_2", text="Width 2",anchor=tk.CENTER)
        tree.heading("Width_3", text="Width 3",anchor=tk.CENTER)
        tree.heading("Length_1", text="Length 1",anchor=tk.CENTER)
        tree.heading("Length_2", text="Length 2",anchor=tk.CENTER)
        tree.heading("Length_3", text="Length 3",anchor=tk.CENTER)
        



        i = 0
        for ro in conn:
            if ro[0]%2==0:
                
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18],ro[19],ro[20],ro[21],ro[22],ro[23],ro[24],ro[25],ro[26],ro[27],ro[28],ro[29],ro[30],ro[31],ro[32],ro[33],ro[34]),tags=("odd",))
            i = i + 1
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="white",background="black")

        hsb = ttk.Scrollbar(r,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(r,orient="vertical",)
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)

        tree.pack()

        def delete_data(tree):
            selected_item=tree.selection()[0]
            
            uid=tree.item(selected_item)['values'][0]
            del_query="DELETE FROM Jalaram WHERE Sr_No=%s"
            sel_data=(uid,)
            conn.execute(del_query,sel_data)
            connect.commit()
            tree.delete(selected_item)
            mb.showinfo("Success","Entry Deleted")

        deletebutton = tk.Button(r,text="delete",command=lambda:delete_data(tree))
        deletebutton.configure(font =('calibri', 14, 'bold'), bg = 'red',fg='white')
        deletebutton.place(x=300,y=670)        
        r.bind("<Escape>", lambda x: r.destroy())  
        r.mainloop()


           
        
    tk.Button(root,text = 'Order Data',fg='black',bg='#0088FC' ,borderwidth = 5,takefocus=0,command = order).place(x=1295, y=350)

        
        
                    
    tk.Button(root,text = 'Sort Data',fg='black',bg='#0088FC' ,borderwidth = 5,takefocus=0,command = sort).place(x=700, y=700)


    def enter_button(event):
        calculate()

    root.bind('<Return>', enter_button)


    root.bind('<Control-o>', close)



    
    root.mainloop()

Button(j,text = 'Yellow Card',fg='black',bg='#32DE84' ,font=("Kokila",20),borderwidth = 10,takefocus=0,command = Yellow_Card).place(x=1000, y=500)
j.mainloop()


