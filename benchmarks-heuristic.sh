# Greedy
mkdir -p benchmarks

echo "Greedy"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    rye run ammm-project --algorithm greedy $instance > benchmarks/greedy-$(basename $instance .dat).out
done

echo "Greedy with local search"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    rye run ammm-project --algorithm greedy_with_local_search $instance > benchmarks/greedy_with_local_search-$(basename $instance .dat).out
done
