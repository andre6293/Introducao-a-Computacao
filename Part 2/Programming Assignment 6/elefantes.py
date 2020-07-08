def incomodam(n):
    return '' if n <= 0 else 'incomodam ' + incomodam(n - 1)


def elefantes(n):
    if n == 1:
        return 'Um elefante incomoda muita gente\n'
    elif n <= 0:
        return ''
    else:
        return (
            elefantes(n - 1) + "{} elefantes ".format(n) + incomodam(n) +
            "muito mais\n" + "{} elefantes incomodam muita gente\n".format(n))
