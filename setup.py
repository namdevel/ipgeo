import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ipgeo-namdevel",
    version="0.0.1",
    author="namdevel",
    author_email="namdevel@gmail.com",
    description="Free IP Geolocation API and IP Location Lookup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/namdevel/ipgeo",
    project_urls={
        "Bug Tracker": "https://github.com/namdevel/ipgeo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)