import setuptools
import os

# package metadata
NAME = 'faceonnx'
VERSION = '1.0.3.1'
DESCRIPTION = 'Face analytics library based on deep neural networks and ONNX runtime.'
LICENSE = 'MIT'
GIT = 'https://github.com/asiryan/FaceONNX'
PYTHON = '>=3.5'

# directory
this = os.path.dirname(__file__)

# readme
with open(os.path.join(this, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# requirements
with open(os.path.join(this, 'requirements.txt'), "r") as f:
    requirements = [_ for _ in [_.strip("\r\n ")
                                for _ in f.readlines()] if _ is not None]
# setup tools
setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    license=LICENSE,
    packages=setuptools.find_packages(),
    python_requires=PYTHON,
    author='Valery Asiryan',
    author_email='dmc5mod@yandex.ru',
    url=GIT,
    install_requires=requirements,
    package_data={
      NAME: ['*.onnx', os.path.join(this, './models/*.onnx')],
    },
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Image Recognition'
    ],
)