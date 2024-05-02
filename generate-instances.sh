NUM_INSTANCES_PER_SIZE=3

mkdir -p instances

for algorithm in "knapsack" "bin_packing" "mix"; do
    for size in 50 100 200; do
        for i in $(seq 1 $NUM_INSTANCES_PER_SIZE); do
            rye run generate-instance mix $size > instances/$algorithm-$size-$i.dat
        done
    done
done