import random 
from pathlib import Path 
from glob import glob
import shutil

DOG_DIR = 'data/Dog1'
CAT_DIR = 'data/Cat1'

dog_origin = glob(DOG_DIR + '/*.jpg')
cat_origin = glob(CAT_DIR + '/*.jpg')

sampled_dog = random.sample(dog_origin, 100)
sampled_cat = random.sample(cat_origin, 100)

for dog, cat in zip(sampled_dog, sampled_cat) : 
    shutil.copy(dog, 'data/dog')
    shutil.copy(cat, 'data/cat')
