import xml.dom.minidom as minidom
import xml.sax


class Reader(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.data_table = []
        self.client_data = []
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

    def endElement(self, name):
        if self.current == "asdjda":
            self.client_data.append(self.name)
        elif self.current == "jjfjnfe":
            self.client_data.append(self.account_number)

        if len(self.client_data) == 7:
            self.data_table.append(tuple(self.client_data))
            self.client_data = []

        self.current = ""


class Writer:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.dom_tree = minidom.Document()
        self.rows = []

    def create_xml_client(self, data):
        client = self.dom_tree.createElement("client")

        for value in data:
            temp_child = self.dom_tree.createElement(value)
            client.appendChild(temp_child)

            node_text = self.dom_tree.createTextNode(data[value].strip())
            temp_child.appendChild(node_text)

        self.rows.append(client)

    def create_xml_file(self):
        pass_table = self.dom_tree.createElement("pass_table")

        for client in self.rows:
            pass_table.appendChild(client)

        self.dom_tree.appendChild(pass_table)

        self.dom_tree.writexml(open(self.file_name, 'w'),
                               indent="  ",
                               addindent="  ",
                               newl='\n')
        self.dom_tree.unlink()


if __name__ == '__main__':
    writer = Writer('test.xml')
    writer.create_xml_client({
        "book_name": "book1",
        "author_name": "name1",
        "author_last_name": "last name 1",
        "author_patronymic": "oqoqoqo",
        "publisher": "pub1",
        "amount_of_volumes": "1212",
        "circulation": "101000101",
    })
    writer.create_xml_client({
        "book_name": "book2",
        "author_name": "name2",
        "author_last_name": "last name 2",
        "author_patronymic": "oqoqoqo",
        "publisher": "pub2",
        "amount_of_volumes": "1112121212",
        "circulation": "99999999",
    })
    writer.create_xml_client({
        "book_name": "book3",
        "author_name": "name3",
        "author_last_name": "last name 3",
        "author_patronymic": "yuuuuyuu",
        "publisher": "pub3",
        "amount_of_volumes": "0",
        "circulation": "0",
    })
    writer.create_xml_file()
    # handler = Reader()
    # parser = xml.sax.make_parser()
    # parser.setContentHandler(handler)
    # parser.parse('test.xml')
    # print(handler.data_table)
