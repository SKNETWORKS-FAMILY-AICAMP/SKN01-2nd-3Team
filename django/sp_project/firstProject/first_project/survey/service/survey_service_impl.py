from survey.repository.survey_repository_impl import SurveyRepositoryImpl
from survey.service.survey_service import SurveyService


class SurveyServiceImpl(SurveyService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__surveyRepository = SurveyRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createSurvey(self, surveyData):
        return self.__surveyRepository.create(surveyData)

