NUM_INSTANCES_PER_SIZE=3

mkdir -p instances

for algorithm in "knapsack" "bin_packing" "mix"; do
    for size in 50 100 200; do
        for i in $(seq 1 $NUM_INSTANCES_PER_SIZE); do
            echo "Generating instance $algorithm $size $i"

            rye run generate-instance --algorithm $algorithm $size > instances/$algorithm-$size-$i.dat
        done
    done
done