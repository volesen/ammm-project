mkdir -p grasp_tuning

for alpha in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
    for i in {1..5}; do
        instance="instances/mix-50-1.dat"
        echo "Tuning $instance $alpha"
        rye run ammm-project --algorithm grasp --alpha $alpha $instance --max-time 300 --max-time-since-improvement 60 > grasp_tuning/$(basename $instance .dat)-$alpha-$i.out
    done
done