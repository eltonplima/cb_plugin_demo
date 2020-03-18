def run(job, logger, **kwargs):
    logger.info(job)
    print('Test if this modification go to the server in "real time"')

    return "SUCCESS", "It's alive!!!", ""
