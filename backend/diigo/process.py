# Load graphml graph made in yed 
# Process loaded JSON and look for missing connections

import json
from pprint import pprint
import networkx as nx

graph = nx.read_graphml('/home/jarkko/dev/tag-hierarchy-enforcer/backend/diigo/graphs/full-test.graphml')

import itertools
def get_successors(tag):
    '''Find all successors for given tag from graphml graph imported from yed.'''
    search_gen = (node for node in graph.nodes(data=True) if node[1]['label'] == tag)
    try:
        match = next(search_gen)
    except StopIteration:
        return None
    
    successors_res = nx.bfs_successors(graph, match[0])
    successor_ids = list(itertools.chain.from_iterable(successors_res.values()))
    node_tags = nx.get_node_attributes(graph, 'label')
    successor_tags = [node_tags[sid] for sid in successor_ids]
    return successor_tags

class Statistics:
    new_tags = {}

    def add_tag(self, tag):
        current_count = self.new_tags.get(tag)
        if current_count is None:
            self.new_tags[tag] = 1
        else:
            self.new_tags[tag] += 1

    def total_count(self):
        total_count = 0
        for tag in self.new_tags:
            total_count += self.new_tags[tag]
        return total_count

stats = Statistics()

def process_bookmark(bm):
    # what about bm with empty tags
    tags = bm['tags'].split(',')

    # Add all missing tags according to graph
    for tag in tags:
        connections = get_successors(tag)
        if connections is None:
            continue
        for con in connections:
            if con not in tags:
                # add missing connection
                tags.append(con)
                stats.add_tag(con)

    # additional_tags = []

def read_missing():
    with open('jasalt.json') as data_file:
        data = json.load(data_file)

        print('Processing %s bookmarks' % len(data))

        for bm in data:
            process_bookmark(bm)

        print('Found %s missing tags' % stats.total_count())
        pprint(stats.new_tags)

# get_successors('angularjs')
read_missing()

import ipdb; ipdb.set_trace()
