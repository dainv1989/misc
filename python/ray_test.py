"""
multiprocessing measurement with Ray lib
reference: https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1
"""
import numpy as np
import ray
import psutil
import time
import scipy.signal

num_cpus = psutil.cpu_count(logical=False)
print("number of CPUs {}".format(num_cpus))

ray.init(num_cpus=num_cpus)

@ray.remote
def f(image, random_filter):
    return scipy.signal.convolve2d(image, random_filter)[::5, ::5]

filters = [np.random.normal(size=(4,4)) for _ in range(num_cpus)]

for _ in range(10):
    image = np.ones((5000, 5000))
    image_id = ray.put(image)
    start_time = time.time()
    ray.get([f.remote(image_id, filters[i]) for i in range(num_cpus)])
    print("execute time {:.2f}ms".format((time.time() - start_time)*1000));
