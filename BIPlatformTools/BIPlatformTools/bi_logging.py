def log_test(library):
    """
    Will print out the given library name.
    """
    print(f"This is a statement from the library: {library}")


# import logging


# def init_logging(name="default_name",
#                  log_level=logging.DEBUG,
#                  session=None,
#                  log_group="default_log_group",
#                  stream_name="default_stream_name"):
#     """ Configure the root logger with a file handler, console handler and optional cloudwatch handler.
#     Ensures the file handler is a rotating log """

#     log_path = "./logs"
#     log_file = f"{log_path}/{stream_name}-{datetime.now().strftime(" % Y % m % d")}.log"
#     # ensure the log path directory exists
#     os.makedirs(log_path, exist_ok=True)

#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                         stream=stream_name)

#     # create the logs in the directory below where the code is running from- relative path
#     # add a rotating handler based on the day
#     file = TimedRotatingFileHandler(log_file,
#                                     when="midnight",
#                                     interval=1,
#                                     backupCount=7)
#     file.setLevel(log_level)
#     # create console handler with a lower log level
#     console = logging.StreamHandler()
#     console.setLevel(log_level)

#     fh.setFormatter(formatter)
#     ch.setFormatter(formatter)

#     # add the handlers to the logger
#     log.addHandler(file)
#     log.addHandler(console)

#     # create cloudwatch handler if a boto3 session has been passed in
#     if session is not None:
#         cloudwatch = watchtower.CloudWatchLogHandler(boto3_session=session,
#                                                      log_group=log_group,
#                                                      stream_name=stream_name)
#         # limit cloudwatch to INFO and above entries only
#         cw.setLevel(logging.INFO)
#         logging.getLogger('').addHandler(cw)


class BiPlatformTools():

    def __init__(self):
            return
