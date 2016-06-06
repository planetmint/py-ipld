from setuptools import setup

tests_require = [
    'pep8',
    'pyflakes',
    'pylint',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'pytest-flask',
]

setup(
    name="py-ipld",
    version="0.0.1",
    author="Tim Daubenschuetz",
    author_email="tim.daubenschuetz@gmail.com",
    description="An IPLD implementation in Python",
    license="Apache-2.0",
    keywords="ipld python ipfs bigchaindb",
    install_requires=[
        'pymultihash>=0.9.0.dev2',
    ],
    dependency_links=[
        'git+https://github.com/TimDaub/pymultihash.git@devel#egg=pymultihash-0.9.0.dev2',
    ],
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
)