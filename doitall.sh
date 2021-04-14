rm -rf dist/*
cd docs/
make html
cd ..
python3 -m build
twine upload dist/* 
git add -A
git commit -a
git push

