#from setuptools import setup
from distutils.core import setup

setup(
    name = 'caterapp',
    packages=['caterapp'],
    version = '1.1',  # Ideally should be same as your GitHub release tag varsion
    description='A TCP based file sharing application',
    author='Ravi Prakash',
    author_email='ravi.cs20@iiitmk.ac.in',
    url='https://github.com/ravi-prakash1907/CaterApp', # github source url
    download_url = 'https://github.com/ravi-prakash1907/CaterApp/archive/refs/tags/v0.1-alpha.tar.gz',
    long_descp = 'README.md',
    keywords = ['v0.1-alpha', 'caterapp'],
    REQUIRED = ['cater','shareBox'],
    classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" ---- the current state of this package
    'License :: OSI Approved :: MIT License',   # picking a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',    
  ],
)
