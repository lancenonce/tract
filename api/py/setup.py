from setuptools import setup
from setuptools_rust import Binding, RustExtension
import toml
import re

version = toml.load("../Cargo.toml")["package"]["version"]
version = re.sub("\-alpha\.", "a", version)
version = re.sub("\-.*", ".dev", version)

with open('docs/index.md', 'r') as file:
    readme = file.read()

setup(
        name="tract",
        author="Mathieu Poumeyrol, Sonos, and tract contributors",
        author_email="mathieu@poumeyrol.fr",
        keywords="onnx tensorflow nnef runtime neural network",
        version=version,
        description="Python bindings for tract, a neural network inference engine",
        project_urls={
            "Documentation": "https://sonos.github.io/tract",
            "Source": "https://github.com/sonos/tract",
        },
        license="Apache License, Version 2.0 OR MIT",
        long_description=readme,
        long_description_content_type="text/markdown",
        options={"bdist_wheel": {"universal": True}},
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Rust",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "License :: OSI Approved :: Apache Software License",
            "License :: OSI Approved :: MIT License"
            ],
        rust_extensions=[RustExtension("tract.tract", binding=Binding.NoBinding, path="../ffi/Cargo.toml")],
        packages=["tract"],
        zip_safe=False,
        python_requires=">=3.7",
        install_requires=[ "numpy" ],
        extras_require={ "test": ["pytest"] },
)

