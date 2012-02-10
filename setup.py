from setuptools import setup, find_packages

# see http://packages.python.org/distribute/setuptools.html
setup(
    name='example-app',
    version='0.0.1',
    packages=find_packages(),

    install_requires=[
        'requests == 0.10.1',
        'BeautifulSoup == 3.2.0',
    ],

    entry_points={
        'console_scripts': [
            'isitchristmas = example.main:isitchristmas',
            'isithalloween = example.main:isithalloween',
        ]
    },

    author='Tim Monks',
    author_email='t.r.monks@gmail.com'
)
