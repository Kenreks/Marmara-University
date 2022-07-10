# Given n>=0, prints n!
# If n<0, raises ValueError
def fact(n):
    if n < 0:
        raise ValueError
    try:
        product = 1
        for i in range(1, n+1):
            product *= i
    except TypeError:
        print 'I cannot process this input.'
    except:
        print 'I really did not expect this error'
    else:
        # else is rarely needed in practice
        # this code could safely be moved to try block in this case
        print 'returning...'
        return product
    finally:
        print 'I am done. This is executed always!'


print fact(4), '\n'

print fact('a')

try:
    print fact(-4)
except ValueError:
    print "Raised by the function, caught by the caller"
