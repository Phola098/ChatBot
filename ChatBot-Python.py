from _typeshed import SupportsNoArgReadline
import nltk
nltk.downlaod('punkt')
nltk.downlaod(wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np 
from kera.models import sequential
from keras.layers import dense, Activation, Dropout
from keras.optimizers import Sgd 
