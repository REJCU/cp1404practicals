class ProgrammingLanguage:
    """ Represent programming language as an object """

    def __init__(self,field='', typing='', reflection=True or False, year=0):
        """
        Initialise the instance
        :param typing:
        :param reflection:
        :param year:
        """
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"ProgrammingLanguage: {self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"