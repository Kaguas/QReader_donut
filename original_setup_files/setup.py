from setuptools import find_packages, setup

setup(
    name="qreader_donut",
    version="3.16d",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # expose qreader.py as the unique module
    py_modules=["qreader_donut"],
    # include py.typed file in the distribution
    package_data={"qreader_donut": ["src/qreader/py.typed"]},
    url="https://github.com/Kaguas/QReader_donut",
    license="MIT",
    author="Kaguas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy",
        "opencv-python",
        "pyzbar",
        "qrdet>=2.5",
        "donutcode",
    ],
    extras_require={
        "tests": ["mypy", "pytest", "qrcode"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
