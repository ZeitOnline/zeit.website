from setuptools import setup, find_packages

setup(
    name='zeit.website',
    version='1.1.2.dev0',
    author='Dominik Hoppe',
    author_email='dominik.hoppe@zeit.de',
    url='',
    description="""\
""",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='gocept proprietary',
    namespace_packages=['zeit'],
    install_requires=[
        'gocept.httpserverlayer',
        'gocept.selenium',
        'gocept.testing>=1.4.0.dev0',
        'grokcore.component',
        'plone.testing',
        'setuptools',
        'zc.form',
        'zeit.cms>=2.20.0.dev0',
        'zeit.content.article>=3.5.0.dev0',
        'zeit.edit',
        'zope.interface',
        'zope.component',
    ],
)
