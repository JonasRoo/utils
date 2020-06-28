def with_logging(func):
    import sys
    import datetime, time
    def wrap():
        time_format = "%Y-%m-%d--%H-%M-%S"
        timestamp = datetime.datetime.fromtimestamp(time.time())
        formatted_time = timestamp.strftime(time_format)
        file_name = f"{formatted_time}.log"
        with open(file_name, "w") as sys.stdout:
            func()
