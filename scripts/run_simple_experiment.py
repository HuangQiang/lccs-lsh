from dataset_config import MNIST
from method_config import LCCS
import os
import sys
from run_ground_truth import run_ground_truth
from run_time_recall import run_alg, create_results_folder


if __name__ == '__main__':
    datasets = [MNIST()]
    run_ground_truth(datasets=datasets, dist='l2')

    create_results_folder()
    run_alg([LCCS()], [MNIST()], 'l2')