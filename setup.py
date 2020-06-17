import setuptools

with open("README.md", 'r') as f:
	long_description = f.read()

setuptools.setup(
	name = "eponym-alloy",
	version = "1.0.0",
	author = "Sean Christians",
	author_email = "seanchristians.scc@gmail.com",
	description = "Useful tool for generating variable names",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/seanchristians/eponym",
	packages = setuptools.find_packages(),
	classifiers = [
		"License :: OSI Approved :: GNU Affero General Public License v3",
		"Natural Language :: English",
		"Operating System :: Unix",
		"Programming Language :: Python :: 3.8",
		"Topic :: Database"
	],
	python_requires = ">=3.8"
)
