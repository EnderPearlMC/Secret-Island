import yaml


# class which Manage every file : Create / Read
class FileManager:

    # writes file with a given path and some datas given
    # @param path : Path of the file
    # @param data : data to write into the file
    def write_file(self, path, data):
        with open(path, 'w') as stream:
            yaml.dump(data, stream, default_flow_style=False, allow_unicode=True)
            stream.flush()
            stream.close()

    # reads file with a path given and returns an array with infos
    # @param path : Path of the file
    def read_file(self, path):
        with open(path, 'r') as outfile:
            data_loaded = yaml.safe_load(outfile)
            outfile.flush()
            outfile.close()
            return data_loaded
