for i in {1..41}
do
    if [ $i -lt 10 ]; then
        touch "0$i.txt"
    else
        touch "$i.txt"
    fi
    
done