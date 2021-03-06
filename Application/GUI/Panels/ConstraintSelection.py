# Copyright Notice
# ================
# 
# The PyMOL Plugin source code in this file is copyrighted, but you can
# freely use and copy it as long as you don't change or remove any of
# the copyright notices.
# 
# ----------------------------------------------------------------------
#               This PyMOL Plugin is Copyright (C) 2013 by 
#                 olivier serve <olivier dot serve at gmail dot com>
# 
#                        All Rights Reserved
# 
# Permission to use, copy, modify, distribute, and distribute modified
# versions of this software and its documentation for any purpose and
# without fee is hereby granted, provided that the above copyright
# notice appear in all copies and that both the copyright notice and
# this permission notice appear in supporting documentation, and that
# the name(s) of the author(s) not be used in advertising or publicity
# pertaining to distribution of the software without specific, written
# prior permission.
# 
# THE AUTHOR(S) DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.  IN
# NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
# ----------------------------------------------------------------------

import Tkinter as Tk
import Pmw

from Panel import Panel


class ConstraintSelectionPanel(Panel):
    def __init__(self, master):
        Panel.__init__(self, master, frameText="Constraints Selection")
        self.panelsList = []
        self.widgetCreation()

    def widgetCreation(self):
        #Creation of range input
        self.consRangeFrame = RangeSelectionPanel(self)
        self.consRangeFrame.grid(row=0, column=0)
        self.panelsList.append(self.consRangeFrame)

        #Creation of Violations inputs
        self.violationsFrame = ViolationSelectionPanel(self)
        self.violationsFrame.grid(row=0, column=1)
        self.panelsList.append(self.violationsFrame)

        #Creation of structure inputs
        self.structureManagement = StructureSelectionPanel(self)
        self.structureManagement.grid(row=1, column=0, columnspan=2)
        self.panelsList.append(self.structureManagement)

    def getInfo(self):
        infos = {}
        for panel in self.panelsList:
            infos.update(panel.getInfo())
        return infos

class RangeSelectionPanel(Panel):
    def __init__(self, master):
        Panel.__init__(self, master, frameText="Range Selection")

        self.RangesVars = {}
        self.RangesCB = {}
        self.RangesFunctions = {}
        self.widgetCreation()

    def widgetCreation(self):
        rowPosition=0
        for consRange in ['intra', 'sequential', 'medium', 'long']:
            self.RangesVars[consRange] = Tk.IntVar(self)
            self.RangesCB[consRange] = Tk.Checkbutton(self, text=': ' + consRange, command=self.tick, variable=self.RangesVars[consRange])
            self.RangesCB[consRange].grid(row=rowPosition, column=0, sticky=Tk.W)
            rowPosition=rowPosition + 1
        self.RangesVars["all"] = Tk.IntVar(self)
        self.RangesCB["all"] = Tk.Checkbutton(self, text=': all', command=self.tickAll, variable=self.RangesVars["all"])
        self.RangesCB["all"].grid(row=rowPosition, column=0, sticky=Tk.W)
        self.RangesCB["all"].invoke()

    def tickAll(self):
        if self.RangesVars["all"].get() == 1:
            for consRange in ['intra', 'sequential', 'medium', 'long']:
                self.RangesCB[consRange].select()
        if self.RangesVars["all"].get()==0:
            for consRange in ['intra', 'sequential', 'medium', 'long']:
                self.RangesCB[consRange].deselect()
    def tick(self):
        self.RangesCB["all"].select()
        for aRange in ['intra', 'sequential', 'medium', 'long']:
            if self.RangesVars[aRange].get() == 0:
                self.RangesCB["all"].deselect()
                break
    def getInfo(self):
        ranges=[]
        for consRange in ['intra', 'sequential', 'medium', 'long']:
            if self.RangesVars[consRange].get()==1:
                ranges.append(consRange)
        return {"residuesRange":ranges}

class ViolationSelectionPanel(Panel):
    def __init__(self, master):
        Panel.__init__(self, master, frameText="Violation state Selection")

        self.ViolationsVars = {}
        self.ViolatedCB = {}
        self.cutOff = Tk.DoubleVar(self)
        self.widgetCreation()

    def widgetCreation(self):
        rowPosition = 0
        for violationType in ['violated', 'not violated']:
            self.ViolationsVars[violationType] = Tk.IntVar(self)
            self.ViolatedCB[violationType] = Tk.Checkbutton(self, text=': ' + violationType, variable=self.ViolationsVars[violationType])
            self.ViolatedCB[violationType].grid(row=rowPosition, column=0, sticky=Tk.W)
            self.ViolatedCB[violationType].select()
            rowPosition = rowPosition + 1

        Tk.Label(self, text='Distance CutOff (A)').grid(row=rowPosition + 1, column=0)

        self.spinBox_cutOff = Tk.Spinbox(self, textvariable=self.cutOff, from_=0.0, to=10.0, increment=0.1)
        self.spinBox_cutOff.grid(row=rowPosition+2, column=0)

    def getInfo(self):
        violationState = []
        for violationType in ['violated','not violated']:
            if self.ViolationsVars[violationType].get() == 1:
                violationState.append(violationType)
        return {"cutOff": self.cutOff.get(), "violationState": violationState}

class StructureSelectionPanel(Panel):
    def __init__(self, master):
        Panel.__init__(self, master, frameText="Structure")
        self.residueRanges = Tk.StringVar(self)
        self.widgetCreation()

    def widgetCreation(self):
        Tk.Label(self, text="Structure :").grid(row=0, column=0)
        x = Pmw.EntryField()#Do not remove this line if combobox is the first Pmw combobox, Pmw bug
        self.comboPDB = Pmw.ComboBox(self)
        self.comboPDB.grid(row=0, column=1)
        self.comboPDB.bind('<Enter>', self.updatePdbList)

        Tk.Label(self, text = 'Residues ranges :').grid(row=2, column=0, sticky=Tk.W)
        self.entry_res = Tk.Entry(self, textvariable=self.residueRanges)
        self.entry_res.grid(row=2, column=1)
        self.residueRanges.set('all')

    def getInfo(self):
        return {"pdb": self.comboPDB.component("entryfield").getvalue(), "ranges": self.residueRanges.get()}

    def updatePdbList(self, event):
        self.comboPDB.setlist(self.mainApp.getModelsNames())
