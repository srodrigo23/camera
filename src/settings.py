from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Settings():
    
    def __init__(self):
        self.path_file = '../config.yaml'
        self.read_file()
    
    def read_file(self):
        with open(self.path_file, 'r') as content:
            self.data = load(content, Loader=Loader)
    
    def get_frame_rate(self):
        return self.data['frame_rate']

    def get_ip_addres(self):
        return self.data['ip']
        
    def get_resolution(self):
        return (self.data['resolution'][0], self.data['resolution'][1])
    
    def get_source(self):
        return self.data['src']
    
    def set_source(self, src):
        self.data['src'] = src
        with open(self.path_file, 'w') as edit:
            dump(self.data, edit)