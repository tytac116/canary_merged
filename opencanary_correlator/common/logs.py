import logging

class RedisHandler(logging.Handler):
    """
    A class which sends records to a redis list.
    """

    def __init__(self, level=logging.NOTSET):
        #this song and dance avoids a circular dependency at load time,
        #by importing only when this class is instatiated
        super(RedisHandler, self).__init__(level=level)
        from opencanary_correlator.common.queries import write_log
        self.write_log = write_log

    def emit(self, record):
        """
        Emit a record.
        """
        try:
            self.write_log(self.format(record))
        except:
            self.handleError(record)

logger = None
# Console and correlator use different logger names. Common modules
# should still log to the logger for the process under which they're running.
# Impact of this is we don't support multiple loggers per process
existing_logger_names = logging.getLogger().manager.loggerDict.keys()
if len(existing_logger_names) > 0:
    lgr = list(existing_logger_names)[0]
    logger = logging.getLogger(lgr)


