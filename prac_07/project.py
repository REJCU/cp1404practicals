"""
Estimate: 2 hours
Actual:  1  hours
"""
COMPLETED_PROJECT = 100

class Project:


    def __init__(self,name='', start_date = 0, priority = 0, cost_estimate = 0, completion_percentage = 0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name} {self.start_date} {self.priority} {self.cost_estimate} {self.completion_percentage}"

    # def __lt__(self, other):
    #     return self.completion_percentage < other.completion_percentage

    def is_complete(self):
        return  self.completion_percentage == "100"



