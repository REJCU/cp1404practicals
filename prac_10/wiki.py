import wikipedia

# a = wikipedia.search('')
#
# print(a)

def wiki_search():
    user_search = input("Enter page title: ")
    while user_search != "":
        try:
            result = wikipedia.WikipediaPage(user_search)
            print(f"{user_search}\nSummary:\n{result.summary}\n{result.pageid}")
            user_search = input("search: ")
        except wikipedia.exceptions.DisambiguationError as error:
            print(f"We need a more specific title. Try one of the following, or a new search:\n{error.options}")
            user_search = input("search: ")
    print("Thank You")

wiki_search()

