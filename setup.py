import setuptools

setuptools.setup(
    name='localagi',
    version='1.0.2',
    license='MIT',
    packages=['localagi'],
    description='Experience local Artificial General Intelligence.',
    long_description=open('README.txt').read(),
    long_description_content_type="text/markdown",
    author='Hallvard Høyland Lavik',
    url='https://github.com/hallvardnmbu/localagi.git',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',
    install_requires=[
        'torch',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'localagi = localagi.__main__:main',
            'localagi-load = localagi.__main__:load',
            'localagi-prompt = localagi.__main__:prompt',
        ],
    },
)
