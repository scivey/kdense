from setuptools import setup

version_path = 'kdense/version.py'

exec(open(version_path).read())

setup(
    name="kdense",
    zip_safe=True,
    version=VERSION,
    description="Efficient kernel density estimation for numpy+scipy.",
    url="http://github.com/scivey/kdense",
    maintainer="Scott Ivey",
    maintainer_email="scott.ivey@gmail.com",
    packages=['kdense'],
    package_dir={'kdense': 'kdense'},
    install_requires=['scipy>=0.15.1', 'numpy>=1.10.1']
)
