mkdir -p grasp_tuning

for alpha in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
    for instance in instances/*-50-1.dat; do
        for i in {1..10}; do
            echo "Tuning $instance $alpha"
            ammm-project --algorithm grasp --alpha $alpha $instance > grasp_tuning/$(basename $instance .dat)-$alpha-$i.out
        done
    done
done