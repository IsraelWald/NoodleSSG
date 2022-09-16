from setuptools import setup
from noodle import __version__, __author__

setup(
    name='Noodle',
    version=__version__,
    author=__author__,
    description="Noodle SSG: Another Static Site Generator",
    packages=['noodle'],
    entry_points={
        'console_scripts': [
            'noodle = noodle.__main__:cli'
        ]
    }
)