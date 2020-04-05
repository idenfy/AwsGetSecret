from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    name='aws_get_secret',
    version='1.0.0',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    packages=find_packages(exclude=['venv', 'test']),
    description=('AWS package which helps your program to retrieve a secret value stored in AWS Secrets Manager.'),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'boto3',
    ],
    author='Deividas Tamkus, Laimonas Sutkus',
    author_email='dtamkus@gmail.com (deividas@idenfy.com), laimonas.sutkus@gmail.com (laimonas@idenfy.com)',
    keywords='AWS SecretsManager Secret',
    url='https://github.com/idenfy/AwsGetSecret.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
