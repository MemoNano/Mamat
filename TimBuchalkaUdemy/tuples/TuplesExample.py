class TuplesExample:
    pass

    """Create a Tuples: We can create tuples in two different way
     Using parenthesis or without parenthesis"""

    # Tuples are immutable: Once you created you created you can't change it's content:

    t = "a", 'b', "c"
    t2 = ("a", "b", "c")
    print(t)  # Printing out tuple
    print(t2)  # Printing out tuple t2

    print(("a", "b", "c", "d"))  # Printing Tuple
    print('a', 'b', 'c', 'd', 'e')  # It's just printing a, b, c, d, e

    welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
    bad = "Bad Company" "Bad Company", 1974
    budgie = "Nightflight", "Budgie", 1981
    imelda = "More Mayhem", "Emilda May", 2011
    metallica = "Ride the Lightnigh", "Metallica", 1984, (
        (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
    print(metallica)

    print("***** This is how tuple comes handy ********")
    title, artist, year, tracks = metallica
    print(title)
    print(artist)
    print(year)
    print(tracks)
    # print(metallica)
    print(metallica[0])
    print(metallica[1])
    print(metallica[2])

    # metallica[0] = "Master of puppets"  // We can't change tuple completely
    # print(metallica)

    imelda = imelda[0], "Imelda May", imelda[2]
    print(imelda)

    """"
    Given the tuple below that represents the Imelda May album "More Mayhem", write
    code to print the album details, followed by a listing of all the tracks in the album.
    
    Indent the tracks by a single tab stop when printing them ( remember that you can pass 
    more than one item to the print function, separating them with a comma).
    
    """

    borbiev = "Bek Borbiev", "Aida taxi aida", 1988, (
        (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

    for i in borbiev:
        print("\n {} \t".format(i))
    print("\n*************  Tim Buchalka's way of printing  ********************")
    print(borbiev)

    title, artist, year, tracks = borbiev
    print(title)
    print(artist)
    print(year)
    for song in tracks:
        track, title = song
        print("\t Track number: {}, Title: {}".format(track, title))

    """
    Tuple's are immutable and content can't be change.
        But, if Tuple contains list , List content can be changed which is in the Tuple.
        
    """

    bek = "Bek Borbiev", "Aida taxi aida", 1988, (
        [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
    )
    # Here we are, How we can change the List content which is in the Tuple.
    bek[3].append((5, "All For You"))
    bek[3].append((6, "Eternity"))
    title, artist, year, tracks = bek
    print(title)
    print(artist)
    print(year)

    for song in tracks:
        track, title = song
        print("\tTrack number {}, Title: {}".format(track, title))

    """
    What will be the output of the following program?
    """

    cast = ["Clees", "Idle", "Gilliam", "Jones", "Plain", "Chapman"]
    print(cast)
    cast.sort()
    print(cast)
    print(sorted(cast))
    cast.sort()
    print(cast)

    str2 = 'Your Coupon value $10 is applied towards your order'
    balance = '$10.00'

    balance = balance.split(".")
    print(balance[0])

    """  This is how works when converting to int() """
    # balance = int(float(balance))
    # print(balance)
    # str1 = str(balance)
    # if str1 in str2:
    #     print(str1 + "-->  " + str2)

    tup = ('physics', 'chemistry', 1997, 2000)
    print(tup)
    del tup
    print("After deleting tup: ")
    print(tup)

    T = ("C++", "Java", "Python")
    print(len(T[1:]))
