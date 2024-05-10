deployment/upload-pypi/build-package
cp deployment/upload-pypi/config/.pypirc ~/.pypirc
pip install twine
pip install --upgrade twine
twine upload dist/*

# rm -rf *.egg-info build dist
