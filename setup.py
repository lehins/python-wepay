from distutils.core import setup
import wepay
import os.path

short_description = 'Unofficial Python SDK for WePay API.'
long_description = open('README.rst').read() if os.path.isfile('README.rst') \
                   else short_description

setup(
    name='python-wepay',
    version=wepay.get_version(),
    packages=['wepay'],
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
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
