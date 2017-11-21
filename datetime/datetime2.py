from datetime import datetime

now=datetime.now()
print(now)

filename="{0:%Y}-{0:%m}-{0:%d} {0:%H}:{0:%M}:{0:%S}".format(now)
print(filename)

filename +=".h264"
print(filename)
