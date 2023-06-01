colordict = {
    'BLACK': {'F': '\033[30m', 'B': '\033[40m'},
    'RED': {'F': '\033[31m', 'B': '\033[41m'},
    'GREEN': {'F': '\033[32m', 'B': '\033[42m'},
    'YELLOW': {'F': '\033[33m', 'B': '\033[43m'},
    'BLUE': {'F': '\033[34m', 'B': '\033[44m'},
    'MAGENTA': {'F': '\033[35m', 'B': '\033[45m'},
    'CYAN': {'F': '\033[36m', 'B': '\033[46m'},
    'WHITE': {'F': '\033[37m', 'B': '\033[47m'},
    'RESET': {'F': '\033[39m', 'B': '\033[49m'},
    'FULLRESET': {'\033[0m' }
}
clrs = colordict
clr_reset = colordict['RESET']['F'] + colordict['RESET']['B']

bblack = colordict['BLACK']['B']
bred   = colordict['RED']['B']
bgreen = colordict['GREEN']['B']
byellow = colordict['YELLOW']['B']
bblue = colordict['BLUE']['B']
bmagenta = colordict['MAGENTA']['B']
bcyan = colordict['CYAN']['B']
bwhite = colordict['WHITE']['B']
breset = colordict['RESET']['B']

fblack = colordict['BLACK']['F']
fred   = colordict['RED']['F']
fgreen = colordict['GREEN']['F']
fyellow = colordict['YELLOW']['F']
fblue = colordict['BLUE']['F']
fmagenta = colordict['MAGENTA']['F']
fcyan = colordict['CYAN']['F']
fwhite = colordict['WHITE']['F']
freset = colordict['RESET']['F']