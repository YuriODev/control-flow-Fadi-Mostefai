# Your solution to Exercise 18

def greet():
    name = input("")
    if name == "yes":
        ex = input("")
        if ex == "yes":
            drunk = input("")
            if drunk == "yes":
                rekindle = input("")
                if rekindle == "yes":
                    return "Say hi."
                else:
                    return "Don't say hi."
            else:
                convertible = input("")
                if convertible == "yes":
                    return "Say hi."
                else:
                    return "Don't say hi."
        else:
            friend_ex = input("")
            if friend_ex == "yes":
                return "Don't say hi."
            else:
                enemy = input("")
                if enemy == "yes":
                    convertible = input("")
                    if convertible == "yes":
                        return "Say hi."
                    else:
                        return "Don't say hi."
                else:
                    rob = input("")
                    if rob == "yes":
                        return "Don't say hi."
                    else:
                        bathrobe = input("")
                        if bathrobe == "yes":
                            return "Don't say hi."
                        else:
                            return "Say hi."
    else:
        time = input("")
        if time == "yes":
            return "Run for it."
        else:
            pretend = input("")
            if pretend == "yes":
                return "Hello, doctor. What are my test results?"
            else:
                sunglasses = input("")
                if sunglasses == "yes":
                    return "Keep walking."
                else:
                    return "Address the person using an amusing nickname such as 'Sarge' or 'Slugger' or 'Master Blaster'"
                

print(greet())
