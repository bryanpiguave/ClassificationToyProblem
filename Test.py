import numpy as np
from numpy.core.fromnumeric import size 
import torch
from datetime import datetime
device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
print(device)


def exec_time(func):
    def wrapper(*args,**kwargs):
        w = list()
        for i in range(100):

            initial_time = datetime.now().timestamp()
            func(*args,**kwargs)
            final = datetime.now().timestamp()
            time_elapsed= (final-initial_time)
            w.append(time_elapsed)
        print(sum(w)/len(w))
    return wrapper

@exec_time
def create_numpy():
    n = np.zeros(shape=(3,2))
    return torch.tensor(n)

@exec_time
def create_from_numpy():
    n = np.zeros(shape=(3,2))
    return torch.from_numpy(n)

create_numpy()
create_from_numpy()

