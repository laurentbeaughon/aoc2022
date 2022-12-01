import argparse


def main(args):
    problem = getattr(__import__(f'day_{args.day}', fromlist=['main']), 'main')
    problem(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', '-d', help= "problem day", required=True)
    parser.add_argument('--data_file', '-f', help= "input_data_file", required=True)
    parser.add_argument('--verbose', '-v', action='store_true', help='display more logs')
    args = parser.parse_args()

    main(args)