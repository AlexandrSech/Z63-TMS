# 2021-12-21

import requests
import json

url = "https://randomuser.me/api/"


def printer(data, tabs="    ", col_tabs=0):
    if type(data) in [list, tuple, set]:
        print(tabs * (col_tabs - 1)+ "[")
        for item in data:
            printer(item, col_tabs=col_tabs + 1)
        print(tabs * (col_tabs - 1) + "]")
    elif type(data) == dict:
        print(tabs * (col_tabs - 1) + "{")
        for k, v in data.items():
            print(f"{tabs * col_tabs}'{k}': ", end="")
            printer(v, col_tabs=col_tabs + 1)
        print(tabs * (col_tabs - 1) + "}")
    else:
        print(tabs * col_tabs + str(data))

    # for k, v in _json.items():
    #     print(f"'{k}': ")
    #     if type(v) in [list, tuple, set]:
    #         for item in v:
    #             print(" "*4 + str(item))
    #     elif type(v) is dict:
    #         for _k, _v in v.items():
    #             print(f"{' '*4}'{_k}': '{_v}'")
    #     else:
    #         print(" "*4 + str(v))


if __name__ == "__main__":
    r = requests.get(url)
    dd = json.loads(r.text)

    printer(dd)
