"""Write a program to find how many times substring “Emma” appears in the given string."""
def substring_count(string):
    count = string.count("Emma")
    print("Emma has appeared {} times".format(count))
substring_count("Emma is good developer. Emma is a writer")
