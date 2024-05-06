# Greedy
mkdir -p benchmarks_cplex

echo "Cplex bigM2"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM2.mod $instance > benchmarks_cplex/bigM2-$(basename $instance .dat).out
done


# echo "Cplex bigM"
# for instance in instances/*-2.dat; do
#     echo "Benchmarking $instance"
#     /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM.mod $instance > benchmarks_cplex/bigM-$(basename $instance .dat).out
# done

# # Run Cplex algorithm on the input files in the input directory
# echo "Cplex binary"
# for instance in instances/*-2.dat; do
#     echo "Benchmarking $instance"
#    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/binary.mod $instance > benchmarks_cplex/binary-$(basename $instance .dat).out
# done

# echo "Cplex bigM1"
# for instance in instances/*-2.dat; do
#     echo "Benchmarking $instance"
#     /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM1.mod $instance > benchmarks_cplex/bigM1-$(basename $instance .dat).out
# done
