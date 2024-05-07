# Greedy
mkdir -p benchmarks_cplex

echo "CPLEX binary"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
   /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/binary.mod $instance > benchmarks_cplex/binary-$(basename $instance .dat).out
done

echo "CPLEX bigM"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM.mod $instance > benchmarks_cplex/bigM-$(basename $instance .dat).out
done

echo "CPLEX bigM1"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM1.mod $instance > benchmarks_cplex/bigM1-$(basename $instance .dat).out
done

echo "CPLEX bigM2"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM2.mod $instance > benchmarks_cplex/bigM2-$(basename $instance .dat).out
done

echo "CPLEX bigM3"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM3.mod $instance > benchmarks_cplex/bigM3-$(basename $instance .dat).out
done

