docker build -t vocab . 

docker ps | grep vocab | awk '{print $1}' 

docker run -td -v "$(pwd):/opt/src" vocab 

docker exec 6abb54af1e0e python /opt/src/vocab.py opt/src/bom.txt


