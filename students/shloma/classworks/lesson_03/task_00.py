from typing import Any
from typing import Union


def f2(v: Union[str, int, float]) -> Union[str, int, float]:
    return v


def f1(val: Any) -> Any:
    return val


def my_fun(k: int, fl: bool, m: list[str, ...]) -> None:
    print("YES" if fl else "NO")


number: int = 44
arr: list[str, int, float, bool] = ["a", 1, 1, 1]