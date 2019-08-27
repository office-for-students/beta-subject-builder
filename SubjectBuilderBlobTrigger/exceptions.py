""" exceptions.py: PostcodeSearchBuilder Custom Exceptions """


class Error(Exception):
    """ Base Exception Class """
    pass


class StopSubjectBuilderWarningException(Error):
    """ A warning is raised during the ETL Pipeline """
    pass


class StopSubjectBuilderErrorException(Error):
    """ An error is raised during the ETL Pipeline """
    pass
