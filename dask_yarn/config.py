import os

import dask
import yaml


fn = os.path.join(os.path.dirname(__file__), 'yarn.yaml')
dask.config.ensure_file(source=fn)

with open(fn) as f:
    defaults = yaml.safe_load(f)

dask.config.update_defaults(defaults)
