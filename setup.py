from setuptools import setup, find_packages

setup(
    name='emotion_detection',               # Name of your package
    version='1.0',
    packages=find_packages(),              # Automatically finds your package dirs
    install_requires=[
        'requests',                        # Dependencies from requirements.txt
    ],
    author='F West',
    description='A package for detecting emotions',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6.11',
)