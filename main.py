# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT STANDARD LIBRARY
import os
import sys
import argparse

from time import strftime

# IMPORT LOCAL
from key_id_maker import get_time, rand_char, make_id



# Lets Code :)
# GET PYTHON VERSION
PYTHONVERSION = sys.version_info
PY: tuple[int, int] = PYTHONVERSION.major, PYTHONVERSION.minor

# CHECK PYTHON VERSION MINIMUM VERSION 3.7
assert PY[0] > 2 and PY[1] > 6

# VERSION INFO
VERSION = 0.1
BUILD = 14
MODE = 'D'      # 'D' DEBUG - 'A' ALPHA -'B' BETA - 'F' FINAL
VERSION_INFO = f"{VERSION}.{BUILD}.{MODE}"

# CREATE DICT USE FOR ARG PARSE
APPS = {'mkid': 'make_id', 'rchr': 'rand_char', 'now': 'get_time'}
TYPETIME = {'float': get_time, 'human': lambda : strftime('%X-%x'), 'both': lambda : f"FLOAT:{get_time()}-HUMAN:{strftime('%x %X')}"}

# APP TITLE & DESCRIPTION
TITLE = "- KEY ID -"
DESCRIPTION = """
    'Make Uniq Key ID' - 'Random Choice' - 'Time Now' Exists In This Small App
    Default Set in Make ID --length '-l' 32 Use Option --app '-a' for Change It.
    """

# WRITE TO FILE
def write(_path: str, txt: str):
    _path = os.path.abspath(_path)
    try:
        with open(_path, 'w') as f:
            f.write(txt)
    except (BaseException, Exception, IOError) as err:
        raise err

# PYTHON VER < 3.10
def oex(val) -> None:
    
    if val.app == 'mkid':
        ex = [make_id(val.length, val.packsize) for _ in range(0, val.many)]
        ex = '\n'.join(ex)
    
        if val.file != None:
            write(val.file, ex)
    
        if val.display.lower() == 'n':
            ex = f"[{val.many}] ID is CREATED !"
        print(ex)
    
    elif val.app == 'rchr':
        ex = [rand_char(val.sequence) for _ in range(0, val.many)]
        ex = val.charspacer.join(ex)
        if val.file != None:
            write(val.file, ex)
        if val.display.lower() == 'n':
            ex = f"[{val.many}] RANDOM SELECTIONS !"
        print(ex)
    
    elif val.app == 'now':
        ex = TYPETIME[val.time]()
        print(ex)
    
    if val.version:
        print(VERSION_INFO)


# MAIN
def main() -> int:
    parser = argparse.ArgumentParser(TITLE, description = DESCRIPTION)
    parser.add_argument('--app', '-a', type=str, default='mkid', choices=APPS.keys())
    parser.add_argument('--display', '-d', type=str, default= 'y', choices=['y', 'n'], help="Option for Make ID & Rand Char show in display After Generating or Choosing")
    parser.add_argument('--many', '-m', type=int, default=1, help="Option for Make ID & Rand Char How Many Make or Choice")
    parser.add_argument('--length', '-l', type=int, default=32, help="Option for Make ID Means Length Generate ID")
    parser.add_argument('--packsize', '-p', type=int, default=16, help="Option for Make ID Pack Size Generating Number From How Many binarray")
    parser.add_argument('--file', '-f', type=str, default=None, help="Option for Make ID & Rand Char Result Into The File")
    parser.add_argument('--sequence', '-s', type=str, default=None, help="Option for Random Char Default is None means All 'en' Alphabet")
    parser.add_argument('--charspacer', '-c', type=str, default=' ', help="Option for Random Char Spacer if more than 1 choice")
    parser.add_argument('--time', '-t', type=str, default='human', choices=TYPETIME.keys(), help="Option for Time Return Type Time You Need")
    
    parser.add_argument('--version', '-v', action='store_true', default= False, help="App Version")

    get_args = parser.parse_args()
    
    if PY[1] >= 10:
        match get_args.app:
            
            case 'mkid':
                # Make ID Execute & Show
                ex = [make_id(get_args.length, get_args.packsize) for _ in range(0, get_args.many)]
                ex = '\n'.join(ex)
                
                if get_args.file != None:
                    write(get_args.file, ex)
               
                match get_args.display.lower():
                    case 'n':
                        ex = f"[{get_args.many}] ID is CREATED !"
                print(ex)
           
            case 'rchr':
                # Random Char Execute & Show
                ex = [rand_char(get_args.sequence) for _ in range(0, get_args.many)]
                ex = get_args.charspacer.join(ex)
                
                if get_args.file != None:
                    write(get_args.file, ex)
                
                match get_args.display.lower():
                    case 'n':
                        ex = f"[{get_args.many}] RANDOM SELECTIONS !"
                print(ex)
            
            case 'now':
                # Make ID Execute & Show
                ex = TYPETIME[get_args.time]()
                print(ex)
            
            case _:
                print("-- NOT SUPPORTED COMMAND --")
        
        match get_args.version:
            
            case True:
                print(VERSION_INFO)
    
    else:
        ex = oex(get_args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
