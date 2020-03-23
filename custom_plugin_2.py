def run(job, logger, **kwargs):
    logger.info("I'm playing with jobs again")
    print('{:#^80}'.format('job'))
    print(dir(job))
    print('{:#^80}'.format('kwargs'))
    print(kwargs)

    return "SUCCESS", "It's alive!!!", ""
