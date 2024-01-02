"""
A gedit plugin which adds a Label to the status bar with the active documents 
wordcount, where a word is definied as r"[a-zA-Z0-9]+[a-zA-Z0-9\-']*\s?"
"""

import re
from gi.repository import GObject, Gtk, Gedit # pylint: disable=E0611

WORD_RE = re.compile(r"\w+\w*\s?", re.UNICODE)

def get_text(doc):
    """Return the full text of the document"""
    if doc.get_has_selection():
        start, end = doc.get_selection_bounds()
    else:
        start, end = doc.get_bounds()
    return doc.get_text(start, end, False)
    

class WordcountPlugin(GObject.Object, Gedit.WindowActivatable):
    """
    Adds a Label to the status bar with the active documents wordcount, 
    where a word is definied as r"[a-zA-Z0-9]+[a-zA-Z0-9\-']*\s?"
    """
    __gtype_name__ = "wordcount"
    window = GObject.property(type=Gedit.Window)
    
    def __init__(self):
        GObject.Object.__init__(self)
        self._doc_changed_id = None
        self._label = Gtk.Label()
    
    def do_activate(self):
        """called when plugin is activated"""
        self.window.get_statusbar().pack_end(self._label, False, False, 5)
        self._label.show()
    
    def do_deactivate(self):
        """called when plugin is deactivated, cleanup"""
        Gtk.Container.remove(self.window.get_statusbar(), self._label)
        if self._doc_changed_id:
            self._doc_changed_id[0].disconnect(self._doc_changed_id[1])
        del self._label
    
    def do_update_state(self):
        """state requires update"""
        if self._doc_changed_id:
            self._doc_changed_id[0].disconnect(self._doc_changed_id[1])
        doc = self.window.get_active_document()
        if doc:
            self._doc_changed_id = (doc, 
                doc.connect("cursor-moved", self.on_document_changed))
            self.update_label(doc)
        else: # user closed all tabs
            self._label.set_text('')
    
    def on_document_changed(self, doc):
        """active documents content has changed"""
        self.update_label(doc)
        
    def update_label(self, doc):
        """update the plugins status bar label"""
        txt = get_text(doc)
        ln = txt.count('\n')+1 if len(txt)!=0 else 0
        msg = f'Lines: {ln}, Words: {len(WORD_RE.findall(txt))}, Characters: {len(txt)}'
        self._label.set_text(msg)
