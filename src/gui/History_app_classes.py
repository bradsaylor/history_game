class Date:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def duration(self):
        return self.end - self.start

class Event:
    event_list = []
    
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.keywords = []
        self.description = ''
        Event.event_list.append(self)
        
    def add_keywords(self, *args):
        for item in args:
            self.keywords.append(item.lower())
            
    def add_descrip(self, description):
        self.description = description
        
class Period:
    event_list = []
    
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        
    def collect_events(self):
        pass

class EventQuery():
    def __init__(self, dates, *keywords):
        self.dates = dates
        self.result_list = []
        self.keywords = []
        for item in keywords:
            self.keywords.append(item.lower())
            
    def get_result_list(self):
        for item in Event.event_list:
            if (item.date.start > self.dates.start and 
                item.date.end < self.dates.end):
                found_item_flag = True
                for kw in self.keywords:
                    if kw not in set(item.keywords):
                        found_item_flag = False
                        break
                if found_item_flag: self.result_list.append(item)
        return self.result_list