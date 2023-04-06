from typing import*


def stringConversion(s: str, arr: List[int]) -> int:
    r1=" "
    for i in range(len(arr)):
        t=(bin(arr[i])[2:])
        r=r+str(t)
    if r==s:
        return 1
    else:
        return 0
   









    pass
