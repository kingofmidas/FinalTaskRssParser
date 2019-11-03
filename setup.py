from setuptools import setup, find_packages
import os
from pip._internal.req import parse_requirements


with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'rss/version.py')) as f:
        VERSION = None
        exec(f.read())
        return VERSION
    raise RuntimeError('No version info found.')


requirements = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'))


setup(
    name="rss-reader",
    version=get_version(),
    packages=find_packages(),
    #scripts=[],
    install_requires=[str(requirement.req) for requirement in requriements],
    author="Ilya Khonenko",
    author_email="honenkoi@gmail.com",
    # url="https://github.com"
    description="This is rss-reader",
    long_description = long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="rss reader",
    python_requires='>=3.8',
)

#python setup.py sdist bdist_wheel
#(for testing)
#python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
#python -m pip install --index-url https://test.pypi.org/simple/ --no-deps ilyakhonenko (in venv)
#(for real)
#python -m twine upload dist/*      (https://pypi.org by default)
#pip install [your-package]

