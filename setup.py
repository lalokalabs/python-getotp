# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['getotp', 'getotp.migrations', 'getotp.tests']

package_data = \
{'': ['*'], 'getotp': ['templates/getotp/login/*']}

install_requires = \
['Django<4.0', 'phonenumbers>=8.12.33,<9.0.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'getotp',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Surya',
    'author_email': 'surya@xoxzo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
