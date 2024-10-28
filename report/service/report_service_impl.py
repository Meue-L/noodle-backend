from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report.service.report_service import ResultReportService
from report_completion.repository.report_completion_repository_impl import ResultReportCompletionRepositoryImpl
from report_completion_maintain.repository.report_completion_maintain_repository_impl import \
    ResultReportCompletionMaintainRepositoryImpl
from report_completion_secure.repository.report_completion_secure_repository_impl import \
    ResultReportCompletionSecureRepositoryImpl
from report_completion_total.repository.report_completion_total_repository_impl import \
    ResultReportCompletionTotalRepositoryImpl
from report_feature.repository.report_feature_repository_impl import ResultReportFeatureRepositoryImpl
from report_feature_content.repository.report_feature_content_repository_impl import \
    ResultReportFeatureContentRepositoryImpl
from report_improvement.repository.report_improvement_repository_impl import ResultReportImprovementRepositoryImpl
from report_improvement_content.repository.report_improvement_content_repository_impl import \
    ResultReportImprovementContentRepositoryImpl
from report_modify.repository.report_modify_repository_impl import ResultReportModifyRepositoryImpl
from report_overview.repository.report_overview_repository_impl import ResultReportOverviewRepositoryImpl
from report_skill.repository.report_skill_repository_impl import ResultReportSkillRepositoryImpl
from report_skill_set.repository.result_skill_set_repository_impl import ResultReportSkillSetRepositoryImpl
from report_team.repository.result_team_repository_impl import ResultReportTeamRepositoryImpl
from report_team_member.repository.report_team_member_repository_impl import ResultReportTeamMemberRepositoryImpl
from report_title.repository.report_title_repository_impl import ResultReportTitleRepositoryImpl
from report_usage.repository.report_usage_repository_impl import ResultReportUsageRepositoryImpl


class ResultReportServiceImpl(ResultReportService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()
            cls.__instance.__resultReportModifyRepository = ResultReportModifyRepositoryImpl.getInstance()
            cls.__instance.__resultReportOverviewRepository = ResultReportOverviewRepositoryImpl.getInstance()
            cls.__instance.__resultReportTitleRepository = ResultReportTitleRepositoryImpl.getInstance()
            cls.__instance.__resultReportSkillRepository = ResultReportSkillRepositoryImpl.getInstance()
            cls.__instance.__resultReportSkillSetRepository = ResultReportSkillSetRepositoryImpl.getInstance()
            cls.__instance.__resultReportTeamRepository = ResultReportTeamRepositoryImpl.getInstance()
            cls.__instance.__resultReportTeamMemberRepository = ResultReportTeamMemberRepositoryImpl.getInstance()
            cls.__instance.__resultReportFeatureRepository = ResultReportFeatureRepositoryImpl.getInstance()
            cls.__instance.__resultReportFeatureContentRepository = ResultReportFeatureContentRepositoryImpl.getInstance()
            cls.__instance.__resultReportUsageRepository = ResultReportUsageRepositoryImpl.getInstance()
            cls.__instance.__resultReportImprovementRepository = ResultReportImprovementRepositoryImpl.getInstance()
            cls.__instance.__resultReportImprovementContentRepository = ResultReportImprovementContentRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionRepository = ResultReportCompletionRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionSecureRepository = ResultReportCompletionSecureRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionMaintainRepository = ResultReportCompletionMaintainRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionTotalRepository = ResultReportCompletionTotalRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReport(self, username, **kwargs):
        report = self.__resultReportRepository.create(username)
        modifier = self.__resultReportModifyRepository.create(report, username)
        reportTitle = self.__resultReportTitleRepository.create(report, kwargs['title'])
        reportOverview = self.__resultReportOverviewRepository.createResultReportOverview(kwargs['overview'], report)
        # TODO: Frontend에서 Team 관련 내용 어떻게 넘길지 결정해야 함(AI Client에서는 Team 관련 내용을 생성하지 않기 때문)
        reportTeam = self.__resultReportTeamRepository.create(report)
        reportTeamMember = self.__resultReportTeamMemberRepository.createResultReportTeamMember(kwargs['teamMember'], reportTeam)
        reportSkillSet = self.__resultReportSkillSetRepository.create(report)
        # TODO: techStack 수정 필요(AI Client에서 techStack이 제대로 분할되지 않는 문제 확인, 수정 필요)
        reportSkill = self.__resultReportSkillRepository.create(kwargs['skillList'], reportSkillSet)
        reportFeature = self.__resultReportFeatureRepository.createResultReportFeature(report)
        reportFeatureContent = self.__resultReportFeatureContentRepository.createResultReportFeatureContent(kwargs['featureList'], reportFeature)
        reportUsage = self.__resultReportUsageRepository.createResultReportUsage(report, kwargs['usage'])
        reportImprovement = self.__resultReportImprovementRepository.createResultReportImprovement(report)
        reportImprovementContent = self.__resultReportImprovementContentRepository.createResultReportImprovementContent(report, kwargs['improvement'])
        reportCompletion = self.__resultReportCompletionRepository.createResultReportCompletion(report)
        reportCompletionSecure = self.__resultReportCompletionSecureRepository.createResultReportCompletionSecure(
            reportCompletion, kwargs['scoreList'][0][0], kwargs['scoreList'][0][1])
        reportCompletionMaintain = self.__resultReportCompletionMaintainRepository.createResultReportCompletionMaintain(
            reportCompletion, kwargs['scoreList'][1][0], kwargs['scoreList'][1][1])
        reportCompletionTotal = self.__resultReportCompletionTotalRepository.createResultReportCompletionTotal(
            reportCompletion, kwargs['scoreList'][2][0], kwargs['scoreList'][2][1])

        return report

    def list(self):
        resultReportList = self.__resultReportRepository.getAllResultReportList()
        resultReportTitleList = self.__resultReportTitleRepository.getAllResultReportTitleList()

        result = []
        for i in range(len(resultReportList)):
            result.append([resultReportTitleList[i].title, resultReportList[i].creator, resultReportList[i].createdDate])

        return result
