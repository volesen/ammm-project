# Greedy
mkdir -p cplex-benchmarks

echo "CPLEX binary"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
   /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/binary.mod $instance > cplex-benchmarks/binary-$(basename $instance .dat).out
done

echo "CPLEX bigM"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM.mod $instance > cplex-benchmarks/bigM-$(basename $instance .dat).out
done

echo "CPLEX bigM1"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM1.mod $instance > cplex-benchmarks/bigM1-$(basename $instance .dat).out
done

echo "CPLEX bigM2"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM2.mod $instance > cplex-benchmarks/bigM2-$(basename $instance .dat).out
done

echo "CPLEX bigM3"
for instance in instances/*-2.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM3.mod $instance > cplex-benchmarks/bigM3-$(basename $instance .dat).out
done

