import os
import logging.config
import tomllib

from kernel.settings.base import BASE_DIR

if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))

if not os.path.exists(os.path.join(BASE_DIR, 'logs/core')):
    os.makedirs(os.path.join(BASE_DIR, 'logs/core'))

if not os.path.exists(os.path.join(BASE_DIR, 'logs/auth')):
    os.makedirs(os.path.join(BASE_DIR, 'logs/auth'))

with open('configs/log/logging.toml', 'rb') as config_file:
    log_config = tomllib.load(config_file)
    logging.config.dictConfig(log_config)
