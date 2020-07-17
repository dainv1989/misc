"""
Concurrent example in python
ref: https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_pool_of_threads.htm
"""
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
   'http://www.cnn.com/',
   'https://vietnamnet.vn/',
   'http://www.bbc.co.uk/',
   'http://some-made-up-domain.com/']

def load_url(url, timeout):
   with urllib.request.urlopen(url, timeout = timeout) as conn:
       return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor:

   future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
   for future in concurrent.futures.as_completed(future_to_url):
       url = future_to_url[future]
       try:
          data = future.result()
       except Exception as exc:
          print('%r generated an exception: %s' % (url, exc))
       else:
          print('%r page is %d bytes' % (url, len(data)))
