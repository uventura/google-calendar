import logging


class Logger:
    def __init__(self):
        self._formatter = logging.Formatter(
            "{levelname} - {message}", style="{", datefmt="%d.%m.%Y - %H:%M"
        )

        self._console_handler = logging.StreamHandler()
        self._console_handler.setFormatter(self._formatter)

        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(self._console_handler)

    def info(self, *args, **kwargs):
        self._logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self._logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self._logger.debug(*args, **kwargs)

    def error(self, *args, **kwargs):
        self._logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self._logger.critical(*args, **kwargs)
