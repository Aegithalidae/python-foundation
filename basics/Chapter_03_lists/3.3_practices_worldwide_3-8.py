trip_want = ["Japan", "Italy", "New Zealand", "Switzerland", "Canada"]
print("Original list:")
print(trip_want)

print("\nSorted list (temporarily):")
print(sorted(trip_want))

print("\nOriginal list unchanged:")
print(trip_want)

print("\nReversed list (temporarily):")
print(sorted(trip_want, reverse = True))

print("\nOriginal list unchanged:")
print(trip_want)

trip_want.reverse()
print("\nList after reversing:")
print(trip_want)

trip_want.reverse()
print("\nList after reversing again to original:")
print(trip_want)

trip_want.sort()
print("\nList after sorting permanently:")
print(trip_want)

trip_want.sort(reverse = True)
print("\nList after sorting permanently in reverse order:")
print(trip_want)

print(trip_want)