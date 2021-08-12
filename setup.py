from setuptools import setup, find_packages

setup(
    name="lhorizon",
    version="1.0.0",
    url="https://github.com/millionconcepts/lhorizon.git",
    author="Million Concepts",
    author_email="mstclair@millionconcepts.com",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "more-itertools",
        "requests",
        "pandas",
    ],
    extras_require={
        "tests": ["pytest", "pytest-mock", "pytest-cov"],
        "target": ["spiceypy", "sympy"],
        "examples": ["jupyter"],
    },
    package_data={
        "": ["kernels/*.*", "tests/data/*.*"],
    },
)
