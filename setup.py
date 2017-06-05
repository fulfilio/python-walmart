import setuptools


requirements = [
    'lxml',
    'pycrypto',
    'requests',
]

test_requirements = [
    'pytest',
]

setuptools.setup(
    name="python-walmart",
    version="0.0.2",
    url="https://github.com/fulfilio/python-walmart",

    author="Fulfil.IO Inc.",
    author_email="hello@fulfil.io",

    description="Walmart Marketplace API",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=requirements,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
