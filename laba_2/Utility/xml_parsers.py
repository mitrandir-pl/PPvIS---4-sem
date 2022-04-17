import xml.dom.minidom as minidom
import xml.sax


class Reader(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.data_table = []
        self.book_data = []
        self.parser = xml.sax.make_parser()

    def startElement(self, name, attrs):
        self.current = name
        if name == "book":
            pass

    def characters(self, content):
        if self.current == "book_name":
            self.book_name = content
        elif self.current == "author_name":
            self.author_name = content
        elif self.current == "author_last_name":
            self.author_last_name = content
        elif self.current == "author_patronymic":
            self.author_patronymic = content
        elif self.current == "publisher":
            self.publisher = content
        elif self.current == "amount_of_volumes":
            self.amount_of_volumes = content
        elif self.current == "circulation":
            self.circulation = content
        elif self.current == "summary_volumes":
            self.summary_volumes = content
    def endElement(self, name):
        if self.current == "book_name":
            self.book_data.append(self.book_name)
        elif self.current == "author_name":
            self.book_data.append(self.author_name)
        elif self.current == "author_last_name":
            self.book_data.append(self.author_last_name)
        elif self.current == "author_patronymic":
            self.book_data.append(self.author_patronymic)
        elif self.current == "publisher":
            self.book_data.append(self.publisher)
        elif self.current == "amount_of_volumes":
            self.book_data.append(self.amount_of_volumes)
        elif self.current == "circulation":
            self.book_data.append(self.circulation)
        elif self.current == "summary_volumes":
            self.book_data.append(self.summary_volumes)
        if len(self.book_data) == 8:
            self.data_table.append(tuple(self.book_data))
            self.book_data = []

        self.current = ""


class Writer:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.dom_tree = minidom.Document()
        self.rows = []

    def create_xml_book(self, data):
        book = self.dom_tree.createElement("book")

        for value in data:
            temp_child = self.dom_tree.createElement(value)
            book.appendChild(temp_child)

            node_text = self.dom_tree.createTextNode(str(data[value]))
            temp_child.appendChild(node_text)

        self.rows.append(book)

    def create_xml_file(self):
        pass_table = self.dom_tree.createElement("pass_table")

        for book in self.rows:
            pass_table.appendChild(book)

        self.dom_tree.appendChild(pass_table)

        self.dom_tree.writexml(open(self.file_name, 'w'),
                               indent="  ",
                               addindent="  ",
                               newl='\n')
        self.dom_tree.unlink()
