from abc import abstractmethod, ABC


class ResultReportCompletionSecureRepository(ABC):
    @abstractmethod
    def createResultReportCompletionSecure(self, completion, score, detail):
        pass