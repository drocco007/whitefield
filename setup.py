try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='WhitefieldScheduler',
    version='0.2',
    description='Whitefield class schedule application',
    author='Daniel J. Rocco',
    author_email='drocco@gmail.com',
    url='',
    install_requires=[
        "Pylons>=0.9.7",
        "parsedatetime>=0.8.6",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'whitefieldscheduler': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'whitefieldscheduler': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = whitefieldscheduler.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
