from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="rss-reader",
    version="1.0",
    packages=find_packages(),
    #scripts=[],
    install_requires=['beautifulsoup4==4.8.1', 'feedparser==5.2.1'],
    author="Ilya Khonenko",
    author_email="honenkoi@gmail.com",
    description="This is rss-reader",
    long_description = long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # url="https://github.com"
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

