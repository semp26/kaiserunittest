
def shiftyeartester(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                print("Jahr: " + str(year) +" ist ein Schaltjahr")
                return True
            else:
                print("Jahr: " + str(year) +" ist kein Schaltjahr")
                return False
        else:
            print("Jahr: " + str(year) +" ist ein Schaltjahr")
            return True
    else:
        print("Jahr: " + str(year) +" ist kein Schaltjahr")
        return False