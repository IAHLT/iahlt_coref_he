from setuptools import setup


setup(
    name='iahlt_coref_he',
    version='0.1.0',
    packages=['iahlt_coref_he'],
    install_requires=[
        'ufal.udpipe==1.3.1.1',
        'fastcoref==2.1.6',
        'conllu==4.5.3'
    ],
    package_data = {},
    include_package_data=True
)
