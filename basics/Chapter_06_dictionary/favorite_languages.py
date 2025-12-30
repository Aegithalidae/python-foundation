favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in sorted(favorite_languages.items()):
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"- {language.title()}")
    else:
        print(f"{name.title()}'s favorite language is:")
        print(f"- {language.title()}")
    print()