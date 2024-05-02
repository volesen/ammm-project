mkdir -p grasp_tuning

for alpha in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
    for instance in grasp_tuning/*.dat; do
        echo "Tuning $instance $alpha"
        rye run ammm-project --algorithm grasp --alpha $alpha $instance > grasp_tuning/$(basename $instance .dat)-$alpha.out
    done
done