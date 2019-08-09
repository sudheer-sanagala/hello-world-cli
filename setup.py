from setuptools import setup

setup(
    name='hello-world-cli',
    py_modules=['helloworld'],
    intstall_requires=['Click'],
    entry_points='''
        [console_scripts]
        hello=helloworld:hello
        ''',
)
