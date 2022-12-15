import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='fletcarousel',
    author='naderidev',
    author_email='mohammadrezanaderi84@gmail.com',
    description='Simple carousel sliders for flet framework',
    keywords=['flet', 'carousel', 'slideshow', 'slider', 'python', 'flet-carousel', 'fletcarousel'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/naderidev/flet-carousel',
    package_dir={'': 'fletcarousel'},
    packages=setuptools.find_packages(where='fletcarousel'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.9',
    install_requires=[
        'flet'
    ],
)