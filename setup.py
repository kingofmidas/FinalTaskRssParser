from setuptools import setup, find_packages
import os


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()

def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'rss_reader/version.py')) as f:
        VERSION = None
        exec(f.read())
        return VERSION
    raise RuntimeError('No version info found.')

setup(
    name="rss-reader",
    version=get_version(),
    packages=find_packages(),
    install_requires=['beautifulsoup4','dominate','feedparser','pdfkit','twine','urllib3'],
    author="ilya khonenko",
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
