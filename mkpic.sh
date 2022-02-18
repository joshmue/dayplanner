set -ex

for file in 0*_*.py; do
	python3 -u $file
done
