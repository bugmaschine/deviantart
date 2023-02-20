from setuptools import setup

setup(
    name="new-deviantart",
    version="0.1.6",
    description="A Python wrapper for the DeviantArt API",
    url="https://github.com/bugmaschine/deviantart",
    author="Kevin Eichhorn",
    author_email="kevineichhorn@me.com",
    license="MIT",
    packages=["new-deviantart"],
    install_requires=[
        "sanction"
    ]
)
