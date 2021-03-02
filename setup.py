import logging
import sys

from setuptools import setup
from setuptools.extension import Extension


logging.basicConfig(stream=sys.stderr, level=logging.INFO)
log = logging.getLogger()

# python -W all setup.py ...
if "all" in sys.warnoptions:
    log.level = logging.DEBUG

# Parse the version from the tilechips module.
with open("tilechips/__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue


setup(
    name='tilechips',
    version=version,
    description='A python package to create tiles for deep learning\'s '
                'training image chips',
    url='https://github.com/wslerry/tilechips',
    author='Lerry William',
    author_email='lerryws.xyz@outlook.com',
    license='BSD',
    packages=['tilechips'],
    install_requires=['GDAL',
                      'tqdm',
                      ],
    keywords="raster gdal",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
