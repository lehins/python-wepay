from setuptools import setup, find_packages
import wepay
import os, sys

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    if sys.version < '3':
        return open(path).read()
    return open(path, encoding="utf-8").read()


setup(
    name='python-wepay',
    version=wepay.get_version(),
    packages=find_packages(),
    description="Python SDK for WePay API (third party).",
    long_description='%s\n\n%s' % (read('README.rst'), read('CHANGELOG.rst')),
    author='Alexey Kuleshevich',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=["wepay", "payment", "credit card"],
    install_requires=['six'],
    tests_require=['mock', 'requests']
)
