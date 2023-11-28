import tkinter as tk
from tkinter import ttk

# Data classes

class Query():
    def __init__(self, date_start=None, date_end=None, keywords=None):
        self.date_start = date_start
        self.date_end = date_end
        self.keywords = keywords
        
    def query_test(self):
        print(f'Start Date: {self.date_start}')
        print(f'End Date: {self.date_end}')
        print(f'Keywords : {self.keywords}')    
        
    def query_clear_data(self):
        self.date_start = None
        self.date_end = None
        self.keywords = None
        
class Results():
    pass


# Main App Class

class App(tk.Tk):
    # Initialize query object
    query_obj = Query()
    
    def __init__(self, title, size):
        
        # Main app setup
        super().__init__()
        self.title(title)
        self.geomtery=(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])        
        
        # Add sub frames
        self.side_frame = SideFrame(self)
        self.view_frame = ViewFrame(self)
        self.info_frame = InfoFrame(self)
        
        # run main loop
        self.mainloop()
    
  
# GUI element classes  
        
class SideFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = ttk.Label(self, text='', background='red', anchor='n')
        label.pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=0.2, relheight=1)
        
        SearchFrame(self)
        ResultsFrame(self)
        

class ViewFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = ttk.Label(self, text='Results View', background='green')
        label.pack()
        self.place(relx=0.2, y=0, relwidth=0.8, relheight=.6)


class InfoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # info_title_label = ttk.Label(self, text='info view label')
        # info_title_label.pack()
        
        info_box_label = ttk.Label(self, text='info view label', background='blue')
        info_box_label.place(rely=0.5, relx=0.5, relwidth=0.95, relheight=0.95, anchor='center')
        
        self.config(borderwidth=2, relief='sunken')
        self.place(relx=0.2, rely=0.6, relwidth=0.8, relheight=.4)

        
class SearchFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Frame Label
        title_label = ttk.Label(self, text='Search', background='orange')
        title_label.pack()
        
        # Set up start date widgets
        date_start_label = ttk.Label(self, text='Date Start:')
        date_start_label.place(relwidth=.5, rely=.15)
        
        date_start_entry = ttk.Entry(self, width=10)
        date_start_entry.place(rely=.15, relx=.35)
        
        # Set up end date widgets
        date_end_label = ttk.Label(self, text='Date End:')
        date_end_label.place(relwidth=.5, rely=0.25)
        
        date_end_entry = ttk.Entry(self, width=10)
        date_end_entry.place(rely=0.25, relx=0.35)
        
        # Set up keyword widgets
        keyword_search_label = ttk.Label(self, text='Keywords:')
        keyword_search_label.place(relwidth=.55, rely=.35)
        
        key_word_text = tk.Text(self, width=20, height=3)
        key_word_text.place(relwidth=0.9, relx=.5, rely=.57, anchor='center')
        
        # Set up Search button
        search_button = ttk.Button(self, 
                                   text='Go', 
                                   command=(lambda:start_search(
                                                    date_start_entry.get(),
                                                    date_end_entry.get(),
                                                    key_word_text.get('1.0', 'end'))
                                       )
                                   )
        search_button.place(relwidth=.75, rely=.8, relx=.5, anchor='center')
        
        # Place search frame
        self.place(relx=0.5, rely=0.25, relheight=0.4, relwidth=0.9, anchor='center')
        

class ResultsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        title_label = ttk.Label(self, text='Results', background='orange')
        title_label.pack()
        
        results_label = ttk.Label(self, text='Results:')
        results_label.place(relwidth=.5, rely=.15)
        
        results_data_label = ttk.Label(self, text='XXX items')
        results_data_label.place(rely=.15, relx=.35)
        
        keyword_search_label = ttk.Label(self, text='Keywords:')
        keyword_search_label.place(relwidth=.55, rely=.35)
        
        key_word_entry = tk.Text(self, width=20, height=3)
        key_word_entry.place(relwidth=0.9, relx=.5, rely=.57, anchor='center')

        
        self.place(relx=0.5, rely=0.75, relheight=0.4, relwidth=0.9, anchor='center')

        
        
# GUI callback functions

def start_search(start_date_text=None, end_date_text=None, keywords=None):
    
    # Construct query object 
    App.query_obj.date_start = start_date_text
    App.query_obj.date_end = end_date_text
    App.query_obj.keywords = keywords.replace(' ', '').replace('\n', '').lower().split(',')
    
    # Send query object and results object to database seach functions
    
    # Populate results and view frames with results
    
        
        
        
        
 # Main application       
        
App('Context', (960,540))