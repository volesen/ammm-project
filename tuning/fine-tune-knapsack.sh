mkdir -p grasp_tuning

for alpha in 0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99; do
    for i in {1..5}; do
        instance="instances/knapsack-50-1.dat"
        echo "Finetune $instance $alpha"
        rye run ammm-project --algorithm grasp --alpha $alpha $instance > grasp_tuning/$(basename $instance .dat)-$alpha-$i.out
    done
done