import logging

_logger: logging.Logger = logging.getLogger(__name__)


def setup_logger() -> None:
    library_logger = logging.getLogger("my_awesome_component")
    library_logger.setLevel("INFO")
    # Create handler and so on
    stream_handler = ...
    library_logger.addHandler(stream_handler)


if __name__ == "__main__":
    setup_logger()
    # the next line will also get printed because the name of _logger is
    # my_awesome_component.cli and _logger is therefore a child of the
    # logger named my_awesome_component.
    _logger.debug("logging setup done")
