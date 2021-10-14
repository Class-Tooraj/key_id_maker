# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

# IMPORT LOCAL
from base import make_id

# IMPORT TYPING
from typing import Iterable


# TEST PACKET
def make_test_pack(weight: int = 64, length: int = 4, ped_size: int = 4) -> Iterable[tuple[str, str]]:
        _l1 = (make_id(length, ped_size) for _ in range(weight))
        _l2 = (make_id(length, ped_size) for _ in range(weight))
        return zip(_l1, _l2)


# TEST ALL IS NOT SAME
def check(value: Iterable[tuple[str, str]]) -> bool:
    _list = [p1 != p2 for p1, p2 in value]
    return all(_list)


def test(verbose: bool = False) -> dict[str, bool]:
    _tell = lambda x: print(x, flush=True) if verbose else None
    _test = {}
    _value = {
        'T1': (64, 4, 4),
        'T2': (64, 10, 4),
        'T3': (64, 30, 4),
        'T4': (64, 4, 8),
        'T5': (64, 10, 10),
        'T6': (64, 30, 16),
        'T7': (64, 64, 20),
        'T8': (64, 64, 4),
        'T9': (64, 64, 2),
        'T10': (64, 64, 32),
    }
    _tell("\n... STARTING TESTS - 10 TEST is AVALABEL - ...\n")
    for k,v in _value.items():
        _tell(f"TEST {k} VALUE {v}")
        val = make_test_pack(*v)
        _test[k] = check(val)
        _tell(f"RESULT -> {_test[k]}\n")
    _tell("... TEST IS DONE - FINISHED - ...\n")
    return _test

if __name__ == "__main__":
    print("MAKE KEY ID :: FUNCTION <make_id> FROM <base> :: TEST STARTS")
    t = test(True)
    print(f"ALL: {all(t.values())}\tANY: {any(t.values())}\nPACKED: {t}")