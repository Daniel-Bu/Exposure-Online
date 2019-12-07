import sys
EXPOSURE_DIR = '../exposure'
sys.path.insert(1, EXPOSURE_DIR)
import os
from app_evaluate import evaluate

def eva(files=None):
    os.chdir('../exposure')
    evaluate(files)

if __name__ == "__main__":
    files = ['models/sample_inputs/A.tif', 'models/sample_inputs/B.tif']
    eva(files)
