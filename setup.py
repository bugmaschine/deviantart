from setuptools import setup

setup(
    name="new_deviantart",
    version="0.2.4",
    description="A Python wrapper for the DeviantArt API",
    url="https://github.com/bugmaschine/deviantart",
    author="Kevin Eichhorn",
    author_email="kevineichhorn@me.com",
    license="MIT",
    packages=["new_deviantart"],
    install_requires=[
        "sanction"
    ]
)
