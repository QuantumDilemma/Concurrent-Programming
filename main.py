import time
import threading
import asyncio
from multiprocessing import Process

#define average function used for sequential programming, threading, and multiprocessing
def cal_average(num):  
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  return avg

#define main wrapper for sequential example
def main_sequential(list1, list2, list3):  
  s = time.perf_counter()
  
  #calculate averages test case, sequentially
  cal_average(list1)
  cal_average(list2)
  cal_average(list3)

  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")


 #define average function used for asynchronous programming only ( needs await asyncio.sleep() )
async def cal_average_async(num): 
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  return avg

 #define main wrapper for asynchronous example
async def main_async(list1, list2, list3): 
  s = time.perf_counter()
  
  #calculate averages test case, async
  tasks = [
    cal_average_async(list1),
    cal_average_async(list2),
    cal_average_async(list3)
    ]

  await asyncio.gather(*tasks)

  elapsed = time.perf_counter() - s
  print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")


#define main wrapper for threading example
def main_threading(list1, list2, list3):  
  s = time.perf_counter()
  
  #calculate averages test case, threading
  lists = [
    list1,
    list2,
    list3
  ]

  threads = []

  for i in range(len(lists)):
    x = threading.Thread(target = cal_average, args = (lists[i],))
    threads.append(x)
    x.start()

  for t in threads:
    t.join()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")


 #define main wrapper for multiprocessing example
def main_multiprocessing(list1, list2, list3): 
  s = time.perf_counter()
  
  #calculate averages test case, multiprocessing
  lists = [
    list1,
    list2,
    list3
  ]

  processes = [Process(target=cal_average, args=(lists[i],)) for i in range(len(lists))]

  for p in processes:
    p.start()

  for q in processes:
    q.join()

  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")


if __name__ == '__main__':  # Need to use this if-statement so multiprocessing doesn't cause an infinite loop
  #three lists we are trying to calculate average on
  l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
  l2 = [2, 4, 6, 8, 10]
  l3 = [1, 3, 5, 7, 9, 11]
  #run all functions
  main_sequential(l1, l2, l3)
  asyncio.run(main_async(l1, l2, l3))
  main_threading(l1, l2, l3)
  main_multiprocessing(l1, l2, l3)

  #async was the winner, followed closely by threading