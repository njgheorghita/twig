#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    'test': [
        "pytest==3.3.2",
        "pytest-xdist",
        "tox>=2.9.1,<3",
    ],
    'lint': [
        "black>=18.6b4,<19",
        "flake8==3.4.1",
        "isort>=4.2.15,<5",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +
    extras_require['test'] +
    extras_require['lint'] +
    extras_require['doc']
)

setup(
    name='twig',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.1.0-alpha.3',
    description="""twig: A tool for Ethereum smart contract development.""",
    long_description_markdown_filename='README.md',
    author='Jason Carver',
    author_email='ethcalibur+pip@gmail.com',
    url='https://github.com/ethereum/twig',
    include_package_data=True,
    install_requires=[
        "eth-utils>=1,<2",
        "ethpm==0.1.3a7",
        "pytest-ethereum==0.1.2-alpha.3",
        "web3[tester]==4.4.1",
    ],
    setup_requires=['setuptools-markdown'],
    python_requires='>=3.5, <4',
    extras_require=extras_require,
    py_modules=['twig'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
