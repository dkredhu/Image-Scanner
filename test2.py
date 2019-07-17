from tkinter import *
import PIL
from tkinter import filedialog
import csv
import os.path
import os
import sys
from PIL import Image, ImageTk
import numpy
import cv2
import pytesseract
from pyzbar import pyzbar
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.title("Image Reader")
        root.state('zoomed')
        root.geometry("1400x900")
        self.current = None
        self.right = None
        self.r =0
        self.count = None
        self.stopCamera = None
        self.isCameraOpen  = FALSE
        self.forget = None


        self.root = root
        with open('csvfile.csv','a',newline='') as csv:
            print("opened")

        self.topbar = Frame(root, width=200, bg='skyblue', height=50, relief='sunken', borderwidth=2,)
        self.topbar.pack(expand=False, fill='both', side='top', anchor='nw')

        # sidebar
        self.sidebar = Frame(root, width=30, bg='white', height=500, relief='sunken', borderwidth=2)
        self.openfile = Button(self.sidebar, text="Add File", width=5, height=2, command=self.first)
        self.openfile.grid(row=0)

        self.sidebar.pack(expand=False, fill='y', side='left', anchor='nw')

        self.rightbar = Frame(self.root, width=300, bg='white', height=500, relief='sunken', borderwidth=2)
        self.rightbar.pack(expand=False, fill='y', side='right', anchor='ne')

        self.downbar = Frame(self.root, width=300, bg='white', height=200, relief='sunken', borderwidth=2)
        self.downbar.pack(expand=False, fill='both', side='bottom', anchor='s')

        # main content area
        self.mainarea = Frame(root, bg='#CCC', width=400, height=500,relief = 'raised',borderwidth = 2)
        self.mainarea.pack(expand=True, fill='both', side='top')

        #self.rightbar = Frame(self.mainarea, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
        #self.rightbar.pack(expand=False, fill='both', side='right', anchor='ne')



        # self.menulabel = Label(self.topbar,text = "Menu",height = 3,width = 5,relief = 'raised',borderwidth = 2,bg = 'white')
        # self.menulabel.pack(side = 'left',expand  = False)

        self.add = Button(self.downbar, text="Add Field", height=2, width=10, relief='raised', command=self.writecsv)
        self.add.pack(expand=False, side='top', anchor="n")

        self.fieldvalue = StringVar()

        self.filename = Entry(self.downbar, bd=5, width=20, textvariable=self.fieldvalue)
        self.filename.pack(side = "top",expand = False)



        self.openfile = Button(self.sidebar, text="Add File", width=5, height=2, command=self.first)
        self.openfile.grid(row=0)
        self.openCamera = Button(self.sidebar, text="Camera", width=5, height=2, command=self.opnCamera)
        self.openCamera.grid(row=1)
        # self.clseCamera = Button(self.sidebar, text="Close Camera", width=5, height=2, command=self.closeCamera)
        # self.clseCamera.grid(row=2)

        # self.makelabels = Button(self.downbar,text = "Show Data",width = 10,relief = "raised",command = self.createlabels)
        # self.makelabels.pack(expand = False, side = 'top',anchor = 'n')

        #self.choosefile = Button(self.downbar, text="Choose File", width=10, relief="raised", command=self.choosecsvfile)
        #self.choosefile.pack(expand=False, side='top', anchor='ne')






        #MenuBar Creation and Command Buttons
        self.menubar = Menu(root)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.hello)
        self.filemenu.add_command(label="Save", command=self.hello)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # create more pulldown menus
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.hello)
        self.editmenu.add_command(label="Copy", command=self.hello)
        self.editmenu.add_command(label="Paste", command=self.hello)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.hello)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # display the menu
        root.config(menu=self.menubar)



#creating CSV file and Writing data in csv file
    def writecsv(self):
        data = (self.fieldvalue.get())


        # self.Savecsvfile = filedialog.asksaveasfile(defaultextension=".csv",
        #                                        filetype=[("All Files", "*.*"), ("CSV file", "*.csv")])
        # self.csvfile = filedialog.askopenfilename(defaultextension=".csv",
        #                                      filetype=[("All Files", "*.*"), ("CSV file", "*.csv")])
        with open('csvfile.csv', 'a', newline='') as csvfile:
             self.fieldnames = ['name', 'uid','gender','yob','co','po','dist','state','pc']
             self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
             if self.count is None:
                self.writer.writeheader()
             self.writer.writerow({'name': self.name , 'uid': self.uid , 'gender': self.gender, 'yob':self.YearOfBirth,'co': self.Gurdianname,'po': self.postoffice,'dist': self.dist,'state': self.state,'pc':self.pincode, })
             self.count = csvfile
        with open('csvfile.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                print(row)

        self.createlabels()
# showing up selected tiff image in mainarea Frame


    def labels(self):
        if self.forget is not None:
            self.rightbarlabel1.grid_forget()
            self.rightbarentry1.grid_forget()
            self.rightbarlabel2.grid_forget()
            self.rightbarentry2.grid_forget()
            self.rightbarlabel3.grid_forget()
            self.rightbarentry3.grid_forget()
            self.rightbarlabel4.grid_forget()
            self.rightbarentry4.grid_forget()
            self.rightbarlabel5.grid_forget()
            self.rightbarentry5.grid_forget()
            self.rightbarlabel6.grid_forget()
            self.rightbarentry6.grid_forget()
            self.rightbarlabel7.grid_forget()
            self.rightbarentry7.grid_forget()
            self.rightbarlabel8.grid_forget()
            self.rightbarentry8.grid_forget()
            self.rightbarlabel9.grid_forget()
            self.rightbarentry9.grid_forget()
            self.forget =None
        self.rightbarlabel1 = Label(self.rightbar, text='Name', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel1.grid(row=0)
        self.entrytext = StringVar()
        self.rightbarentry1 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.name)
        self.rightbarentry1.grid(row=0, column=1)
        self.rightbarlabel2 = Label(self.rightbar, text='UID', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel2.grid(row=1)
        self.entrytext = StringVar()
        self.rightbarentry2 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.uid)
        self.rightbarentry2.grid(row=1, column=1)
        self.rightbarlabel3 = Label(self.rightbar, text='Year of Birth', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel3.grid(row=2)
        self.entrytext = StringVar()
        self.rightbarentry3 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.YearOfBirth)
        self.rightbarentry3.grid(row=2, column=1)
        self.rightbarlabel4 = Label(self.rightbar, text='State', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel4.grid(row=3)
        self.entrytext = StringVar()
        self.rightbarentry4 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.state)
        self.rightbarentry4.grid(row=3, column=1)
        self.rightbarlabel5 = Label(self.rightbar, text='Co', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel5.grid(row=4)
        self.entrytext = StringVar()
        self.rightbarentry5 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.Gurdianname)
        self.rightbarentry5.grid(row=4, column=1)
        self.rightbarlabel6 = Label(self.rightbar, text='Pincode', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel6.grid(row=5)
        self.entrytext = StringVar()
        self.rightbarentry6 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.pincode)
        self.rightbarentry6.grid(row=5, column=1)
        self.rightbarlabel7 = Label(self.rightbar, text='District', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel7.grid(row=6)
        self.entrytext = StringVar()
        self.rightbarentry7 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.dist)
        self.rightbarentry7.grid(row=6, column=1)
        self.rightbarlabel8 = Label(self.rightbar, text='Gender', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel8.grid(row=7)
        self.entrytext = StringVar()
        self.rightbarentry8 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.gender)
        self.rightbarentry8.grid(row=7, column=1)
        self.rightbarlabel9 = Label(self.rightbar, text='Post office', height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel9.grid(row=8)
        self.entrytext = StringVar()
        self.rightbarentry9 = Entry(self.rightbar, bd=5, width=20, textvariable=self.entrytext, relief=GROOVE)
        self.entrytext.set(self.postoffice)
        self.rightbarentry9.grid(row=8, column=1)
        self.forget = self.rightbarentry1
    def first(self):
        global current
        self.sumwid = 0
        self.sumhei = 0
        self.file = filedialog.askopenfilename()
        if self.isCameraOpen is True:
            self.lmain.pack_forget()


        extension = os.path.splitext(self.file)[1]
        print(extension)
        config = ('-l eng --oem 1 --psm 3')
        self.im1 = cv2.imread(self.file, 0)
        #text = pytesseract.image_to_string(self.im1, config=config)

        #print(text)
        barcode = pyzbar.decode(self.im1)
        print(type(barcode))

        barcodeData = ''
        #barcodeData = barcode.data.decode("utf-8")
        for obj in barcode:
            self.barcodeData = obj.data.decode("utf-8")
            self.barcodeType = obj.type
            text = "{} ({})".format(self.barcodeData, self.barcodeType)
            #print(text)
            print("barcode: {}".format(barcodeData))
            q = 0
        #barcodeData2 = str(barcodeData)
        #with open('newxml.xml') as fb:







        # tree = ET.parse('newxml.xml')
        # root = tree.getroot()
        # for child in root:
        #     print(child.tag, child.attrib)
        # for data in root.bind_all('PrintLetterBarcodeData'):
        #     Userinformation[q] = data
        #     q += 1





        self.im = Image.open(self.file)
        self.im.load()
        self.im.thumbnail((1400, 1000), Image.ANTIALIAS)
        if extension =='.JPG' or extension == '.JPEG' or extension == '.jpeg' or extension == '.jpg' or extension == '.png' or extension == '.PNG':
            self.frames = 1
        else:
            self.frames = self.im.n_frames
        self.wid = (self.im.width)
        self.hei = (self.im.height)
        #print(self.frames)
        if self.current is not None:
            self.canvas.pack_forget()
            self.horizontal.pack_forget()
            self.vertical.pack_forget()

        self.image = []


        # file = filedialog.askopenfilename()
        # img = Image.open(file)

        # print(width, height)
        #self.height,self.width  = self.im.size()
        self.canvas = Canvas(self.mainarea, relief=SUNKEN, confine='false')
        #self.canvas.config(scrollregion=(0,0,1000, 1000))
        # canv.configure(scrollregion=canv.bbox('all'))
        self.canvas.config(highlightthickness=0)
        self.canvas.config(width=700, height=800)

        self.vertical = Scrollbar(self.canvas, orient=VERTICAL)
        self.horizontal = Scrollbar(self.canvas, orient=HORIZONTAL)

        self.vertical.config(command=self.canvas.yview)
        self.horizontal.config(command=self.canvas.xview)

        self.canvas.config(yscrollcommand=self.vertical.set)
        self.canvas.config(xscrollcommand=self.horizontal.set)

        self.vertical.pack(side=RIGHT, fill=Y)
        self.horizontal.pack(side=BOTTOM, fill=X)

        self.canvas.pack(side=LEFT, expand=YES, fill='both')

        self.photoimage = []
        self.resizeimg = []
        #self.labels = ['label1', 'label2', 'label3', 'label4''label5', 'label6', 'label7', 'label8', 'label9', 'label10']
        self.placex = 30
        self.placey = 0
        self.canvas.config(scrollregion=(0, 0, self.wid, self.sumhei))
        if self.frames is 1:

            self.photoimage = ImageTk.PhotoImage(self.im)

            # self.wid = (self.photoimage.width)
            # self.hei = (self.photoimage.height)

            self.canvas.config(scrollregion=(0, 0, self.wid, self.hei), confine=True)
            # self.vertical.config(command=self.cv1.yview)
            # self.horizontal.config(command=self.cv1.xview)
            # self.cv1.config(yscrollcommand=self.vertical.set)
            # self.cv1.config(xscrollcommand=self.horizontal.set)
            self.canvas.create_image(self.placex, self.placey, image=self.photoimage, anchor=NW)
            self.current = self.canvas
        else:

            for i in range(0, self.frames):
                self.im.seek(i)
                print(self.im.seek(i))
                #print(i)
                self.photoimage.append("image" + str(i))

                self.image.append('img' + str(i))
                self.resizeimg.append('resize' + str(i))

                #self.imarray = cv2.imreadmulti(self.file, -1)
                #print(self.imarray.shape)
                self.width, self.height = self.im.size

                #if self.width > 700 or self.height > 800:
                self.resizeimg[i] = self.im.resize((int(self.width / 2.7), int(self.height / 2.7)), Image.ANTIALIAS)
                #self.resizeimg[i] = self.im.resize((int(self.width / 1), int(self.height / 1)), Image.ANTIALIAS)
                self.imarray = numpy.array(self.resizeimg[i])
                print(self.imarray.shape)
                self.image[i] = Image.fromarray(self.imarray.reshape((self.imarray.shape)).astype('uint8') * 255)


                # print(im.size)
                # print(imarray)
                #self.image[i] = Image.fromarray(self.imarray)
                self.photoimage[i] = ImageTk.PhotoImage(self.image[i])
                self.wid = self.photoimage[i].width()
                self.hei = self.photoimage[i].height()
                print(self.wid)
                print(self.hei)
                self.sumwid = self.sumwid + self.wid
                self.sumhei = self.sumhei + self.hei
                print(self.sumwid)
                print(self.sumhei)
                self.canvas.config(width=self.sumwid, height=self.sumhei)
                #self.canvas.configure(scrollregion=self.canvas.bbox('all'))
                self.canvas.config(scrollregion=(0, 0, self.wid, self.sumhei),confine = True)
                # self.vertical.config(command=self.canvas.yview)
                # self.horizontal.config(command=self.canvas.xview)
                # self.canvas.config(yscrollcommand=self.vertical.set)
                # self.canvas.config(xscrollcommand=self.horizontal.set)
                self.canvas.create_image(self.placex, self.placey, image=self.photoimage[i], anchor=NW)
                self.placey = self.placey + self.hei
                self.current =self.canvas
            print(self.photoimage)
            print(self.image)
        self.userdata()
        # file = filedialog.askopenfilename()
        # print(file)
        # load = Image.open(file)
        # image = ImageTk.PhotoImage(load)
        #
        #
        # if self.current is not None:
        #     self.current.pack_forget()
        # label1 = Label(self.mainarea, text="Here is project 1", height=500, width=400, image=image)
        # label1.image = image
        #
        # label1.pack(expand="True", fill="both")
        # self.current = label1

    def closeCamera(self):
        print('camera closed')
        cv2.VideoCapture.release(self.cap)
        self.cap.release()
        cv2.destroyAllWindows()
        self.lmain.pack_forget()
        self.isCameraOpen  = FALSE

    def opnCamera(self):
        print('open camera')
        # if self.stopCamera is not None:
        #     self.closeCamera(self)
        width, height = 800, 600
        self.lmain = Label(self.mainarea)
        self.lmain.pack()
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.stopCamera = self.lmain
        self.isCameraOpen = True

        self.countframes = 0

        def show_frame():
            self.countframes += 1
            print(self.countframes)
            if self.countframes >= 200:
                self.closeCamera()



            _, self.mainarea = self.cap.read()
            self.mainarea = cv2.flip(self.mainarea, 1)
            #frame = cv2.flip(self.mainarea, 1)
            img = numpy.array(self.mainarea, dtype=numpy.uint8)
            cv2image = cv2.cvtColor(self.mainarea,cv2.COLOR_BGR2RGBA)
            imgs = PIL.Image.fromarray(cv2image)

            imgtk = ImageTk.PhotoImage(image=imgs)
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)
            self.lmain.after(10, show_frame)

            #config = ('-l eng --oem 1 --psm 3')
            #self.im1 = cv2.imread(imgtk, 0)
            # text = pytesseract.image_to_string(self.im1, config=config)
            # width, height = img.size
            #zbar_image = pyzbar.zbar_image_create(frame)

            decodedObjects = pyzbar.decode(imgtk)
            #
            # # Scans the zbar image.
            # scanner = pyzbar._image_scanner(zbar_image)
            # scanner.scan(zbar_image)

            # Prints data from image.
            for decoded in decodedObjects:
                print(decoded.data)
            # # print(text)
            # barcode = pyzbar.decode(img)
            #
            # # barcodeData = barcode.data.decode("utf-8")
            # for obj in barcode:
            #     barcodeData = obj.data.decode("utf-8")
            #     barcodeType = obj.type
            #     text = "{} ({})".format(barcodeData, barcodeType)





        show_frame()


    def hello(self):
        print("hello!")



    # def choosecsvfile(self):
    #
    #     self.Savecsvfile = filedialog.asksaveasfile(defaultextension=".csv",
    #                                            filetype=[("All Files", "*.*"), ("CSV file", "*.csv")])
    #     self.csvfile = filedialog.askopenfilename(defaultextension=".csv",
    #                                          filetype=[("All Files", "*.*"), ("CSV file", "*.csv")])
    #
    #     try:
    #         s = os.stat(self.csvfile)
    #         if s.st_size == 0:
    #             print("The file {} is empty".format(self.csvfile))
    #             with open(self.csvfile, 'a', newline='') as csvfile:
    #                 self.fieldnames = ['first_name', 'last_name']
    #                 self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
    #                 self.writer.writeheader()
    #
    #         else:
    #             print("file is not empty")
    #     except OSError as e:
    #         print(e)


    def userdata(self):
        soup = BeautifulSoup(self.barcodeData, 'xml')
        data = soup.find('PrintLetterBarcodeData')
        # soup = BeautifulSoup(barcodeData, 'xml')
        # data = soup.find('PrintLetterBarcodeData')
        # Userinformation = ['uid','name','gender','yob','co','lm','loc','vtc','po','dist','state','pc','dob']
        userdata = []
        # Userinformation[0] = data[Userinformation[0]]
        print(data)
        try:


            self.uid = data['uid']
            self.name = data['name']
            self.gender = data['gender']
            self.YearOfBirth = data['yob']
            self.Gurdianname = data['co']
            # self.landmark = data['lm']
            #self.location = data['loc']
            self.dist = data['dist']
            #self.dateofbirth = data['dob']
            self.state = data['state']
            self.pincode = data['pc']
            self.postoffice = data['po']
            self.writecsv()
            self.labels()
        except Exception as e:
            print(e)
            self.writecsv()
            self.labels()


# creating labels  and entry widget in rightbar
    def createlabels(self):
        global r
        data = (self.fieldvalue.get())

        self.rightbarlabel = Label(self.rightbar, text=data, height=2, width=10, relief=GROOVE, borderwidth=3,
                                   bg='light blue', )
        self.rightbarlabel.grid(row =self.r)
        self.entrytext = StringVar()
        self.rightbarentry = Entry(self.rightbar,bd=5, width=20,textvariable = self.entrytext,relief = GROOVE)
        self.entrytext.set("")
        self.rightbarentry.grid(row =self.r,column = 1)
        self.r +=1


        # with open('csvfile.csv', mode='r') as csv_file:
        #     csv_reader = csv.DictReader(csv_file)
        #     line_count = 0
        #     self.info = StringVar()
        #     self.info ="none"
        #     r =0
        #
        #
        #     for row in csv_reader:
        #         if line_count == 0:
        #             print(f'Column names are {", ".join(row)}')
        #             line_count += 1
        #         if self.right is not None:
        #             self.rightbarlabel.pack_forget()
        #             self.rightbarentry.pack_forget()
        #
        #         if self.info == row["first_name"]:
        #             print("same name")
        #
        #
        #         else:
        #             self.rightbarlabel = Label(self.rightbar,text = data,height = 5,width = 10,relief = 'raised',borderwidth=3,bg = 'light blue',)
        #             self.rightbarlabel.grid(row =r)
        #             self.entrytext = StringVar()
        #             self.rightbarentry = Entry(self.rightbar,bd=5, width=20,textvariable = self.entrytext)
        #             self.entrytext.set("")
        #             self.rightbarentry.grid(row =r,column = 1)
        #             self.info = row["first_name"]
        #             r +=1
        #             self.right = self.rightbarlabel
        #
        #
        #             print(row["first_name"])
        #         line_count += 1
        #     print(f'Processed {line_count} lines.')
root = Tk()
my_gui = MyFirstGUI(root)
#cv2.VideoCapture.release()
root.mainloop()
