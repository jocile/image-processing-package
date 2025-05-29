
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='image-processing',
    version='0.0.1',
    author='Jocile',
    author_email='jocilecam@gmail.com',
    description='Image Processing Package using skimage',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jocile/image-processing-package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
    python_requires='>=3.5',
)
