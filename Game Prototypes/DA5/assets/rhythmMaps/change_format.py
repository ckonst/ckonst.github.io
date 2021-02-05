import json

with open('beatmap.json', 'r') as f:
    beatmap = json.load(f)
    
onsets = beatmap['onsets']
with open('rhythmMap1.txt', 'w+') as f:
    f.write('\n'.join(map(str, onsets)))