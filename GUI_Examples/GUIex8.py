from tkinter import *


class Application(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)

        self.grid(); self._skillList=[]

        self.name(); self.major(); self.yrsAttend(); self.skills(); self.text(); self.submit()

    def name(self):

        self._lblName=Label(self,text='Name:'); self._lblName.grid(row=0,column=0,sticky=W)

        self._txtName=Entry(self); self._txtName.grid(row=0,column=1,sticky=W)

    def major(self):

        self._lblMajor=Label(self,text='Major:'); self._lblMajor.grid(row=1,column=0,sticky=W)

        self._txtMajor=Entry(self); self._txtMajor.grid(row=1,column=1,sticky=W)

    def yrsAttend(self):

        self._lblYrs=Label(self,text='Yrs attended:'); self._lblYrs.grid(row=2,column=0,sticky=W)

        self.spinYrs=Spinbox(self,from_=0,to=10,state=NORMAL); self.spinYrs.grid(row=2,column=1,sticky=W)


    def skills(self):

        self._powerpoint=BooleanVar(); self._excel=BooleanVar(); self._word=BooleanVar()

        self._lblSkills=Label(self,text='Check all skills:'); self._lblSkills.grid(row=4,column=0,sticky=W)

        self._ckbxWord=Checkbutton(self,text='Word', variable=self._word,onvalue=True,offvalue=False)

        self._ckbxWord.grid(row=4,column=1,sticky=W)

    #Powerpoint

        self._ckbxPwrPt=Checkbutton(self,text='Powerpoint', variable=self._powerpoint,\
        onvalue=True, offvalue=False)

        self._ckbxPwrPt.grid(row=5,column=1,sticky=W)

        self._ckbxExcel=Checkbutton(self,text='Excel', variable=self._excel, onvalue=True, offvalue=False)

        self._ckbxExcel.grid(row=6,column=1,sticky=W)

    def submit(self):

        self._btnSubmit=Button(self,text='Submit',command=self.showInfo)

        self._btnSubmit.grid(row=7,column=0,sticky=W)

    def text(self):

        self._text=Text(self,width=40,height=5); self._text.grid(row=8,column=0,sticky=W)

    def updateSkillList(self):

        if self._word.get():
            self._skillList.append('Word')

        if self._excel.get():
            self._skillList.append('Excel')

        if self._powerpoint.get():
            self._skillList.append('Powerpoint')


    def showInfo(self):

        formattedString=''; self._skillList=[]

        nameString=self._txtName.get(); strMajor='Major: '+self._txtMajor.get(); 
        strYrs='Years attended: '+str(self.spinYrs.get())

        strSkill=''

        self.updateSkillList()

        for skill in self._skillList:

            strSkill+=skill+', '

            strSkill = strSkill[0:len(strSkill)-2]

            tmp=nameString+'\n'+strMajor+'\n'+strYrs+'\n'+strSkill+'\n'

            self._text.delete(0.0,END)

            self._text.insert(0.0,tmp)

root=Tk()
        

root.title('Student Information')


app=Application(root)

root.mainloop()
