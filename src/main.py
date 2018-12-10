from src.Condition.Condition import GreaterOrEqual, LesserOrEqual
from src.FowardChain import FowardChain
from src.Knowledge.KnowledgeParser import KnowledgeParser
from src.Knowledge.Knowledge import Knowledge
from src.Rules.RulesParser import RulesParser
from src.Rules.Rule import Rule

rulesTest=RulesParser.getRules("./InputFiles/rulesTest.txt")
rules=RulesParser.getRules("./InputFiles/rules.txt")
knowledgeTest=KnowledgeParser.getKnowledges("./InputFiles/knowledgeTest.txt")
knowledgeInexperto=KnowledgeParser.getKnowledges("./InputFiles/knowledgesInexperto.txt")
knowledgeExperto=KnowledgeParser.getKnowledges("./InputFiles/knowledgesExperto.txt")

# fwdChain = FowardChain(rules=rulesTest, knowledge=knowledgeTest)
# fwdChain.runReteAlgorithm()
# print(knowledgeTest)
# fwdChain = FowardChain(rules=rules, knowledge=knowledgeInexperto)
# fwdChain.runReteAlgorithm()
# print(knowledgeInexperto)
fwdChain = FowardChain(rules=rules, knowledge=knowledgeExperto)
fwdChain.runReteAlgorithm()
print(knowledgeExperto)
fwdChain.printUsedRules()