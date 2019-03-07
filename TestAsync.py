import requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]

def my_func(url):
    res = requests.get(url)
    print(f"{res.status_code} - {url}")


# make the Pool of workers
pool = ThreadPool(4)

# open the urls in their own threads
# and return the results
results = pool.map(my_func, urls)

# close the pool and wait for the work to finish
pool.close()
pool.join()
