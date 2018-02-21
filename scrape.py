import xlrd
import argparse
import facebook


class Parser:

    def __init__(self, filepath, sheetname):
        self.file = xlrd.open_workbook(filepath).sheet_by_name(sheetname)

    def get_pages(self):
        pass


class Scraper:

    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token=access_token, version='2.7')

    def get(self, page_id, connection_type):
        return self.graph.get_connections(page_id, connection_type)


def main(args):
    scraper = Scraper(args.access_token).get("AlternativeRockNation", "friends")
    parser = Parser(args.filepath, args.sheetname)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Program parses facebook link from xls file and scrape data")

    parser.add_argument('--filepath', help='Path to the xls file with links', required=True)

    parser.add_argument('--sheetname', help='Sheet name in file passed', required=True)

    parser.add_argument('--access_token', default=USER_TOKEN, help='Sheet name in file passed')

    args = parser.parse_args()

    main(args)
