def fact(n):
    if n < 0:
        raise ValueError
    try:
        product = 1
        for i in range(1, n+1):
            product *= i
    except TypeError:
        print "I cannot process this input"
    except:
        print "I can't do this"
    else:
        print "pls w8..."
        return product
    finally:
        print "yeah it's done."

print fact("a")