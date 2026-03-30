# type: ignore

from setuptools import setup

setup(
  name="cyan-x",
  version="1.4.6",
  description="(blunt-rw) finally, pyzule doesn't suck",
  author="zx",
  author_email="z@zxcvbn.fyi",
  maintainer="b1atant",
  packages=["cyan", "cyan.tbhtypes"],
  python_requires=">=3.9",
  include_package_data=True,
  entry_points={
    "console_scripts": [
      "cyan-x=cyan.__main__:main",
    ],
  }
)

