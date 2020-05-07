# simpleflaskapp

update travis
git add .
git commit -m "travis.ci"
git push

docker build -t nguyenanht/simpleflaskapp:latest .


docker run -it -p 80:80 nguyenanht/simpleflaskapp:latest