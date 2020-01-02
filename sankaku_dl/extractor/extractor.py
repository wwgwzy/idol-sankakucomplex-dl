import re

metadata = {}

with open('response.txt', 'r') as response_f:
    response_content = response_f.read()

    pattern_vote = re.compile(r'<li>Vote Average: <span id=post-score-1>(.*?)</span></li>\s<li>Vote Count: <span id=post-vote-count-1>(.*?)</span></li>')
    pattern_favorby = re.compile(r'<a href="/user/show/\d+">(.*?)</a>')
    pattern_favorbymore = re.compile(r'''<a href="#" onclick="$('remaining-favs').show(); $('remaining-favs-link').hide(); return false;">(\d+) others</a>''')
    pattern_tag = re.compile(r'<li class=tag-type-.*?><a.*?>(.*?)</a>.*?</li>')

    vote_data = pattern_vote.search(response_content)

    if vote_data:
        metadata['vote_average'] = vote_data.group(1)
        metadata['vote_count'] = vote_data.group(2)

    favorby0 = pattern_favorby.findall(response_content)
    if favorby0:
        favorby = len(favorby0)
        favorby1 = pattern_favorbymore.search(response_content)
        if favorby1:
            favorby += int(favorby1)
    else:
        favorby = 0
    metadata['favorby'] = favorby

    metadata['tags'] = pattern_tag.findall(response_content)
    print(metadata)
