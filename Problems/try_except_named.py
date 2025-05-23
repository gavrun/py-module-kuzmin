###
try:
    raise TypeError('Oh no!')
except Exception as e:
    if type(e) is ValueError:
        print('Oh no, a value error!')
    elif type(e) is TypeError:
        print('Oh no, a type error!')

###
try:
    raise TypeError('Oh no!')
except Exception as e:
    if type(e) is ValueError:
        print('Oh no, a value error!')
    elif type(e) is TypeError:
        print('Oh no, a type error!')
    else:
        raise e

###
try:
    raise TypeError('Oh no!')
except ValueError:
    print('Oh no, a value error!')
except TypeError:
    print('Oh no, a type error!')
except Exception as e:
    print('Oh, must be something else')
