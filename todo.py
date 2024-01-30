go = 0
counter = 1

while go != 1:

    print ('Task: ')
    task = str(input())
    print ('Date added: ')
    added = str(input())
    print ('Date needed by: ')
    needed = str(input())
    print ('Importance: ')
    important = str(input())
    print ('Other comments: ')
    other = str(input())
    
    print ('Would you like to continue (yes - 0, no - 1)')
    go = int(input())

    stuff = {
        "Task:": task,
        "Date added:": added,
        "Date needed by:": needed,
        "Importance:": important,
        "Other comments:": other,
    }

    if counter == 1:       
        stuffnew1 = stuff.copy()
    elif counter == 2:
        stuffnew2 = stuff.copy()
    elif counter == 3:
        stuffnew3 = stuff.copy()
    elif counter == 4:
        stuffnew4 = stuff.copy()
    elif counter == 5:
        stuffnew5 = stuff.copy()
    elif counter == 6:
        stuffnew6 = stuff.copy()
    elif counter == 7:
        stuffnew8 = stuff.copy()
    else:
        print ("You have entered too many items")
        break

    counter = counter + 1


    for x, y in stuff.items():
        print(x, y)

counter = counter - 1

if counter == 1:
    print(stuffnew1)
elif counter == 2:
    print(stuffnew1)
    print(stuffnew2)
elif counter == 3:
    print(stuffnew1)
    print(stuffnew2)
    print (stuffnew3)
elif counter == 4:
    print(stuffnew1)
    print(stuffnew2)
    print (stuffnew3)
    print (stuffnew4)
elif counter == 5:
    print(stuffnew1)
    print(stuffnew2)
    print (stuffnew3)
    print(stuffnew4)
    print(stuffnew5)
elif counter == 6:
    print(stuffnew1)
    print(stuffnew2)
    print (stuffnew3)
    print(stuffnew4)
    print(stuffnew5)
    print (stuffnew6)
elif counter == 7:
    print(stuffnew1)
    print(stuffnew2)
    print (stuffnew3)
    print(stuffnew4)
    print(stuffnew5)
    print (stuffnew6)
    print (stuffnew7)
