import os
from path import Path
import logging

logging.basicConfig(level= logging.INFO, format='[%(asctime)s)]: %(message)s:')

list_of_files = [
    
f"src/__init__.py",
f"src/components/__init__.py",
f"src/components/data_ingetion.py",
f"src/components/data_transform.py",
f"src/components/model_traner.py",
f"src/pipeline/__init__.py",
f"src/pipeline/train_pipeline.py",
f"src/pipeline/train_pipeline.py",
f"src/logger.py",
f"src/exception.py",
f"src/utils.py",
f"templates/index.html",
f"templates/home.html",
f"requirements.txt",
f"README.md",
f"setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename =os.path.split(filepath)
    
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")