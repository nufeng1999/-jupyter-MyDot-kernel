#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyDot_kernel',
      vedotion='0.0.1',
      description='Minimalistic Dot kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      url='https://github.com/nufeng1999/jupyter-MyDot-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyDot-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiedot=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
      scripts=['jupyter_MyDot_kernel/install_MyDot_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'dot','dot'],
      include_package_data=True
      )
