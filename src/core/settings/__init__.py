from .django import *       # All Django related settings
from .third_party import *  # Celery, Django REST Framework & other 3rd parties

if DEBUG:
    from .dev import *      # Custom dev settings
else:
    from .production import * # Custom production settings
