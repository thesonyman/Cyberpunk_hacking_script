import random, time, math
w = ("scale", "catsha", "matrix", "obedo", "kylersecureity", "meshumoto")

s = len(raw_input("Who are you hacking? \n")) #based on length determends security level


if s >= 2:
    l = random.choice(w)
    o = 0
    while o < 10:
        o = o + 1
        sec = random.randint(0, 5)
        o = o + 1

    print("You have encounted a firewall")
    print("The name of it is ") + l
    print("its secureity level is level %s" %sec)
    z = raw_input("Continue hack Y/N?")
    if z == "y":
        o = 0
        while o > 10:
            print ("Hacking")
            time.sleep(.2)
            print ("...")
        r = random.randint(1, 20)
        if r >= 20:
            print ("success")
            print("search for data?")
            c= raw_input("what are you searching for? \n")
            o = 0
            while o < 100:
                o = o + 1
                x = random.randint(1, 100)
            if x >= 60:
                print("You retreaved ") + c
                print("success")

            else:
                print("There was nothing")

        else:
            trys = 0
            if sec == 5:
                trys = 3
            elif sec == 4:
                trys = 4
            elif trys == 3:
                trys = 5
            elif sec == 2:
                trys = 7
            elif sec == 1:
                trys = 8
            elif sec == 0:
                trys = 10

            print("manual hack required")
            print("guess the number between 1 and 10")
            print("you have %s trys before the system kicks you out because of the security level" %trys)
            p = 0

            num = random.randint(1, 10)

            while p < trys:
                num1 = int(raw_input("guess \n"))
                p = p + 1
                if num1 == num:

                    print("sucess")
                    print("search for data?")
                    c= raw_input("what are you searching for? \n")
                    o = 0
                    while o < 100:
                        o = o + 1
                        x = random.randint(1, 100)
                    if x >= 60:
                        print("You retreaved ") + c
                        print("success")
                        break
                    else:
                        print("There was nothing")
                        break
else:
    print("there isnt a firewall")
    print("search for data?")
    c= raw_input("what are you searching for? \n")
    o = 0
    while o < 100:
        o = o + 1
        x = random.randint(1, 100)
    if x >= 60:
        print("You retreaved ") + c
        print("success")
    else:
        print("there was nothing")
