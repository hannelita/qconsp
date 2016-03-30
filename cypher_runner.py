import inspect, os
import re
from py2neo import Graph, authenticate

class CypherRunner(object):
  
  def __init__(self):
    self.queries_file = open('cypher_', 'r+')
    self.graph = Graph()

  def run(self):
    tx = self.graph.cypher.begin()
    for line in self.queries_file:
      constraint_match = re.match("CREATE CONSTRAINT ON (.*)", line)
      if(constraint_match):
        self.graph.cypher.execute(line)
      else:
        tx.append(line)
    tx.commit()

runner = CypherRunner()
runner.run()