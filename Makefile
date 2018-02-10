install:
	python setup.py install

freeze:
	# https://stackoverflow.com/a/40167445/5127934
	pip freeze | grep -v "pkg-resources" > requirements.txt
