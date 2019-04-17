# -*- coding: utf-8 -*-
import os

import yaml


def load():
    with open(os.environ.get('TAHITI_CONFIG')) as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    return config

tahiti_configuration = load()
