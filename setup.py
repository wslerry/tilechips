from setuptools import setup
import subprocess

# Parse the version from the tilechips module.
with open("tilechips/__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue


def gdal_already_installed():
    try:
        from osgeo import gdal  # noqa
        return True
    except ImportError:
        return False


def get_required_gdal():
    gdal_package = 'pygdal'
    try:
        gdal_version = subprocess.check_output(
            'gdal-config --version',
            stderr=subprocess.STDOUT,
            shell=True
        ).decode('utf-8').strip()

        gdal_package = '%s==%s.*' % (gdal_package, gdal_version)
    except subprocess.CalledProcessError:
        pass

    return gdal_package


requirements = []

if not gdal_already_installed():
    requirements.append(get_required_gdal())

setup(
    name='tilechips',
    version=version,
    description='A python package to create raster tiles for deep learning training image chips',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/wslerry/tilechips',
    author='Lerry William',
    author_email='lerryws.xyz@outlook.com',
    license='BSD',
    packages=['tilechips'],
    install_requires=requirements,
    keywords="raster gdal",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
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
