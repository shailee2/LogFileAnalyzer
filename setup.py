from setuptools import setup

setup(
    name='logfileanalyzer',
    version='0.1',
    py_modules=['log_analyzer'],
    install_requires=['colorama'],
    entry_points={
        'console_scripts': [
            'log-analyzer=log_analyzer:main',
        ],
    },
    author='Shailee Patel',
    description='A command-line log file analyzer with filtering and export features.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shailee2/logfile-analyzer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)