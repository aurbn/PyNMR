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

import Pmw

from Panel import Panel


class NOEDrawingPanel(Panel):
    def __init__(self, master):
        Panel.__init__(self, master, frameText="NOE Representation")
        self.widgetCreation()
        self.mainApp = ""  #Must be set at run time
        self.NMRCommands = ""  #Must be set by application at run time

    def widgetCreation(self):
        self.drawingNOEButtonBox = Pmw.ButtonBox(self, orient='horizontal')
        self.drawingNOEButtonBox.add('Sticks', command=self.showSticks)
        self.drawingNOEButtonBox.add('Density', command=self.showDensity)
        self.drawingNOEButtonBox.add('Clean NOEs', command=self.cleanAll)
        self.drawingNOEButtonBox.grid(row=0, column=0)
        self.drawingNOEButtonBox.setdefault('Sticks')

    def showSticks(self):
        infos = self.mainApp.getInfo()
        infoCheck = 1

        if self.infoCheck(infos):
            self.NMRCommands.commandsInterpretation(infos["pdb"], infos["constraintFile"], infos["ranges"], infos["residuesRange"], infos["violationState"], infos["cutOff"], infos["method"])
            self.NMRCommands.showSticks(infos["constraintFile"], infos["pdb"], infos["colors"], infos["radius"])

    def showDensity(self):
        infos = self.mainApp.getInfo()

        if self.infoCheck(infos):
            self.NMRCommands.commandsInterpretation(infos["pdb"], infos["constraintFile"], infos["ranges"], infos["residuesRange"], infos["violationState"], infos["cutOff"], infos["method"])
            self.NMRCommands.showNOEDensity(infos["constraintFile"], infos["pdb"], infos["gradient"])

    def cleanAll(self):
        infos = self.mainApp.getInfo()

        if self.infoCheck(infos):
            self.NMRCommands.cleanScreen(infos["constraintFile"])

    def infoCheck(self, infos):
        check = 1
        for item in infos:
            if infos[item] == "":
                check = 0
                break
        return check
