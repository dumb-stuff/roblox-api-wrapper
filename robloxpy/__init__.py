modulelist = ['accountinformation']
def __check(name):
    if name in modulelist:
        return f"That module exist you may do\nfrom robloxpy import {name}"
    else:
        return f"That module doesn't exist please try again"

def __getattr__(name):
    raise AttributeError(f"Uh excuse me? This is dummy file please don't don't import module. instead import from file like\nfrom robloxpy import errors\netc..\n{__check(name)}") from None