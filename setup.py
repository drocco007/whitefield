from setuptools import setup, find_packages


setup(
    name='WhitefieldScheduler',
    version='0.10.1',
    description='Whitefield class schedule application',
    author='Daniel J. Rocco',
    author_email='drocco@gmail.com',
    url='',
    install_requires=[
        'parsedatetime>=0.8.6',
        'pyramid',
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={'whitefieldscheduler': ['i18n/*/LC_MESSAGES/*.mo']},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = whitefield.mobile.__main__:main
    """,
)
