import os 
import setuptools 

def requirements(file="requirements.txt"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return r.read()
    else:
        return ""


setuptools.setup(
    name="Mdthings",
    version="0.0.2",
    description="my requirements",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Md movies",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Tracker": "https://github.com/hockbhmv/Mdthings/issues",
        "Source": "https://github.com/hockbhmv/Mdthings"
    },
    url="https://github.com/hockbhmv/Mdthings"
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements()
)
