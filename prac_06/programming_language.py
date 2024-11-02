"""
programming_languages
Estimate: 60 minutes
Actual:    minutes
"""
from languages import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print(python.is_dynamic())

programming_languages = python, ruby, visual_basic


print(programming_languages)
for language in programming_languages:
    if language.is_dynamic():
        print(language.field)