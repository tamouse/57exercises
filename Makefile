
clean:
	git ls-files --others | xargs rm -rf
	find . -name 'node_modules' | xargs rm -rf
	find . -name 'bower_components' | xargs rm -rf
	find . -name '_build' | xargs rm -rf
	find . -name '__pycache__' | xargs rm -rf
	find . -name *.pyc | xargs rm -rf
	find . -name *~ | xargs rm -rf
