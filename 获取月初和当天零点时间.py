from datetime import datetime
import time

now = datetime.now()
time.sleep(2)
after = time.localtime()
print(after)
after = "%d-%02d-%02d" % (after.tm_year, after.tm_mon, after.tm_mday)
after = datetime.strptime(after, '%Y-%m-%d')  # 可以得到月初时间 原理是格式化时间的时候不传入当前的月和日期

print(after)
print(now)
print("od")
print("daffa")
