import memcache  # 链接

try:
    mc = memcache.Client(['192.168.50.205:11211'])
except Exception as e:
    print(e)
