import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask-KubeProxy",
    version="0.0.1",
    author="Robbe Sneyders",
    author_email="robbe.sneyders@ml6.eu",
    description="Middleware to fix swagger behavior behind kubernetes proxy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)