# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '2.0.0'

setup(
    name='plone.batching',
    version=version,
    description="Batching facilities used in Plone.",
    long_description=u'\n'.join([
        open("README.rst").read(),
        open("CHANGES.rst").read(),
        open("docs/usage.rst").read(),
    ]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords='Plone',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/plone.batching',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Zope',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
