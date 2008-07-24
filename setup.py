try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='img_gallery',
    version="0.1",
    #description='',
    #author='',
    #author_email='',
    #url='',
    install_requires=[
        "setuptools",
        "Pylons>=0.9.6.1",
        "SQLAlchemy>=0.4.1",
        "PILwoTk",
        #"liblicense",
        ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'img_gallery': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'img_gallery': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    entry_points="""
    [paste.app_factory]
    main = img_gallery.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
