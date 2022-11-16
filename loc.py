
class locale: 
        def __init__(self,name, summary, details, was_visited = False):
            self.name = name
            self.summary = summary
            self.details = details
            self.was_visited = was_visited
        def __str__(self):
            if self.was_visited == True:
                been = "You are at" + self.name
            elif self.was_visited == False:
                self.was_visited == True
                been = self.summary
                return been


    