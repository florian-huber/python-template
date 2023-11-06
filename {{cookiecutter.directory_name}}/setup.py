from setuptools import find_packages, setup

setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.version }}",
    packages=find_packages(),
    install_requires=[
        # Define your project's dependencies here, e.g.,
        # 'requests',
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "pylint",  # or "ruff" if you choose to use ruff
            "pytest",  # if you're using pytest for tests
        ]
    },
)
