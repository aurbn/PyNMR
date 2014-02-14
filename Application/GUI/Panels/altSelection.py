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

class ITunes(Panel):
    def __init__(self, master):
        Panel.__init__(self, master, frameText="iTunes")
        self.panelsList = []
        self.widgetCreation()
    
    def widgetCreation(self):
        rangeList = Pmw.ScrolledListBox(self)
        violationList = Pmw.ScrolledListBox(self)
        residueList = Pmw.ScrolledListBox(self)
        Tk.Label(self, text='Range').grid(row=0, column=0)
        Tk.Label(self, text='Violation').grid(row=0, column=1)
        Tk.Label(self, text='Residue').grid(row=0, column=2)
        rangeList.grid(row=1, column=0)
        violationList.grid(row=1, column=1)
        residueList.grid(row=1, column=2)
        