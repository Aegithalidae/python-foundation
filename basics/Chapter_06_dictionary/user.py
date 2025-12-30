favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    } 

print("The following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())): 
    print(language.title() + ", is the favorite language.")

