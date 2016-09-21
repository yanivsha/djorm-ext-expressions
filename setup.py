from setuptools import setup, find_packages

description="""
Facility of complex sql expressions for Django orm.
"""

setup(
    name = "djorm-ext-expressions",
    version = '0.7',
    url = 'https://github.com/niwibe/djorm-ext-expressions',
    license = 'BSD',
    platforms = ['OS Independent'],
    description = description.strip(),
    author = 'Andrey Antukh',
    author_email = 'niwi@niwi.be',
    maintainer = 'Andrey Antukh',
    maintainer_email = 'niwi@niwi.be',
    packages = find_packages(),
    include_package_data = False,
    install_requires = [
        'djorm-ext-core >= 0.4.1',
    ],
    zip_safe = False,
    classifiers = [
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ]
)
