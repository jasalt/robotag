# Process loaded JSON

import json
from pprint import pprint

graph = {'python': ['programming', 'programming language'],
         'programming': ['software development'],
         'startup': ['business', 'company'],
         'clojure': ['programming language', 'lisp', 'functional programming'],
         'programming language': ['programming'],
         'arduino': ['embedded programming'],
         'library': ['programming'],
         'embedded programming': ['programming'],
         'dj': ['music']}

shorthands = {'fp': 'functional programming'}

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
        connections = graph.get(tag)
        if connections is None:
            continue
        for con in connections:
            if con not in tags:
                tags.append(con)
                stats.add_tag(con)
                
    # additional_tags = []

with open('jasalt.json') as data_file:
    data = json.load(data_file)

print('Processing %s bookmarks' % len(data))

for bm in data:
    process_bookmark(bm)

print('Found %s missing tags' % stats.total_count())

pprint(stats.new_tags)

