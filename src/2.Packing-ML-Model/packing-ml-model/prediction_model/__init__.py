from prediction_model.config import config
import os 
with open(os.path.join(config.PACKAGE_ROOT, "VERSION")) as f:
    ___version__ = f.read().strip()
