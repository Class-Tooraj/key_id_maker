# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT STANDARD LIB
import time
import random

# IMPORT TYPE
from typing import Iterable, Union, Generator


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #


# GIVE ME A TIME
def get_time() -> time.time:
    """[Get Now Time Use 'time.time()']

    Returns:
        time.time: [Now]
    """
    return time.time()


# RANDOM 
def rand_char(letters: Iterable[str] = None) -> chr:
    """[Random Choice Char From Letter Sequence if None Use UpperCase & LowerCase Alphabet]

    Args:
        letters (Iterable[str], optional): [Letter Sequence For Choice]. Defaults to None.

    Returns:
        chr: [Random Choice Returned]
    """
    letters = letters or "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return random.choice(letters)


# CUSTOMIZE BINARY
def custom_bin(value: Union[str, int]) -> str:
    if isinstance(value, str):
        try:
            value = int(value)
        except (BaseException, Exception) as err:
            raise err

    assert isinstance(value, int)
    
    return bin(value).removeprefix('0b')


# VALIDATE TO PACK SIZE
def packing(value: str, ped_size: int = 16, str_ret: bool = False) -> Generator[Union[int, str], None, None]:
    _dec = [*value]
    _active = True
    _resval = lambda x: str(int(x, 2)) if str_ret else int(x, 2)
    while _active:
        _ped = ""
        
        if len(_dec) >= ped_size:

            for _ in range(0, ped_size):
                _ped += _dec.pop(0)
            yield _resval(_ped)
        
        elif 0 < len(_dec) < ped_size:
            _ped = "".join(_dec)
            _dec.clear()
            yield _resval(_ped)
        
        else:
            _active = False
            break
    
    return None


# START PROGRAM TIME
STARTS: time.time = get_time()


# PROCESSING
def process_chars(pack_size: int = 16) -> Iterable[str]:
    _mul = lambda x,y: int(x) * int(y)
    _add = lambda x,y: int(x) + int(y)
    _rec = f"{get_time()}.{STARTS}.{get_time()}".split('.')
    _bins = ''.join((custom_bin(i) for i in _rec))
    _revbins = reversed(_bins)
    _pack_one = packing(_bins, pack_size, True)
    _pack_tow = packing(_revbins, pack_size, True)
    _insertletter = (
        f"{rand_char()}{_add(o,t)}{rand_char()}{o}{rand_char()}{t}{rand_char()}{_mul(o,t)}{rand_char()}"
        for o,t in zip(_pack_one, _pack_tow)
        )
    return _insertletter


# MAKE NEW ID
def make_id(length: int = 32, pack_size: int = 16) -> str:
    """[Make Key ID]

    Args:
        length (int, optional): [Key ID Length]. Defaults to 32.
        pack_size (int, optional): [Ped Intiger Size]. Defaults to 16.

    Returns:
        str: [Generated Key ID]
    """
    _choice = lambda x: rand_char(x)
    _pr = ''.join(process_chars(pack_size))
    _in_size = [_choice(_pr) for _ in range(0, length)]
    return ''.join(_in_size)



__dir__ = ("get_time", "rand_char", "make_id", )


if __name__ == "__main__":
    from test_base import test
    print("... MAKE ID TEST IS READY FOR START ...")
    inp = str(input("/ START TEST ? [Y/N]: ")).lower()
    match inp:
        case 'y':
            ver = str(input('VERBOSE ? [Y/N]: ')).lower()
            ver = True if ver == 'y' else False
            t = test(ver)
            print(f"ALL: {all(t.values())}\tANY: {any(t.values())}\nPACKED: {t}")
            exit()
        case _:
            exit()
