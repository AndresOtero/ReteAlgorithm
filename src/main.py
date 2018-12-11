import src.Alpha.AlphaNetwork

from src.Alpha.AlphaNetwork import AlphaNetwork
from src.Alpha.WME import WME
from src.FowardChain import FowardChain
from src.Knowledge.KnowledgeParser import KnowledgeParser
from src.Rules.RulesParser import RulesParser

rulesTest = RulesParser.getRules("./InputFiles/rulesTest.txt")
rules = RulesParser.getRules("./InputFiles/rules.txt")
knowledgeTest = KnowledgeParser.getKnowledges("./InputFiles/knowledgeTest.txt")
knowledgeInexperto = KnowledgeParser.getKnowledges("./InputFiles/knowledgesInexperto.txt")
knowledgeExperto = KnowledgeParser.getKnowledges("./InputFiles/knowledgesExperto.txt")

# fwdChain = FowardChain(rules=rulesTest, knowledge=knowledgeTest)
# fwdChain.runReteAlgorithm()
# print(knowledgeTest)
# fwdChain = FowardChain(rules=rules, knowledge=knowledgeInexperto)
# fwdChain.runReteAlgorithm()
# print(knowledgeInexperto)
fwdChain = FowardChain(rules=rules, knowledge=knowledgeExperto)
fwdChain.runReteAlgorithm()
#print(knowledgeExperto)
# fwdChain.printUsedRules()

alphaNetwork = AlphaNetwork()
for key in knowledgeExperto.getKeys():
    wme=WME(key,knowledgeExperto.getSymbol(key),knowledgeExperto.getValue(key))
    alphaNetwork.addWME(wme)
for rule in rules:
    alphaNetwork.addProduction(rule)

print(alphaNetwork.printWorkinMemory())
