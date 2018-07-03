install:
	python setup.py install

freeze requirements:
	# https://stackoverflow.com/a/40167445/5127934
	pip freeze | grep -v "pkg-resources" > requirements.txt

clean:
	rm -f l293d/*.pyc
	rm -f *.pyc

test:
	tests/local-tests.sh

dist:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

