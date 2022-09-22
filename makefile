all: test

test:
	python3 -m doctest bandwidth.py

clean:
	rm -rf __pycache__ .mypy_cache
