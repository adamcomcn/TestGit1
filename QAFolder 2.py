import tkinter as tk
import os

path='\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\'
path1 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\1 Certificates\\'
path2 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\2 Management Review\\'
path4 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\4 Policy & Plans\\'
path5 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\5 External Audit\\'
path6 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\6 Internal Audit\\'
path7 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\7 System Procedures\\'
path8 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\8 SOPs&WIs\\'
path9 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\9 Forms\\'
path11 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\11 Document Change Control\\'
path12 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\12 Supplier Management\\'
path13 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\13 Registers\\'
path14 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\Miscellaneous\\'
path15 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\Production Quality Meeting\\'
path16 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\Quality & Reliability\\'
path17 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\Quality Awareness\\'
path18 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\Quality Management System\\Safety System\\'

path001 = 'G:\\engarch\\dwg\\All Dwg\\'
path002 = '\\\\mygme\\mygmedocuments\\Engineering\\Non Version Controlled Docs\\ECO Registers\\'
path002A = '\"G:\\engarch\Scanned ECO, MPE, PCR and New Part Forms\\2013 onwards\\ECO Forms - 2013 onwards (front only)\"'
path003 = '\\\\mygme\\mygmedocuments\\Engineering\\Version Controlled Docs\\Master Registers\\'
path004 = '\\\\nswfs01\\Departments\\Manufacturing\\Daily Test Report\\'
path005 = '\\\\nswfs01\\Departments\\Manufacturing\\Manufacturing Technician Report\\'
# path003 = '\\\\nswfs01\\Departments\\Engineering\\Mechanical'

path0001 = 'F:\\'
path0002 = 'F:\\Manufacturing Equipment Calibration\\'
path0003 = 'F:\\Nonconformance Reports by Part Number\\'
path0004 = 'F:\\Concessions\\'
path0005 = '\\\\nswfs01\\Departments\\Restricted\\Management System\\CAR\\'

# menubar = tk.Menu(root)
# filemenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='About', menu=filemenu)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "QMS"
        self.hi_there["command"] = self.qms
        self.hi_there.grid(row=1, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "1.Certificates"
        self.hi_there["command"] = self.certificates
        self.hi_there.grid(row=2, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "2.Management Review"
        self.hi_there["command"] = self.managementreview
        self.hi_there.grid(row=3, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "4.Policy & Plans"
        self.hi_there["command"] = self.policyandplans
        self.hi_there.grid(row=4, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "5.External Audit"
        self.hi_there["command"] = self.externalaudit
        self.hi_there.grid(row=5, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "6.Internal Audit"
        self.hi_there["command"] = self.internalaudit
        self.hi_there.grid(row=6, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "7.System Procedures"
        self.hi_there["command"] = self.systemprocedures
        self.hi_there.grid(row=7, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "8.SOPs & WIs"
        self.hi_there["command"] = self.sOPsWIs
        self.hi_there.grid(row=8, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "9.Forms"
        self.hi_there["command"] = self.forms
        self.hi_there.grid(row=9, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "11.Document Change Control"
        self.hi_there["command"] = self.dcc
        self.hi_there.grid(row=10, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "12.Supplier Management"
        self.hi_there["command"] = self.suppliermanagement
        self.hi_there.grid(row=11, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "13.Registers"
        self.hi_there["command"] = self.registers
        self.hi_there.grid(row=12, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Miscellaneous"
        self.hi_there["command"] = self.miscellaneous
        self.hi_there.grid(row=13, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Production Quality Meeting"
        self.hi_there["command"] = self.pqm
        self.hi_there.grid(row=14, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Quality & Reliability"
        self.hi_there["command"] = self.qr
        self.hi_there.grid(row=15, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Quality Awareness"
        self.hi_there["command"] = self.qualityawareness
        self.hi_there.grid(row=16, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Safety System"
        self.hi_there["command"] = self.ss
        self.hi_there.grid(row=17, column=1, padx=10, pady=10)

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Safety System"
        # self.hi_there["command"] = self.ss
        # self.hi_there.grid(row=17, column=1, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Engineering Drawings"
        self.hi_there["command"] = self.ed
        self.hi_there.grid(row=1, column=2, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "ECO Registers"
        self.hi_there["command"] = self.eco
        self.hi_there.grid(row=2, column=2, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Scanned ECOs"
        self.hi_there["command"] = self.ecos
        self.hi_there.grid(row=3, column=2, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Master Register"
        self.hi_there["command"] = self.mr
        self.hi_there.grid(row=4, column=2, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Daily Test Report"
        self.hi_there["command"] = self.dtr
        self.hi_there.grid(row=5, column=2, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Repair Reports"
        self.hi_there["command"] = self.rr
        self.hi_there.grid(row=6, column=2, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "QA"
        self.hi_there["command"] = self.qa
        self.hi_there.grid(row=1, column=3, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Calibration"
        self.hi_there["command"] = self.cal
        self.hi_there.grid(row=2, column=3, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "NCRs"
        self.hi_there["command"] = self.ncr
        self.hi_there.grid(row=3, column=3, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Concessions"
        self.hi_there["command"] = self.conc
        self.hi_there.grid(row=4, column=3, padx=10, pady=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "CARs"
        self.hi_there["command"] = self.car
        self.hi_there.grid(row=5, column=3, padx=10, pady=10)

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "QMS"
        # self.hi_there["command"] = self.qms
        # self.hi_there.pack(side="left")

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "System Procedure"
        # self.hi_there["command"] = self.systemprocedure
        # self.hi_there.place(x=20, y=10, anchor='nw')

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "QMS"
        # self.hi_there["command"] = self.qms
        # self.hi_there.grid(row=1, column=1, padx=10, pady=10)

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "NCR"
        # self.hi_there["command"] = self.ncr
        # self.hi_there.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=16, column=3, padx=10, pady=10)
        # self.quit.pack(side="bottom")

        self.hi_there = tk.Label(self, text='by Jayson', font = 'Helvetica -12 bold', fg="black")
        self.hi_there.grid(row=17, column=3, padx=10, pady=10)

        # self.hi_there = tk.Menu(self)
        # filemenu = tk.Menu(menubar, tearoff=0)
        # menubar.add_cascade(label='', menu=filemenu)


    def qms(self):
        os.system("start explorer %s" % path)

    def certificates(self):
        os.system("start explorer %s" % path1)

    def managementreview(self):
        os.system("start explorer %s" % path2)

    def policyandplans(self):
        os.system("start explorer %s" % path4)

    def externalaudit(self):
        os.system("start explorer %s" % path5)

    def internalaudit(self):
        os.system("start explorer %s" % path6)

    def systemprocedures(self):
        os.system("start explorer %s" % path7)

    def sOPsWIs(self):
        os.system("start explorer %s" % path8)

    def forms(self):
        os.system("start explorer %s" % path9)

    def dcc(self):
        os.system("start explorer %s" % path11)

    def suppliermanagement(self):
        os.system("start explorer %s" % path12)

    def registers(self):
        os.system("start explorer %s" % path13)

    def miscellaneous(self):
        os.system("start explorer %s" % path14)

    def pqm(self):
        os.system("start explorer %s" % path15)

    def qr(self):
        os.system("start explorer %s" % path16)

    def qualityawareness(self):
        os.system("start explorer %s" % path17)

    def ss(self):
        os.system("start explorer %s" % path18)

    def ed(self):
        os.system("start explorer %s" % path001)

    def eco(self):
        os.system("start explorer %s" % path002)

    def ecos(self):
        os.system("start explorer %s" % path002A)

    def mr(self):
        os.system("start explorer %s" % path003)

    def dtr(self):
        os.system("start explorer %s" % path004)

    def rr(self):
        os.system("start explorer %s" % path005)

    def qa(self):
        os.system("start explorer %s" % path0001)

    def cal(self):
        os.system("start explorer %s" % path0002)

    def ncr(self):
        os.system("start explorer %s" % path0003)

    def conc(self):
        os.system("start explorer %s" % path0004)

    def car(self):
        os.system("start explorer %s" % path0005)

root = tk.Tk()
root.title('Quality Department')

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='', menu=filemenu)
filemenu.add_command(label='New')

#root.geometry('450x800')
#root.configure(bg='black')
app = Application(master=root)
#app['bg'] = 'grey'
# frm = tk.Frame(root)
# frm.grid()
# frm_r = tk.Frame(frm)
# frm_r.pack(side='right')
#tk.Label(frm_r, text='by Jayson').grid(row=17, column=3, padx=10, pady=10)
app.mainloop()