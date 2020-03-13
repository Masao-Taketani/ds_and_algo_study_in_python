import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", default="eval_data")
args = parser.parse_args()

ranges = [10, 100, 1_000, 10_000, 100_000]

for i, r in enumerate(ranges):
    with open(args.dir + "/data" + str(i+1) + ".pkl", "wb") as f:
        pickle.dump(list(range(r)), f)
print("creating pkl files is done.")
