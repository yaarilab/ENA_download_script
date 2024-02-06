from ENA_Downloader import ENA_Downloader
import argparse


def main(project_name):
    obj = ENA_Downloader(project_name)
    obj.start_downloading()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('project_name', type=str, help='Name of the project')
    args = parser.parse_args()
    main(args.project_name)