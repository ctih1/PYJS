import os
from collections.abc import Iterable
import time as _time

count_map: dict = {}
time_map: dict = {}

def __reset__(**kwargs) -> None:
    count_map.clear()

class console:
    def count(label: str) -> int:
        global count_map
        count_map[label] = count_map.get(label,0) + 1
        return count_map[label]
    
    def clear(**kwargs) -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        __reset__()
        
    def countReset(label: any) -> None:
        count_map[label] = 0
    
    def dir(object: object) -> dict or list:
        data: dict = {
            "length": len(object),
            "type": type(object),
            "value": str(object)
        }
        if isinstance(object,Iterable):
            i = 0
            for item in object:
                data[i] = item
                i+=1
        return data
    
    def time(label: str="default") -> None:
        global time_map
        time_map[label] = _time.time()
        
    def timeEnd(label: str="default") -> float:
        result: float = (_time.time()-time_map.get(label,_time.time()))*1000
        time_map[label] = None
        return result
    
    def timeLog(label: str="default") -> float:
        return (_time.time()-time_map.get(label,_time.time()))*1000
    
    def log(text: any="") -> None:
        print(text)
        
    def error(text: any="") -> None:
        print(f"\033[0;31m{text}\033[0m")