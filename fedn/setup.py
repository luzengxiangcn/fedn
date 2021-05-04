from setuptools import setup, find_packages

setup(
    name='fedn',
    version='0.2.2',
    description="""Scaleout Federated Learning""",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Morgan Ekmefjord',
    author_email='morgan@scaleout.se',
    url='https://www.scaleoutsystems.com',
    include_package_data=True,
    py_modules=['fedn'],
    python_requires='>=3.6,<4',
    install_requires=[
        "attrdict",
        "certifi",
        "chardet",
        "PyYAML",
        "requests",
        "urllib3",
        "minio",
        "six",
        "python-slugify",
        "prettytable",
        "grpcio-tools==1.32.0",
        "grpcio>=1.32.0",
        "protobuf",
        "pypandoc==1.5",
        "wheel",
        "pymongo",
        "Flask",
        "Flask-WTF",
        "pyopenssl",
        "plotly",
        "ttictoc",
        "psutil",
        "click",
        "jinja2",
        "nltk",
        "geoip2",
        "pandas"
    ],
    license="Copyright Scaleout Systems AB. See license for details",
    zip_safe=False,
    entry_points={
        'console_scripts': ["fedn=cli:main"]
    },
    keywords='Federated learning',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
