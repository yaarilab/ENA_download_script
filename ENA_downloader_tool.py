from ENA_Downloader import ENA_Downloader
import argparse


def main(project_name, use_submitted):
    if use_submitted.lowwer() == 'false':
        use_submitted = False
    else:
        use_submitted = True
        
    obj = ENA_Downloader(project_name, use_submitted)
    obj.start_downloading()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('project_name', type=str, help='Name of the project')
    parser.add_argument('use_submitted', type=str, help='True or False for using submmited files')
    args = parser.parse_args()
    main(args.project_name, args.use_submitted)