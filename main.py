from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime
import random
import os

root = Tk()
root.title("Pizza Management System")
root.geometry("1350x750+0+0")
root.config(bg="black")


#***********************FRAMES****************************
tf = Frame(root,width="1350",height="100",border=14,relief=RAISED)
tf.pack(side=TOP)

lf = Frame(root,width="900",height="650",border=8,relief=RAISED)
lf.pack(side=LEFT)

rf = Frame(root,width="450",height="650",border=8,relief=RAISED)
rf.pack(side=RIGHT)

tlf = Frame(lf,width="900",height="330",border=8,relief=RAISED)
tlf.pack(side=TOP)

blf = Frame(lf,width="900",height="320",border=6,relief=RAISED)
blf.pack(side=BOTTOM)

trf = Frame(rf,width="450",height="450",border=12,relief=RAISED)
trf.pack(side=TOP)

brf = Frame(rf,width="450",height="200",border=16,relief=RAISED)
brf.pack(side=BOTTOM)

ltlf = Frame(tlf,width="400",height="330",border=16,relief=RAISED)
ltlf.pack(side=LEFT)

rtlf = Frame(tlf,width="400",height="330",border=16,relief=RAISED)
rtlf.pack(side=RIGHT)

lblf = Frame(blf,width="450",height="330",bd=14,relief=RAISED)
lblf.pack(side=LEFT)

rblf = Frame(blf,width="450",height="330",bd=14,relief=RAISED)
rblf.pack(side=RIGHT)


tf.config(bg="black")
lf.config(bg="black")
rf.config(bg="black")


#*****************FUNCTONS**************************
def Quit():
	Quit=messagebox.askyesno("Quit System","Do you want to quit?")
	if Quit>0:
		root.destroy()
		return
	
def Reset():
	eBbq.set("0")
	eTikka.set("0")
	ePork.set("0")
	eBeef.set("0")
	eMeat.set("0")
	eRabbit.set("0")
	eMargarita.set("0")		
	eBreadBeef.set("0")
	eBreadKuku.set("0")
	eAvo.set("0")
	eMango.set("0")
	eCocktail.set("0")
	ePassion.set("0")
	eSoda.set("0")
	eWater.set("0")
	eIcecream.set("0")
	eVanilla.set("0")
	
	eCostpizza.set("")
	eCostdrinks.set("")
	eVat.set("")
	eTotal.set("")
	eAmmount.set("")
	eBalance.set("")
	
	receipt.delete("1.0",END)
	
	var1.set("0")
	var2.set("0")
	var3.set("0")
	var4.set("0")
	var5.set("0")
	var6.set("0")
	var7.set("0")
	var8.set("0")
	var9.set("0")
	
	var10.set("0")
	var11.set("0")
	var12.set("0")
	var13.set("0")
	var14.set("0")
	var15.set("0")
	var16.set("0")
	var17.set("0")
	
	entryBbq.config(state=DISABLED)
	entryTikka.config(state=DISABLED)
	entryPork.config(state=DISABLED)
	entryBeef.config(state=DISABLED)
	entryMeat.config(state=DISABLED)
	entryRabbit.config(state=DISABLED)
	entryMargarita.config(state=DISABLED)
	entryBreadBeef.config(state=DISABLED)
	entryBreadKuku.config(state=DISABLED)
	
	entryAvo.config(state=DISABLED)
	entryMango.config(state=DISABLED)
	entryCocktail.config(state=DISABLED)
	entryPassion.config(state=DISABLED)
	entrySoda.config(state=DISABLED)
	entryWater.config(state=DISABLED)
	entryIcecream.config(state=DISABLED)
	entryVanilla.config(state=DISABLED)
	



#***********************CHECKBUTTON VALUE****************************	
def CheckBtn():
	if (var1.get()==1):
		entryBbq.config(state=NORMAL)
	elif (var1.get()==0):
		entryBbq.config(state=DISABLED)
		eBbq.set("0")
	if (var2.get()==1):
		entryTikka.config(state=NORMAL)
	elif (var2.get()==0):
		entryTikka.config(state=DISABLED)
		eTikka.set("0")
	if (var3.get()==1):
		entryPork.config(state=NORMAL)
	elif (var3.get()==0):
		entryPork.config(state=DISABLED)
		ePork.set("0")	
	if (var4.get()==1):
		entryBeef.config(state=NORMAL)
	elif (var4.get()==0):
		entryBeef.config(state=DISABLED)
		eBeef.set("0")	
	if (var5.get()==1):
		entryMeat.config(state=NORMAL)
	elif (var5.get()==0):
		entryMeat.config(state=DISABLED)
		eMeat.set("0")	
	if (var6.get()==1):
		entryRabbit.config(state=NORMAL)
	elif (var6.get()==0):
		entryRabbit.config(state=DISABLED)
		eRabbit.set("0")	
	if (var7.get()==1):
		entryMargarita.config(state=NORMAL)
	elif (var7.get()==0):
		entryMargarita.config(state=DISABLED)
		eMargarita.set("0")
	if (var8.get()==1):
		entryBreadKuku.config(state=NORMAL)
	elif (var8.get()==0):
		entryBreadKuku.config(state=DISABLED)
		eBreadKuku.set("0")
	if (var9.get()==1):
		entryBreadBeef.config(state=NORMAL)
	elif (var9.get()==0):
		entryBreadBeef.config(state=DISABLED)
		eBreadBeef.set("0")
		
	if (var10.get()==1):
		entryAvo.config(state=NORMAL)
	elif (var10.get()==0):
		entryAvo.config(state=DISABLED)
		eAvo.set("0")
	if (var11.get()==1):
		entryMango.config(state=NORMAL)
	elif (var11.get()==0):
		entryMango.config(state=DISABLED)
		eMango.set("0")	
	if (var12.get()==1):
		entryCocktail.config(state=NORMAL)
	elif (var12.get()==0):
		entryCocktail.config(state=DISABLED)
		eCocktail.set("0")
	if (var13.get()==1):
		entryPassion.config(state=NORMAL)
	elif (var13.get()==0):
		entryPassion.config(state=DISABLED)
		ePassion.set("0")
	if (var14.get()==1):
		entrySoda.config(state=NORMAL)
	elif (var14.get()==0):
		entrySoda.config(state=DISABLED)
		eSoda.set("0")
	if (var15.get()==1):
		entryWater.config(state=NORMAL)
	elif (var15.get()==0):
		entryWater.config(state=DISABLED)
		eWater.set("0")
	if (var16.get()==1):
		entryIcecream.config(state=NORMAL)
	elif (var16.get()==0):
		entryIcecream.config(state=DISABLED)
		eIcecream.set("0")
	if (var17.get()==1):
		entryVanilla.config(state=NORMAL)
	elif (var17.get()==0):
		entryVanilla.config(state=DISABLED)
		eVanilla.set("0")	


def Cost():
	item1 = int(entryBbq.get())		
	item2= int(entryTikka.get())	
	item3 = int(entryPork.get())
	item4 = int(entryBeef.get())
	item5 = int(entryMeat.get())
	item6 = int(entryRabbit.get())
	item7 = int(entryMargarita.get())
	item8 = int(entryBreadKuku.get())
	item9 = int(entryBreadBeef.get())
	
	item10 = int(entryAvo.get())
	item11 = int(entryMango.get())
	item12 = int(entryCocktail.get())
	item13 = int(entryPassion.get())
	item14 = int(entrySoda.get())
	item15 = int(entryWater.get())
	item16 = int(entryIcecream.get())
	item17 = int(entryVanilla.get())
	

	pizzaPrice=int((item1*150)+(item2*150)+(item3*150)+(item4*150)+(item5*200)+(item6*200)+(item7*50)+(item8*100)+(item9*100))
	eCostpizza.set(pizzaPrice)
	
	drinksPrice=int((item10*30)+(item11*30)+(item12*40)+(item13*30)+(item14*30)+(item15*30)+(item16*50)+(item17*50))
	eCostdrinks.set(drinksPrice)
	
	vat=(pizzaPrice+drinksPrice)*0.08
	VAT="{0:.2f}".format(vat)
	eVat.set(VAT)
	
	total=pizzaPrice+drinksPrice+vat
	eTotal.set(total)
	os.path.join("C:\\User\\Gee\\boy\\{}".format(total))

	try:
		itemPaid=int(entryAmmount.get())
	except Exception as Error:
		pass
		
	try:
		balance=int(itemPaid-total)
		eBalance.set(balance)
	except Exception as Error:
		pass


def Receipt():
	item1 = int(entryBbq.get())
	item2= int(entryTikka.get())	
	item3 = int(entryPork.get())
	item4 = int(entryBeef.get())
	item5 = int(entryMeat.get())
	item6 = int(entryRabbit.get())
	item7 = int(entryMargarita.get())
	item8 = int(entryBreadKuku.get())
	item9 = int(entryBreadBeef.get())
	
	item10 = int(entryAvo.get())
	item11 = int(entryMango.get())
	item12 = int(entryCocktail.get())
	item13 = int(entryPassion.get())
	item14 = int(entrySoda.get())
	item15 = int(entryWater.get())
	item16 = int(entryIcecream.get())
	item17 = int(entryVanilla.get())
	
	item18 = int(eCostpizza.get())
	item19 = int(eCostdrinks.get())
	
	receipt.delete("1.0",END)
	receipt.insert(END,"Receipt Ref: {}\t \t  {}\n\n".format(receiptRef.get(),dateOfOrder.get()))
	receipt.insert(END,"Items \t\t\tQuantity \t\tCost\n\n")
	
	if item1 >= 1:
		pKuku = item1*150
		receipt.insert(END,"Kuku BBQ Pizza \t\t\t{} x 150 \t\t{}\n".format(item1,pKuku))
	if item2 >= 1:
		pTikka = item2*150
		receipt.insert(END,"Kuku Tikka Pizza \t\t\t{} x 150 \t\t{} \n".format(item2, pTikka))
	if item3 >= 1:
		pPork = item3*150	
		receipt.insert(END,"Pork BBQ Pizza \t\t\t{} x 150 \t\t{} \n".format(item3,pPork))
	if item4 >= 1:
		pBeef = item4*150	
		receipt.insert(END,"Beef BBQ Pizza \t\t\t{} x 150 \t\t{} \n".format(item4,pBeef))
	if item5 >= 1:
		pMeat = item5*200	
		receipt.insert(END,"Meatlovers Pizza \t\t\t{} x 200 \t\t{} \n".format(item5,pMeat))
	if item6 >= 1:
		pRabbit = item6*200	
		receipt.insert(END,"Rabbit Pizza \t\t\t{} x 200 \t\t{} \n".format(item6,pRabbit))
	if item7 >= 1:
		pMargarita = item7*50	
		receipt.insert(END,"Margarita \t\t\t{} x 50 \t\t{} \n".format(item7,pMargarita))
	if item8 >= 1:
		pBreadKuku = item8*100	
		receipt.insert(END,"Bread Kuku Pizza \t\t\t{} x 100 \t\t{} \n".format(item8,pBreadKuku))
	if item9 >= 1:
		pBreadBeef = item9*100	
		receipt.insert(END,"Bread Beef Pizza \t\t\t{} x 100 \t\t{} \n".format(item9,pBreadBeef))
	
	if item10 >= 1:
		pAvo = item10*30
		receipt.insert(END,"Avocado Juice \t\t\t{} x 30 \t\t{} \n".format(item10,pAvo))
	if item11 >= 1:
		pMango = item11*30	
		receipt.insert(END,"Mango \t\t\t{} x 30 \t\t{} \n".format(item11,pMango))
	if item12 >= 1:
		pCocktail = item12*40	
		receipt.insert(END,"Cocktail \t\t\t{} x 40 \t\t{} \n".format(item12,pCocktail))
	if item13 >= 1:
		pPassion = item13*30	
		receipt.insert(END,"Passion Juice \t\t\t{} x 30 \t\t{} \n".format(item13,pPassion))
	if item14 >= 1:
		pSoda = item14*30	
		receipt.insert(END,"Soda \t\t\t{} x 30 \t\t{} \n".format(item14,pSoda))
	if item15 >= 1:
		pWater = item15*30	
		receipt.insert(END,"Water \t\t\t{} x 30 \t\t{} \n".format(item15,pWater))
	if item16 >= 1:
		pIcecream = item16*50	
		receipt.insert(END,"Icecream \t\t\t{} x 50 \t\t{} \n".format(item16,pIcecream))
	if item17 >= 1:
		pVanilla = item17*50	
		receipt.insert(END,"Vanilla \t\t\t{} x 50 \t\t{} \n\n".format(item17,pVanilla))
	
	if item18 >= 1:
		receipt.insert(END,"Cost of Pizza KSHS. \t\t\t {} \n".format(item18))
	if item19 >= 1:	
		receipt.insert(END,"Cost of Drinks KSHS. \t\t\t {} \n".format(item19))
		
	receipt.insert(END,"VAT(8%) KSHS. \t\t\t {} \n".format(eVat.get()))
	receipt.insert(END,"Total KSHS. \t\t\t {} \n".format(eTotal.get()))
	receipt.insert(END,"Ammount Paid KSHS. \t\t\t {} \n".format(eAmmount.get()))
	receipt.insert(END,"Balance KSHS. \t\t\t {} \n\n".format(eBalance.get()))
	receipt.insert(END,"*************WE ARE GLAD TO HAVE YOU :) **********")
	
	
#*****************VARIABLES**************************
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()

var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()

eBbq=StringVar()
eTikka=StringVar()
ePork=StringVar()
eBeef=StringVar()
eMeat=StringVar()
eRabbit=StringVar()
eMargarita=StringVar()
eBreadBeef=StringVar()
eBreadKuku=StringVar()

eAvo=StringVar()
eMango=StringVar()
eCocktail=StringVar()
ePassion=StringVar()
eSoda=StringVar()
eWater=StringVar()
eIcecream=StringVar()
eVanilla=StringVar()
eCostpizza=StringVar()
eCostdrinks=StringVar()

eVat=StringVar()
eTotal=StringVar()
eAmmount=StringVar()
eBalance=StringVar()

dateOfOrder=StringVar()
dateOfOrder.set(datetime.today())

receiptRef=StringVar()
rcpt=random.randint(1000,9999)
receiptRef.set(rcpt)

eBbq.set("0")
eTikka.set("0")
ePork.set("0")
eBeef.set("0")
eMeat.set("0")
eRabbit.set("0")
eMargarita.set("0")
eBreadBeef.set("0")
eBreadKuku.set("0")

eAvo.set("0")
eMango.set("0")
eCocktail.set("0")
ePassion.set("0")
eSoda.set("0")
eWater.set("0")
eIcecream.set("0")
eVanilla.set("0")


#******************* LABELS******************************

Label(tf,text="    DOT PYZZA MANAGEMENT SYSTEM    ", font=("COURIER", 50, "bold"),bd=10, fg="cadet blue", bg="purple").grid(row=0,column=0)

Label(lblf,text="COST OF PIZZA \t\t", font=("COURIER", 18, "bold"), bd=8, anchor=W).grid(row=0,column=0,sticky=W)

Label(lblf,text="COST OF DRINKS", font=("COURIER", 18, "bold"), bd=8, anchor=W).grid(row=1,column=0,sticky=W)

Label(lblf,text="VAT (8%)\t", font=("COURIER", 18, "bold"), bd=8, anchor=W).grid(row=2,column=0,sticky=W)

Label(rblf,text="TOTAL\t\t", font=("COURIER", 18, "bold"), bd=8, anchor=W).grid(row=0,column=0,sticky=W)

Label(rblf,text="AMMOUNT PAID", font=("COURIER", 18, "bold"), bd=8, anchor=W).grid(row=1,column=0,sticky=W)

Label(rblf,text="BALANCE", font=("COURIER", 18, "bold"), bd=8, anchor=W).grid(row=2,column=0,sticky=W)

Label(trf,text="Receipt", font=("COURIER", 12, "bold"),bd=2,anchor="w").grid(row=0,column=0,sticky=W)


#*****************PIZZA CHECK BUTTONS**************************

checkBbq = Checkbutton(ltlf,text="Kuku Bbq", font=("COURIER", 16, "bold"),command=CheckBtn,variable=var1,onvalue=1,offvalue=0)
checkBbq.grid(row=0, sticky=W)

checkTikka = Checkbutton(ltlf,text="Kuku Tikka", font=("COURIER", 16, "bold"),command=CheckBtn,variable=var2,onvalue=1,offvalue=0)
checkTikka.grid(row=1, sticky=W)

checkPork = Checkbutton(ltlf,text="Pork Bbq", font=("COURIER", 16, "bold"),command=CheckBtn,variable=var3,onvalue=1,offvalue=0)
checkPork.grid(row=2, sticky=W)

checkBeef = Checkbutton(ltlf,text="Beef", font=("COURIER", 16, "bold"),command=CheckBtn,variable=var4,onvalue=1,offvalue=0)
checkBeef.grid(row=3, sticky=W)

checkMeat = Checkbutton(ltlf,text="Meatlovers",font=("COURIER", 16, "bold"),command=CheckBtn,variable=var5,onvalue=1,offvalue=0)
checkMeat.grid(row=4, sticky=W)

checkRabbit = Checkbutton(ltlf,text="Pizza Rabbit",font=("COURIER", 16, "bold"),command=CheckBtn,variable=var6,onvalue=1,offvalue=0)
checkRabbit.grid(row=5, sticky=W)

checkMargarita = Checkbutton(ltlf,text="Margarita",font=("COURIER", 16, "bold"),command=CheckBtn,variable=var7,onvalue=1,offvalue=0)
checkMargarita.grid(row=6, sticky=W)

checkBreadKuku = Checkbutton(ltlf,text="Kuku Bread Pizza",font=("COURIER", 16, "bold"),command=CheckBtn,variable=var8,onvalue=1,offvalue=0)
checkBreadKuku.grid(row=7, sticky=W)

checkBreadBeef = Checkbutton(ltlf,text="Beef Bread Pizza\t",font=("COURIER", 16, "bold"),command=CheckBtn,variable=var9,onvalue=1,offvalue=0)
checkBreadBeef.grid(row=8, sticky=W)


#*****************JUICE CHECK BUTTONS**************************

checkAvo = Checkbutton(rtlf,text="Blended Avocado\t",font=("COURIER", 18, "bold"),command=CheckBtn,variable=var10,onvalue=1,offvalue=0)
checkAvo.grid(row=0, sticky=W)

checkMango = Checkbutton(rtlf,text="Blended Mango\t",font=("COURIER", 18, "bold"),command=CheckBtn,variable=var11,onvalue=1,offvalue=0)
checkMango.grid(row=1, sticky=W)

checkCocktail = Checkbutton(rtlf,text="Blended Cocktail\t",font=("COURIER", 18, "bold"),command=CheckBtn,variable=var12,onvalue=1,offvalue=0)
checkCocktail.grid(row=2, sticky=W)

checkPassion = Checkbutton(rtlf,text="Passion Juice \t",font=("COURIER", 18, "bold"),variable=var13,onvalue=1,offvalue=0)
checkPassion.grid(row=3, sticky=W)

checkSoda = Checkbutton(rtlf,text="Soda\t",font=("COURIER", 18, "bold"),command=CheckBtn,variable=var14,onvalue=1,offvalue=0)
checkSoda.grid(row=4, sticky=W)

checkWater = Checkbutton(rtlf,text="Water\t",font=("COURIER", 18, "bold"),command=CheckBtn,variable=var15,onvalue=1,offvalue=0)
checkWater.grid(row=5, sticky=W)

checkIcecream = Checkbutton(rtlf,text="Ice Cream\t",font=("COURIER", 18, "bold"),command=CheckBtn,variable=var16,onvalue=1,offvalue=0)
checkIcecream.grid(row=6, sticky=W)

checkVanilla = Checkbutton(rtlf,text="Vanilla\t",font=("COURIER", 18, "bold"),command=CheckBtn,variable=var17,onvalue=1,offvalue=0)
checkVanilla.grid(row=7, sticky=W)


#*****************PIZZA ENTRY**************************

entryBbq = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eBbq)
entryBbq.grid(row=0,column=1)

entryTikka = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eTikka)
entryTikka.grid(row=1,column=1)

entryPork = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=ePork)
entryPork.grid(row=2,column=1)

entryBeef = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eBeef)
entryBeef.grid(row=3,column=1)

entryMeat = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eMeat)
entryMeat.grid(row=4,column=1)

entryRabbit = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eRabbit)
entryRabbit.grid(row=5,column=1)

entryMargarita = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eMargarita)
entryMargarita.grid(row=6,column=1)

entryBreadKuku = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eBreadKuku)
entryBreadKuku.grid(row=7,column=1)

entryBreadBeef = Entry(ltlf,width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eBreadBeef)
entryBreadBeef.grid(row=8,column=1)


#*****************JUICE ENTRY**************************

entryAvo = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eAvo)
entryAvo.grid(row=0,column=1)

entryMango = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eMango)
entryMango.grid(row=1,column=1)

entryCocktail = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eCocktail)
entryCocktail.grid(row=2,column=1)

entryPassion = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=ePassion)
entryPassion.grid(row=3,column=1)

entrySoda = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eSoda)
entrySoda.grid(row=4,column=1)

entryWater = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eWater)
entryWater.grid(row=5,column=1)

entryIcecream = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eIcecream)
entryIcecream.grid(row=6,column=1)

entryVanilla = Entry(rtlf, width=6,font=("ARIAL",12,"bold"),justify=LEFT, bd=8,state=DISABLED,textvariable=eVanilla)
entryVanilla.grid(row=7,column=1)


#*****************TOTAL ENTRY**************************

entryCostpizza = Entry(lblf,width=8,font=("ARIAL", 18),justify=LEFT, bd=8,state=NORMAL,textvariable=eCostpizza)
entryCostpizza.grid(row=0,column=1)

entrycostdrinks = Entry(lblf,width=8,font=("ARIAL", 18),justify=LEFT, bd=8,state=NORMAL,textvariable=eCostdrinks)
entrycostdrinks.grid(row=1,column=1)

entryVat = Entry(lblf,width=8,font=("ARIAL", 18),justify=LEFT, bd=8,state=NORMAL,textvariable=eVat)
entryVat.grid(row=2,column=1)

entryTotal = Entry(rblf,width=8,font=("ARIAL", 18),justify=LEFT, bd=8,state=NORMAL,textvariable=eTotal)
entryTotal.grid(row=0,column=1)

entryAmmount = Entry(rblf,width=8,font=("ARIAL", 18),justify=LEFT, bd=8,state=NORMAL,textvariable=eAmmount)
entryAmmount.grid(row=1,column=1)

entryBalance = Entry(rblf,width=8,font=("ARIAL", 18),justify=LEFT, bd=8,state=NORMAL,textvariable=eBalance)
entryBalance.grid(row=2,column=1)

#******************RECEIPT************************************

receipt = Text(trf,width="59",height="25",bg="white",bd=8,font=("ARIAL", 11, "bold"))
receipt.grid(row=1, column=0)


#***************BUTTONS**************************

btnTotal = Button(brf,text="TOTAL",bd=4,padx=16,pady=1,command=Cost)
btnTotal.grid(row=0,column=0)

btnReceipt = Button(brf,text="RECEIPT",fg="black",bd=4,padx=16,pady=1,command=Receipt)
btnReceipt.grid(row=0,column=1)

btnReset = Button(brf,text="RESET",fg="black",bd=4,padx=16,pady=1,command=Reset)
btnReset.grid(row=0,column=2)

btnExit = Button(brf,text="EXIT",fg="black",bd=4,padx=16,pady=1,command=Quit)
btnExit.grid(row=0,column=3)


root.mainloop()