import logging
import sys

# LOGGING CONFIGS
# Caso queira aprender mais:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI

LOG_LEVEL = logging.DEBUG
# Você pode comentar isso se quiser (root level)
logging.getLogger().setLevel(LOG_LEVEL)

# Nosso logger (GERAL)
LOGGER = logging.getLogger("conc_lessons")
LOGGER.setLevel(LOG_LEVEL)


logger_formatter = logging.Formatter(fmt="%(message)s")
logger_stream_handler = logging.StreamHandler(stream=sys.stdout)
logger_stream_handler.terminator = ""  # Remove a quebra de linha padrão

logger_stream_handler.setFormatter(logger_formatter)
LOGGER.addHandler(logger_stream_handler)
