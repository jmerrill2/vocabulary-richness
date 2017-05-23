docker build -t vocab . 

docker ps | grep vocab | awk '{print $1} 

docker run -td vocab 

docker exec 693e396edb3f python vocab.py text.txt

