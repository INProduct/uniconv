import abc


class ABCConv(abc.ABC):

    @abc.abstractmethod
    def import_file(self, path_to_file) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def export_file(self, json_obj, path_to_file, rewrite: bool) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def convert(self) -> object:
        raise NotImplementedError
