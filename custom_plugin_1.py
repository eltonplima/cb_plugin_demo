def run(job, logger, **kwargs):
    logger.info('Im playing with jobs')
    print('Test if this modification go to the server in "real time"')
    print(dir(job))

    return "SUCCESS", "It's alive!!!", ""
