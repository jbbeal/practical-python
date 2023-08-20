class FormatError(ValueError):
    pass

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
        

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        hRow = ' '.join([ f'{h: <15}' for h in headers])
        print(hRow)
        print(' '.join(['-' * 15] * len(headers)))
        

    def row(self, rowdata):
        print(' '.join([ f'{cell: >15}' for cell in rowdata]))

class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HtmlTableFormatter(TableFormatter):
    def headings(self, headers):
        print(f"<tr>{''.join([ f'<th>{h}</th>' for h in headers ])}</tr>")

    def row(self, rowdata):
        print(f"<tr>{''.join([ f'<td>{c}</td>' for c in rowdata ])}</tr>")

def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CsvTableFormatter()
    elif name == 'html':
        return HtmlTableFormatter()
    else:
        raise FormatError(f"Unknown formatter {name}")


def print_table(rowdata: list, columns: list, formatter):
    formatter.headings(columns)
    for r in rowdata:
        toprint = [ getattr(r, colname) for colname in columns ]
        formatter.row(toprint)
