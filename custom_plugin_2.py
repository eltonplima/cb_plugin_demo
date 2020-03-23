def run(job, logger, **kwargs):
    logger.info("I'm playing with jobs again")
    print(dir(job))
    print(kwargs)

    return "SUCCESS", "It's alive!!!", ""
