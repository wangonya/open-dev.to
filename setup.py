from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='open-dev.to',
    version='1.0',
    description="Open a new dev.to browser tab from your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangonya/open-dev.to",
    author="Kinyanjui Wangonya",
    author_email="kwangonya@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dev.to=app:main
    ''',
)
