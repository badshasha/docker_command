docker run appnameorid  == > docker-compose up

docker build .
docker run appnameorid  == >  docker-compose up --build


# run background
docker-compose up -d  

# stop process 
docker-compose down 


# build docker file with docker file name
docker build -f dockerfile.dev .