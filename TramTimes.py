# Next Tram to the Shop
# By Peter

import time

tup1 = ('17:42', '17:50', '17:59', '18:08', '18:16', '18:23', '18:31', '18:38', '18:46', '18:53', '19:01', '19:08', '19:16',
        '19:23', '19:29', '19:37', '19:47', '19:57', '20:07', '20:17', '20:27', '20:37', '20:47', '20:57', '21:07', '21:17', '22:50')

tup2 = ('17:40', '17:48', '17:57', '18:06', '18:14', '18:21', '18:29', '18:36', '18:44', '18:51', '18:59', '19:06', '19:14',
        '19:21', '19:27', '19:35', '19:45', '19:55', '20:05', '20:15', '20:25', '20:35', '20:45', '20:55', '21:05', '21:15')


def shoppingtrip():
    localtime = time.strftime('%H:%M')
    print("The time is:", localtime)
    c1 = input("Do you want to see the next trams to leave for the shops? Enter Yes to continue: ")
    if c1 == "Yes":
        for tramtime in tup1:
            if tramtime > localtime:
                print("Tram there time:", tramtime)
    print("And the trams back are:")
    for tramback in tup2:
        if tramback > localtime:
            print("Return Tram time: ", tramback)


shoppingtrip()

input("Press enter to exit")
