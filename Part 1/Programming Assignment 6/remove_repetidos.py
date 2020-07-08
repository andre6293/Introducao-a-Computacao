# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def remove_repetidos(ar):
    ar = list(set(ar))
    ar.sort()
    return ar