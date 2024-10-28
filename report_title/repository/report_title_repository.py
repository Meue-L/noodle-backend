from abc import abstractmethod, ABC


class ResultReportTitleRepository(ABC):
    @abstractmethod
    def create(self, report, title):
        pass

    @abstractmethod
    def getAllResultReportTitleList(self):
        pass