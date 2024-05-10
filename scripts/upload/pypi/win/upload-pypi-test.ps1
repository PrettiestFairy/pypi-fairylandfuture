deployment/upload-pypi/build-package
cp deployment/upload-pypi/config/.pypirc ~/.pypirc
pip install twine -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install --upgrade twine -i https://pypi.tuna.tsinghua.edu.cn/simple
twine upload --repository testpypi dist/*

rm -rf *.egg-info build dist
