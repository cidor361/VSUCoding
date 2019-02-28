import time

start = time.clock()
i = 1 + 1
elapsed = (time.clock() - start)
print(elapsed)

start = time.time()
k = 1 + 1
elapsed = (time.time() - start)
print(elapsed)

#         Результат:
#         2.000000000002e-06
#         4.76837158203125e-06
#         В Unix time.clock() измеряет количество процессорного времени, которое было использовано текущим процессом;
#         В любой системе time.time() будет возвращать секунды, прошедшие с эпохи.