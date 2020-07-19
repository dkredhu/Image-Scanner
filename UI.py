from tkinter import *

root = Tk()

class UI:
    def __init__(self,root):
        self.root = root
        root.title("Image Reader")
        #root.state('zoomed')
        root.geometry("900x600")
        self.current = None
        self.count = 0
        self.nextcount = 1




        self.topbar = Frame(root, width=200, bg='white', height=50, relief='sunken', borderwidth=2, )
        self.topbar.pack(expand=False, fill='both', side='top', anchor='nw')

        self.frame1 = Frame(root, width=200, bg='white', height=200, relief='sunken', borderwidth=1)
        self.broButton = Label(self.frame1, text='Next', height=2, width=6,bg = "light green",borderwidth=2,bd =3,padx =2, pady =2)
        self.broButton.grid(row=1, column=0)

        self.frame1.pack(expand=True, fill='both', side='left', anchor='nw')


        self.frame2 = Frame(self.root, width=700, bg='white', height=700, relief='sunken', borderwidth=2)
        self.frame2.pack(expand=False, fill='both', side='left', anchor='nw')

        self.broButton.bind('<ButtonPress-1>', self.on_mouse_down)



    def on_mouse_down(self, event):
        if self.current is not None:
            self.current = None
            self.broButton.config(bg="light Blue")
            self.broButton2.grid_forget()
            self.broButton3.grid_forget()
            self.broButton4.grid_forget()
            self.broButton5.grid_forget()
            self.broButton6.grid_forget()
            self.broButton7.grid_forget()
            self.broButton8.grid_forget()
            self.broButton9.grid_forget()
            self.broButton10.grid_forget()




        else:

            self.broButton2 = Label(self.frame1, text='Next', height=2, width=6, bg="light green", borderwidth=2)
            self.broButton2.grid(row =2, column = 1)
            self.current = self.broButton2
            self.broButton2.bind('<ButtonPress-1>', self.on_mouse_down2)

    def on_mouse_down2(self,event):
        if self.current == self.frame1:
            self.broButton2.config(bg="light Blue")
            self.broButton3.config(bg="light green")
            self.broButton4.grid_forget()
            self.broButton5.grid_forget()
            self.broButton6.grid_forget()
            self.broButton7.grid_forget()
            self.broButton8.grid_forget()
            self.broButton9.grid_forget()
            self.broButton10.grid_forget()
            self.broButton4.grid(row=4, column=1)
            self.broButton5.grid(row=5, column=1)
            self.broButton6.grid(row=6, column=1)
            self.count +=1
        # elif self.nextcount%2==0:
        #     self.broButton2.config(bg="light Blue")
        #     self.broButton3.config(bg="light green")
        #     self.broButton4.grid_forget()
        #     self.broButton5.grid_forget()
        #     self.broButton6.grid_forget()
        #     # self.broButton7.grid_forget()
        #     # self.broButton8.grid_forget()
        #     # self.broButton9.grid_forget()
        #     # self.broButton10.grid_forget()
        #     self.broButton4.grid(row=4, column=1)
        #     self.broButton5.grid(row=5, column=1)
        #     self.broButton6.grid(row=6, column=1)
        #     self.count += 1
        #     self.nextcount +=1
        #     self.current = self.frame1

        else:
            self.broButton2.config(bg="light Blue")
            self.broButton3 = Label(self.frame1, text='Files', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton3.grid(row=3, column=1)
            self.broButton4 = Label(self.frame1, text='log', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton4.grid(row=4, column=1)
            self.broButton5 = Label(self.frame1, text='External Lib', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton5.grid(row=5, column=1)
            self.broButton6 = Label(self.frame1, text='Code Files', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton6.grid(row=6, column=1)
            self.current = self.frame1
            self.count += 1
            self.nextcount += 1
            print(self.count)

        self.broButton3.bind('<ButtonPress-1>', self.on_mouse_down3)

    def on_mouse_down3(self, event):
        if self.count%2==0:
            self.broButton2.config(bg="light Blue")
            self.broButton3.config(bg="light green")
            self.broButton4.grid_forget()
            self.broButton5.grid_forget()
            self.broButton6.grid_forget()
            self.broButton7.grid_forget()
            self.broButton8.grid_forget()
            self.broButton9.grid_forget()
            self.broButton10.grid_forget()
            self.broButton4.grid(row=4, column=1)
            self.broButton5.grid(row=5, column=1)
            self.broButton6.grid(row=6, column=1)
            self.count += 1
        # elif self.count % 2 == 0:
        #     self.broButton2.config(bg="light Blue")
        #     self.broButton3.config(bg="light green")
        #     self.broButton4.grid_forget()
        #     self.broButton5.grid_forget()
        #     self.broButton6.grid_forget()
        #     self.broButton7.grid_forget()
        #     self.broButton8.grid_forget()
        #     self.broButton9.grid_forget()
        #     self.broButton10.grid_forget()
        #     self.broButton4.grid(row=4, column=1)
        #     self.broButton5.grid(row=5, column=1)
        #     self.broButton6.grid(row=6, column=1)
        #     self.count += 1



        else:

            self.broButton4.grid_forget()
            self.broButton5.grid_forget()
            self.broButton6.grid_forget()
            self.broButton2.config(bg="light green")
            self.broButton3.config(bg = "light Blue")


            self.broButton4.grid(row=8, column=1)
            self.broButton5.grid(row=9, column=1)
            self.broButton6.grid(row=10, column=1)
            self.broButton7 = Label(self.frame1, text='new', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton7.grid(row=4, column=2)
            self.broButton8 = Label(self.frame1, text='new1', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton8.grid(row=5, column=2)
            self.broButton9 = Label(self.frame1, text='Libararies', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton9.grid(row=6, column=2)
            self.broButton10 = Label(self.frame1, text='Lookup', height=2, width=10, bg="light green", borderwidth=2)
            self.broButton10.grid(row=7, column=2)
            self.current = self.frame1



MyUI = UI(root)


mainloop()


from pandas import *
import pandas as pd
import numpy as np
import tabula
import PyPDF2
import sys
def convert_pdf_csv(pdf_file,output):
    reader = PyPDF2.PdfFileReader(open(pdf_file, mode='rb'))
    m = reader.getNumPages()
    data = tabula.read_pdf(pdf_file, encoding='utf-8', spreadsheet=True, pages='1-%d'% m)
    value = data.keys()
    header = data.keys()
    data1 =  data
    data1 = data.applymap(str)
    for col in header:
        for words in value:
            data[col] = data[col].replace(words, '')
            data1[col] = data1[col].replace(words, '')
    if 'Unnamed: 0' in header:
        del data['Unnamed: 0']
    if 'TRANSACTI\rNG\rPERSON' in header:
        data['TRANSACTI\rNG\rPERSON'] = data['TRANSACTI\rNG\rPERSON'].replace(to_replace=r'\r',value=' ',regex=True)
        data1['TRANSACTI\rNG\rPERSON'] = data1['TRANSACTI\rNG\rPERSON'].replace(to_replace=r'\r', value=' ', regex=True)
        indexas= data1[data1['ACCOUNT'] == 'nan'].index
        indexas2 = data1[data1['ACCOUNT'] == ''].index
        data.drop(indexas, inplace=True)
        data.drop(indexas2, inplace=True)
    if 'ACTDATETI\rME' in header:
        data['OWNER'] = data['OWNER'].replace(to_replace=r'\r', value=' ', regex=True)
        data1['OWNER'] = data['OWNER'].replace(to_replace=r'\r', value=' ', regex=True)
        data['ACTDATETI\rME'] = data['ACTDATETI\rME'].replace(to_replace=r'\r', value=' ', regex=True)
        data1['ACTDATETI\rME'] = data1['ACTDATETI\rME'].replace(to_replace=r'\r', value=' ', regex=True)
        indexas = data1[data1['ACTDATETI\rME'] == 'nan'].index
        indexas2 = data1[data1['ACTDATETI\rME'] == ''].index
        data.drop(indexas, inplace=True)
        data.drop(indexas2, inplace=True)

    data.to_csv(output, index=False, header=True,)


if __name__ == "__main__":
    if len(sys.argv)==3:
        pdf_file = sys.argv[1]
        output = sys.argv[2]
        convert_pdf_csv(pdf_file, output)

convert_pdf_csv(r'pdf/PHP VALUATION 2020-01-31.pdf','pdf/PHP VALUATION 2020-01-31.pdf.csv')

