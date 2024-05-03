mkdir -p grasp_tuning

for alpha in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
    for instance in instances/knapsack-50-0.dat instances/bin_packing-50-0.dat instances/mix-50-0.dat ;do
        for i in {1..1}; do
            echo "Tuning $instance $alpha"
            rye run ammm-project --algorithm grasp --alpha $alpha $instance > grasp_tuning/$(basename $instance .dat)-$alpha-$i.out
        done
    done
done