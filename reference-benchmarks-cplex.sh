mkdir -p reference-benchmarks

echo "Cplex binary"
for instance in reference/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/binary.mod $instance > reference-benchmarks/binary-$(basename $instance .dat).out
done

echo "Cplex bigM"
for instance in reference/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM.mod $instance > reference-benchmarks/bigM-$(basename $instance .dat).out
done

echo "Cplex bigM1"
for instance in reference/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM1.mod $instance > reference-benchmarks/bigM1-$(basename $instance .dat).out
done

echo "Cplex bigM2"
for instance in reference/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM2.mod $instance > reference-benchmarks/bigM2-$(basename $instance .dat).out
done

echo "Cplex bigM3"
for instance in reference/*.dat; do
    echo "Benchmarking $instance"
    /Applications/CPLEX_Studio2211/opl/bin/arm64_osx/oplrun opl/bigM3.mod $instance > reference-benchmarks/bigM3-$(basename $instance .dat).out
done