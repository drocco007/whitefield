from setuptools import setup, find_packages


setup(
    name='WhitefieldScheduler',
    version='0.9',
    description='Whitefield class schedule application',
    author='Daniel J. Rocco',
    author_email='drocco@gmail.com',
    url='',
    install_requires=[
        "parsedatetime>=0.8.6",
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={'whitefieldscheduler': ['i18n/*/LC_MESSAGES/*.mo']},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    #[paste.app_factory]
    #main = whitefieldscheduler.config.middleware:make_app

    #[paste.app_install]
    #main = pylons.util:PylonsInstaller
    """,
)
