from setuptools import find_packages, setup

setup(
    name='FCamara',
    description='Teste Fullstack',
    version='0.0.1',
    url='https://github.com/',
    license='GPL',
    author='Adauto Nóbrega',
    author_email='adauto204@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-session',
        'sqlalchemy'
    ],
    dependency_links=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite="tests",
    package_data={
    },
    extras_require={
        'dev': [
            'alembic',
            'bandit',
            'coverage',
            'flake8',
            'flake8-docstrings',
            'flake8-quotes',
            'flake8-todo',
            'flask-webtest',
            'isort',
            'autopep8',
            'tox',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.5',
    ],
)
