import logging
logging.basicConfig(filename = "test3.log", level = logging.DEBUG, format = '%(asctime)s %(name)s %(levelname)s %(message)s', filemode = 'w')
console_log = logging.StreamHandler()
console_log.setLevel(logging.INFO)
format = '%(asctime)s %(levelname)s %(message)s'
console_log.setFormatter(format)
logging.getLogger().addHandler(console_log)
logging.info("this is my first test code for log")
logger1 = logging.getLogger('user1')
logger2 = logging.getLogger('user2')
logger3 = logging.getLogger('user3')
logger4 = logging.getLogger('user4')
logger1.info("this is info for logger zero")
logger1.debug("this is debug for logger zero")
logger2.debug("this is debug for logger one")
logger2.info("this is info for logger one")

