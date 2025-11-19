from pathlib import Path
from setuptools import setup


version = "3.0.0a1"

long_description = (
    f"{Path('README.rst').read_text()}\n"
    f"{Path('CHANGES.rst').read_text()}\n"
    f"{(Path('docs') / 'usage.rst').read_text()}"
)

setup(
    name="plone.batching",
    version=version,
    description="Batching facilities used in Plone",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="Plone",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/plone.batching",
    license="GPL",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "AccessControl",
        "Zope",
        "zope.interface",
        "zope.schema",
    ],
    extras_require={
        "test": [
            "zope.component",
            "zope.publisher",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
