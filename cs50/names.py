import sys

names = ["bill", "charlie", "fred", "george", "jane", "joe", "mary", "sue"  ]

name = input("Name: ")

if name in names:
        print("Name found!")
        sys.exit(0)

print("Name not found!")
sys.exit(1)