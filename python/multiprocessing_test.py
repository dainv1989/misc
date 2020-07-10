from multiprocessing import Pool
import numpy as np
import time
import psutil
import scipy.signal


num_cpus = psutil.cpu_count(logical=False)

def f(args):
    image, random_filter = args
    return scipy.signal.convolve2d(image, random_filter)[::5, ::5]

pool = Pool(num_cpus)

filters = [np.random.normal(size=(4,4)) for _ in range(num_cpus)]

for _ in range(10):
    image = np.ones((5000, 5000))
    start_time = time.time()
    pool.map(f, zip(num_cpus * [image], filters))
    print("execute time {:.2f}ms".format((time.time() - start_time)*1000));
