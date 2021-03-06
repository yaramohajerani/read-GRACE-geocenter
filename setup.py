from setuptools import setup, find_packages

# get long_description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='read-GRACE-geocenter',
    version='1.0.0.0',
    description='Reads geocenter coefficients from Sutterley et al. (2019)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tsutterley/read-GRACE-geocenter',
    author='Tyler Sutterley',
    author_email='tsutterl@uw.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='GRACE time-variable gravity, geocenter, degree one harmonics',
    packages=find_packages(),
    install_requires=['numpy','pyyaml'],
)
