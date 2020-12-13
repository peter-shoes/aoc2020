import logging
f = open('day7.txt','r').read().splitlines()

full_dict = {}
for rule in f:
    rule = rule.split('bags contain')
    holding_bag = rule[0].strip()+' bag'
    contents = rule[1].strip().split(', ')
    contents[-1] = contents[-1][:-1]
    rule_dict = {}
    for sub_bag_raw in contents:
        sub_bag_type = sub_bag_raw[2:]
        if sub_bag_type[-1] == 's':
            sub_bag_type = sub_bag_type[:-1]
        try:
            sub_bag_num = int(sub_bag_raw[:2])
        except:
            sub_bag_num = 0
        rule_dict[sub_bag_type] = sub_bag_num
    full_dict[holding_bag] = rule_dict

list = []
def within(search_bag):
    global sum
    held_by = []
    for holding_bag in full_dict:
        if search_bag in full_dict[holding_bag].keys():
            held_by.append(holding_bag)
            if holding_bag not in list:
                list.append(holding_bag)
    for to_search in held_by:
        within(to_search)

within('shiny gold bag')
# print(len(list))

# ++++++++++++++++
fileContents = f
Bags = {}

for line in fileContents:
    # array of words
    halves = line.strip().split("contain")
    bagName = halves[0].replace(' ', '')[:-4]
    bagContents = halves[1].strip().split(', ')
    cDict = {}
    for content in bagContents:
        content = content.strip().replace('.', '')
        if content != "no other bags":
            contentArray = content.strip().split(' ')
            contentQuantity = contentArray[0]
            contentName = contentArray[1] + contentArray[2]
            cDict[contentName] = contentQuantity
    Bags[bagName] = cDict



childrenArray = []
def getChildren(bag):
    global childrenArray
    children = Bags[bag]
    for child in children:
        n = child
        q = int(children[child])
        for x in range(q):
            childrenArray.append(item for item in getChildren(n))
    return childrenArray

print(len(getChildren("shinygold")))
