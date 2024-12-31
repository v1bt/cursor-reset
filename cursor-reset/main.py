import os
import json
import uuid
import sys
from pathlib import Path

platform = sys.platform
if platform == 'win32':
    path = Path.home()/'AppData'/'Roaming'/'Cursor'/'User'/'globalStorage'
elif platform == 'darwin':
    path = Path.home()/'Library'/'Application Support'/'Cursor'/'User'/'globalStorage'
elif platform == 'linux':
    path = Path.home()/'.config'/'Cursor'/'User'/'globalStorage'
else:
    print('Unsupported os')
    print("\nPress Enter to exit...")
    input()

path = str(path/'storage.json')
print(f"File path: {path}")

if not os.path.exists(path):
    print(f"File not found: {path}")
    print("\nPress Enter to exit...")
    input()

try:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_id = str(uuid.uuid4())
    data['telemetry.macMachineId'] = new_id

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"New ID: {new_id}")
    print("Success!")
    print("\nPress Enter to exit...")
    input()

except Exception as e:
    print(f"Error: {str(e)}")
    print("\nPress Enter to exit...")
    input()