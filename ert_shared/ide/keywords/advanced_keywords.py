from ert_shared.ide.keywords.definitions import KeywordDefinition, ConfigurationLineDefinition, PathArgument, StringArgument
from ert_shared.ide.keywords.definitions.proper_name_argument import ProperNameArgument


class AdvancedKeywords(object):
    def __init__(self, ert_keywords):
        super(AdvancedKeywords, self).__init__()
        self.group = "Advanced"

        ert_keywords.addKeyword(self.addDefine())
        ert_keywords.addKeyword(self.addSchedulePredictionFile())

    def addDefine(self):
        define = ConfigurationLineDefinition(keyword=KeywordDefinition("DEFINE"),
                                             arguments=[ProperNameArgument(),
                                                        StringArgument(rest_of_line=True,allow_space=True)],
                                             documentation_link="keywords/define",
                                             required=False,
                                             group=self.group)
        return define



    def addSchedulePredictionFile(self):
        schedule_prediction_file = ConfigurationLineDefinition(keyword=KeywordDefinition("SCHEDULE_PREDICTION_FILE"),
                                                      arguments=[PathArgument()],
                                                      documentation_link="keywords/schedule_prediction_file",
                                                      required=False,
                                                      group=self.group)
        return schedule_prediction_file

