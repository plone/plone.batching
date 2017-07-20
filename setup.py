# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.1.2'

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
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/plone.batching',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Zope2',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
