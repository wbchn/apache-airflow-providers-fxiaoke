from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

"""Perform the package airflow-provider-fxiaoke setup."""
setup(
    name='airflow-provider-fxiaoke',
    version="0.0.2",
    description='Airflow plugins for fxiaoke CRM api.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        "apache_airflow_provider": [
            "provider_info=fxiaoke.__init__:get_provider_info"
        ]
    },
    license='Apache License 2.0',
    packages=['fxiaoke', 'fxiaoke.hooks',
              'fxiaoke.operators'],
    install_requires=['apache-airflow>=2.1'],
    setup_requires=['setuptools', 'wheel'],
    author='wb',
    author_email='wb@papaya*mobile.com',
    url='http://papaya.io/',
    python_requires='~=3.8',
)