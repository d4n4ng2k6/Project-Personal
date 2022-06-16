#import google
from turtle import width
from bs4 import BeautifulSoup
from googlesearch import search
from tkinter import ttk
import tkinter as tk

root = tk.Tk();
root.geometry('1000x1000')


root.title("Cloudbeds Data Enrichment Tools")
SearchFrame = tk.Frame(root)
SearchFrame.grid(column=0,row=0)
ResultFrame = tk.Frame(root)
ResultFrame.grid(column=0,row=1)
label = tk.Label(SearchFrame,text = "Properties Search Aggregator", font='Arial 15 bold')
label.grid(column=0, row=0,columnspan= 3, padx=20, pady=30)

# Start of GUI for property input
labelProp = tk.Label(SearchFrame,text = "Property Name :")
labelProp.grid (column=0, row=1, padx=10, pady=10, sticky=tk.W)
entProp = tk.Entry(SearchFrame,width=30)
entProp.grid(column=1, row=1, sticky=tk.W)
labelCity = tk.Label(SearchFrame,text = "City :")
labelCity.grid (column=0, row=2, padx=10, pady=10, sticky=tk.W)
entCity = tk.Entry(SearchFrame, width=30)
entCity.grid (column=1, row=2, sticky=tk.W)
labelAdr = tk.Label(SearchFrame,text = "Address :")
labelAdr.grid (column=0, row=3, padx=10, pady=10, sticky=tk.W)
entAdr = tk.Entry(SearchFrame,width=50)
entAdr.grid(column=1, row=3, sticky=tk.W)
BtnSearch = tk.Button(SearchFrame,text = "Search", width = 15)
BtnSearch.grid (column = 1, row=4)
#End of GUI property Input

#Start UI of Tabbed Pane
tabControl = ttk.Notebook(ResultFrame)
#Create tab frame
tabBooking = ttk.Frame(tabControl)
tabExpedia = ttk.Frame(tabControl)
#Adding Tab frame to tabControl and add tab title
tabControl.add(tabBooking, text='Booking.com')
tabControl.add(tabExpedia, text='Expedia')
#Arrange TabControl position
tabControl.grid(column =0, row=6, padx=10, pady=10)
#Add Component for Booking.com Tab
ttk.Label(tabBooking, text="More Information from Booking.com").grid(column=0,row=0,padx=10,pady=10)
ttk.Label(tabBooking, text="URL Link : ").grid(column=0,row=1,pady=20)
tk.Text(tabBooking, width=30,height=2).grid(column=1,row=1,padx=10,columnspan=2)
ttk.Label(tabExpedia, text="More Information from Expedia").grid(column=0,row=0,padx=10,pady=10)
#Add Component for Expedia Tab
#End UI of Tabbed Pane
root.mainloop()

#print ("Hello world")