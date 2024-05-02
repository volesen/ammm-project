# Greedy

# Run the greedy algorithm on the input files in the input directory
# and write the output to the output directory

mkdir -p benchmarks

# echo "Greedy"
# for instance in instances/*.dat; do
#     echo "Benchmarking $instance"
#     rye run ammm-project --algorithm greedy $instance > benchmarks/greedy-$(basename $instance .dat).out
# done

# echo "Greedy with local search"
# # Run `greedy_with_local_search` algorithm on the input files in the input directory
# for instance in instances/*.dat; do
#     echo "Benchmarking $instance"
#     rye run ammm-project --algorithm greedy_with_local_search $instance > benchmarks/greedy_with_local_search-$(basename $instance .dat).out
# done


# Run Cplex algorithm on the input files in the input directory
echo "Cplex binary"
for instance in instances/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/binary.mod $instance > benchmarks/cplex-$(basename $instance .dat).out
done

echo "Cplex bigM"
for instance in instances/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM.mod $instance > benchmarks/cplex-$(basename $instance .dat).out
done

echo "Cplex bigM1"
for instance in instances/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM1.mod $instance > benchmarks/cplex-$(basename $instance .dat).out
done