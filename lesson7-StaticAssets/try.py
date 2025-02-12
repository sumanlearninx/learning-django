from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent
path_joined = os.path.join(BASE_DIR,'static')
print(f"BASE DIr is : {BASE_DIR}")  
print(f"Path joined is : {path_joined}")  