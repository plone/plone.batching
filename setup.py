# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.1.7.dev0'

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
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Core",
        "Framework :: Zope2",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
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
        'Zope2',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
