mkdir -p grasp_tuning

for alpha in 0.9 0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99 1.00; do
    for instance in instances/*-50-1.dat; do
        for i in {1..10}; do
            echo "Tuning $instance $alpha"
            ammm-project --algorithm grasp --alpha $alpha $instance > grasp_tuning/$(basename $instance .dat)-$alpha-$i.out
        done
    done
done