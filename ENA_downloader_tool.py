from ENA_Downloader import ENA_Downloader




def main():
    obj = ENA_Downloader("PRJEB26509")
    obj.start_downloading()

if __name__ == "__main__":
    main()