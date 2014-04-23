from setuptools import setup
import wepay
import os.path

short_description = 'Third party Python SDK for WePay API.'
long_description = open('README.rst').read() if os.path.isfile('README.rst') \
                   else short_description

setup(
    name='python-wepay',
    version=wepay.get_version(),
    packages=['wepay', 'wepay.calls'],
    description=short_description,
    long_description=long_description,
    author='lehins',
    author_email='lehins@yandex.ru',
    license='MIT License',
    url='https://github.com/lehins/python-wepay',
    platforms=["any"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['six=>1.6.1']
)
