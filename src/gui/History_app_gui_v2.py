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
        self.grid_columnconfigure(0, weight=1)
        
        main_frame = ttk.Frame(self, padding='3 3 12 12') 
        main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        main_frame.grid_columnconfigure(1, weight=1)
        
        # Add sub frames
        self.side_frame = SideFrame(main_frame)
        self.view_frame = ViewFrame(main_frame)
        self.info_frame = InfoFrame(main_frame)
        
        # run main loop
        self.mainloop()
    
  
# GUI element classes  
        
class SideFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Side frame config and placement.  
        # Want all extra space at bottom hence the grid_config's
        self.configure(borderwidth=3, relief='sunken')
        self.grid(row=0, rowspan=2, column=0, 
                  sticky=(tk.N, tk.S, tk.E, tk.W))
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add Search and Results frames to side frame    
        SearchFrame(self)
        ResultsFrame(self)
        

class ViewFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # View frame config and placement.  
        # Want the single column to fill entire cell hence the grid_config
        self.configure(borderwidth=3, relief='sunken')
        self.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.grid_columnconfigure(0, weight=1)
        
        # View frame label
        label = ttk.Label(self, text='Results View', 
                          background='green', anchor='center')
        label.grid(column=0, row=0, sticky=(tk.E, tk.W))
        
        # Results view frame.  
        # Style needed b/c ttk.Frame has no 'background' parameter
        s = ttk.Style()
        s.configure('View.TFrame', background='blue')
        view_sub_frame = ttk.Frame(self, width=500, 
                                   height=300, style='View.TFrame')
        view_sub_frame.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        


class InfoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.config(borderwidth=2, relief='sunken')
        self.grid(column=1, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.grid_columnconfigure(0, weight=1)
        
        info_box_label = ttk.Label(self, text='Info View', 
                                   background='green', anchor='center')
        info_box_label.grid(column=0, row=0, sticky=(tk.E, tk.W))
        
        text_box = tk.Text(self, width=80, height=12)
        text_box.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        
        
class SearchFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Frame Label
        title_label = ttk.Label(self, text='Search', background='orange')
        title_label.grid(column=0, row=0, columnspan=3, sticky=(tk.E, tk.W))
        
        # Set up start date widgets
        date_start_label = ttk.Label(self, text='Date Start:')
        date_start_label.grid(column=0, row=1, sticky=(tk.W), pady=10)
        
        date_start_entry = ttk.Entry(self, width=15)
        date_start_entry.grid(column=1, row=1, columnspan=2, 
                              sticky=(tk.W), padx=10)
        
        # Set up end date widgets
        date_end_label = ttk.Label(self, text='Date End:')
        date_end_label.grid(column=0, row=2, sticky=(tk.W), pady=5)
        
        date_end_entry = ttk.Entry(self, width=15)
        date_end_entry.grid(column=1, row=2, columnspan=2, 
                            sticky=(tk.W), padx=10)
        
        # Set up keyword widgets
        keyword_search_label = ttk.Label(self, text='Keywords:')
        keyword_search_label.grid(column=0, row=3, sticky=(tk.W), pady=10)
        
        key_word_text = tk.Text(self, width=20, height=6)
        key_word_text.grid(column=0, row=4, columnspan=3)
        
        # Set up Search button
        search_button = ttk.Button(self, 
                                   text='Go', 
                                   command=
                                   (lambda:start_search(
                                        date_start_entry.get(),
                                        date_end_entry.get(),
                                        key_word_text.get('1.0', 'end'))))

        search_button.grid(column=0, row=5, pady=10)
        
        # Place search frame
        self.configure(borderwidth=3, relief='groove')
        self.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        

class ResultsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        title_label = ttk.Label(self, text='Results', background='orange')
        title_label.grid(column=0, row=0, columnspan=3, sticky=(tk.E, tk.W))
        
        results_label = ttk.Label(self, text='Results:')
        results_label.grid(column=0, row=1, sticky=tk.W, pady=10)
        
        results_data_label = ttk.Label(self, text='XXX items')
        results_data_label.grid(column=1, row=1, sticky=tk.W)
        
        keyword_search_label = ttk.Label(self, text='Keywords:')
        keyword_search_label.grid(column=0, row=2, sticky=tk.W)
        
        key_word_entry = tk.Text(self, width=20, height=6)
        key_word_entry.grid(column=0, row=3, columnspan=3, pady=10)

        self.configure(borderwidth=3, relief='groove')
        self.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        
        
# GUI callback functions

def start_search(start_date_text=None, end_date_text=None, keywords=None):
    
    # Construct query object 
    App.query_obj.date_start = start_date_text
    App.query_obj.date_end = end_date_text
    App.query_obj.keywords = \
        keywords.replace(' ', '').replace('\n', '').lower().split(',')
    
    App.query_obj.query_test()
    
    # Send query object and results object to database seach functions
    
    # Populate results and view frames with results
    
        
        
        
        
# Main application       
        
App('Context', (960,540))