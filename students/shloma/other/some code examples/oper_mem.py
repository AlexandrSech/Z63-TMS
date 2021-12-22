"""
dgfjdf
"""

import io
import json
from zipfile import ZipFile


# with ZipFile("1.zip", 'w') as file:
#     with open("1.json", 'w') as js:
#         json.dump({"a": "1", "b": "2"}, js)
#         js.seek(0)
#         file.write("1.json")


buf = io.BytesIO()

with ZipFile(buf, 'w') as file:
    with io.BytesIO() as json_buf:
        data = json.dumps({"a": "1", "b": "2"})
        json_buf.write(data.encode())
        json_buf.seek(0)
        file.writestr("1.json", json_buf.read())

with open("1.zip", "wb") as file:
    buf.seek(0)
    file.write(buf.read())