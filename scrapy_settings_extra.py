###### log settings start ######
LOG_LEVEL = 'INFO'
LOG_FILE = '/var/log/scrapy.log'

###### log settings start ######

###### mysql settings start ######
MYSQL_SETTINGS = {
                  'DB_HOST': 'ip',
                  'DB_PORT': 3306,
                  'DB_DB': 'scrapy_db',
                  'DB_USER': 'scrapy_db_user',
                  'DB_PASSWD': 'passwd',
                  'DB_CHARSET': 'utf8',
                 }
###### mysql settings end ######

###### scrapy-redis settings start ######
# https://github.com/rmax/scrapy-redis
# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
REDIS_URL = 'redis://:passwd@ip:port'

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

###### scrapy-redis settings end ######
