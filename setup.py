from setuptools import setup, find_packages
setup(
    name='kyokowt',
    version='0.0.2',
    license='MIT',
    description='kyokowt',

    author='kahenteikou',
    author_email='kokkiemouse@gmail.com',
    url='None.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
