from setuptools import setup, find_packages


requires = [
    'pyramid',
    'pyramid_tm',
    'SQLAlchemy',
    'psycopg2',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'parsedatetime>=0.8.6',
    'alembic',
    'ziggurat_foundations',
]

setup(
    name='WhitefieldScheduler',
    version='0.10.2',
    description='Whitefield class schedule application',
    author='Daniel J. Rocco',
    author_email='drocco@gmail.com',
    url='',
    install_requires=requires,
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [paste.app_factory]
    main = whitefield.mobile.__main__:main
    """,
)
