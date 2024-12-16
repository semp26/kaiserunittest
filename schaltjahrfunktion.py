
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
    
def test_low():
    assert shiftyeartester(40) == True

def test_lowfalse():
    assert shiftyeartester(41) == False

def test_high():
    assert shiftyeartester(2000) == True

def test_highfalse():
    assert shiftyeartester(2001) == False

def test_notdiv400():
    assert shiftyeartester(1900) == False