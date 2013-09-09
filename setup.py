from distutils.core import setup
import wepay
import os.path

short_description = 'Unofficial Python SDK for WePay API.'
long_description = open('README.rst').read() if os.path.isfile('README.rst') \
                   else short_description

version_str = '%s.%s.%s' % (
    wepay.VERSION[0],
    wepay.VERSION[1],
    wepay.VERSION[2]
)

setup(
    name='python-wepay',
    version=version_str,
    packages=['wepay'],
    description=short_description,
    long_description=long_description,
    author='lehins',
    author_email='lehins@yandex.ru',
    license='MIT License',
    url='https://github.com/lehins/python-wepay',
    platforms=["any"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
