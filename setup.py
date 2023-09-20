from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Personal library'
LONG_DESCRIPTION = 'A collection of useful methods from personal use'

setup(
        name="mylib66", 
        version=VERSION,
        author="Chazz Yu",
        author_email="<cklibrary2@qq.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['matplotlib'],
        url="https://github.com/Chazz0606/mylib66",
        
        keywords=['python', 'personal'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)