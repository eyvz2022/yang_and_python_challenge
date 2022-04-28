from jinja2 import Environment, FileSystemLoader


class Config:

    def __init__(self):
        self.file_loader = FileSystemLoader("./TASK2/jinja")
        self.env = Environment(loader=self.file_loader, trim_blocks=True, lstrip_blocks=True)

    def create_interface_config(self, interface_info_dict={}):
        template = self.env.get_template("interface.j2")
        output = template.render(dict_item=interface_info_dict)

        return output
