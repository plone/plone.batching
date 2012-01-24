from setuptools import setup, find_packages

version = '1.0a1'

setup(
    name='plone.batching',
    version=version,
    description="Batching facilities used in Plone.",
    long_description=open("README.rst").read() + "\n" +
                     open("CHANGES.rst").read(),
    classifiers=[
        'Framework :: Plone :: 4.3',
        'Framework :: Zope2',
        'Programming Language :: Python :: 2.6',
    ],
    keywords='Plone',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='http://pypi.python.org/pypi/plone.batching',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    entry_points='''
          [z3c.autoinclude.plugin]
          target = plone
      ''',
)
