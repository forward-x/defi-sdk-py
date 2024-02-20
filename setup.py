import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fwx-python-sdk",                     # This is the name of the package
    version="v1.0.4",                        # The initial release version
    author="FWX/xAKIOx",                     # Full name of the author
    description="SDK for intregration with FWX protocol on RPC chain",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',                # Minimum version requirement of the package
    py_modules=["defi_sdk_py"],             # Name of the python package
    package_dir={'':'./'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)