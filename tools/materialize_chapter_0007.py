"""Materialize the reviewed Chapter 7 reconstruction from immutable source witnesses."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'h': 'http://www.w3.org/1999/xhtml'}
MTL = ROOT / 'source/chapters/chapter-007.xhtml'
KOREAN = ROOT / 'source/korean/chapters/007.txt'
MTL_SHA = '857afae47af7eab43b52d7a578664446df0a711bfdb2d31e9184ea9d80d440cb'
KOREAN_SHA = 'e2162bd21803c27643465970557aac3ffe7bcede3460982362cc841e3295a7f4'

FINAL = [
'Vikir knew Hugo’s personality well.',
'‘…A lizard.’',
'His blood ran so cold he could have been mistaken for a cold-blooded reptile.',
'At heart, Hugo cared only about the future of the family and his own achievements.',
'To him, everyone but himself was a tool—especially those meant to serve as weapons.',
'Weapons existed to harm others. The notion of a weapon independently showing mercy or hesitation was unthinkable.',
'And naturally, the more poison a weapon carried, the better.',
'So there was nothing strange about Hugo’s gaze toward Vikir gradually growing warmer with satisfaction.',
'“So. You think you’re innocent?”',
'“Yes. My brothers were the ones in the wrong.”',
'“What did they do wrong?”',
'“They were weak.”',
'In this world, the strong were respected and the weak were sinners.',
'Wasn’t that Baskerville?',
'Vikir’s answer struck straight at the heart of the family creed.',
'A lion devouring a deer was not committing a sin.',
'The strong defeating the weak was the law of nature; calling it a matter of crime and punishment was merely the absurd protest of the weak.',
'That lesson had been driven into Vikir throughout childhood by tutors whose teachings ultimately came from Hugo.',
'‘…So whining that my brothers bullied me first would have been useless.’',
'Before his regression, Vikir had tried to explain his innocence and his brothers’ wrongdoing like any ordinary child, only for Hugo to regard him with even greater contempt.',
'…And that gaze had not changed even at the very end, when Vikir knelt before the guillotine.',
'Meanwhile—',
'Hugo Le Baskerville.',
'He clasped his hands before his mouth.',
'Then he spoke in a low, subdued voice.',
'“Your brothers came here before you.”',
'“…”',
'“They said that, as your older brothers, they would forgive you.”',
'Vikir did not bother answering.',
'Having spent so long at Hugo’s side in his previous life, he could guess what had happened.',
'The triplets had probably failed to give Hugo the answer he wanted and only irritated him further.',
'‘They must have been terrified. And “forgiveness”? They probably begged to be kept away from me.’',
'Vikir answered in an emotionless voice.',
'“Growing older costs nothing, after all.”',
'“…”',
'Hugo paused for a moment.',
'Then he gave a faint laugh.',
'“Heh. True. Even this father had to work hard to become the eldest son when I became patriarch.”',
'It was strange enough just to hear Hugo refer to himself as “this father.”',
'‘He worked hard to become the eldest son? Is that something effort can accomplish?’',
'Vikir pondered the unfamiliar remark for a moment before understanding.',
'Hugo had risen to the patriarch’s seat by killing all of his older brothers.',
'‘I always thought only the eldest son could inherit the family. So even the eldest son can be made afterward.’',
'Once again, Vikir was reminded of the true nature of Baskerville.',
'Hugo asked another question.',
'“Whatever the circumstances, your older brothers reached out first and offered forgiveness. Do you still feel no guilt?”',
'“…”',
'Vikir looked at Hugo in silence for a moment.',
'The warm eyes of a father—something Vikir had never once received from him in his previous life.',
'But a heart already frozen solid could never be melted by such faint warmth.',
'…It had happened sometime before his regression.',
'The last surviving daughter of a family exterminated by Baskerville had once come to see Hugo in person.',
'Years later, after becoming a nun, she had come to him with the words, “I forgive you.”',
'Back then, Hugo had answered:',
'“Forgiveness is nothing but an excuse used by the weak who lack the power to take revenge.”',
'Vikir repeated those exact words now, changing only the honorifics.',
'Hugo’s eyes widened at once.',
'“Hahahahahaha—!”',
'His laughter rang through the room loudly enough to shake the windows.',
'Hugo leaned back in his chair, looking utterly satisfied.',
'“Now that’s a child of mine. It’s like looking at my eldest son.”',
'It was the first time Vikir had ever seen Hugo show such strong emotion toward one of his children.',
'Their conversation ended there.',
'“Barrymore.”',
'Hugo called for the butler, his face returning to its usual impassive expression.',
'But a trace of warmth still lingered in his voice.',
'“Give Vikir the key to the food storage.”',
'Barrymore’s eyes widened.',
'Baskerville children ate the same food every day until they turned fifteen.',
'Water and haggis.',
'The haggis was a dense mash of meat and offal from various animals mixed with a little vegetable matter—extremely high in calories and nutrients, but salty and thoroughly unpleasant.',
'The supply was unlimited and kept impeccably hygienic, but taste was clearly not a concern.',
'That was why Baskerville children went wild for sweets and chocolate whenever good grades earned them a reward.',
'It was an inexpensive system for motivating children, fostering competition, and ultimately producing capable members of Baskerville.',
'Knowing that, Hugo asked Vikir a question.',
'“Is there any snack you want?”',
'Vikir answered at once with the innocent smile of an eight-year-old.',
'“Chocolate!”',
'Hugo watched him and nodded.',
'‘He probably thinks I’m finally acting my age.’',
'Barrymore smiled as well, as though thinking that a child was still a child after all.',
'Hugo gestured to Barrymore.',
'“Take him to the food storage and let him have as much chocolate as he wants. Don’t let him get too greedy—only what he can carry.”',
'“Yes, my lord.”',
'Barrymore took Vikir by the hand and headed for the door.',
'Just as they were leaving—',
'Hugo spoke with his back to the door.',
'“Do well on this midterm evaluation.”',
'Such encouragement from Hugo was rare.',
'What followed was even more unusual.',
'“…Don’t lose to the direct line.”',
'At those words, Vikir’s eyes glowed blood-red.',
'Like two suns.',
'“We’re here, young master.”',
'Barrymore led Vikir to the kitchen on the outskirts of Fang Castle.',
'Several chefs followed politely behind them.',
'The food storage deep underground was always cool.',
'Cold air seeping through gaps in the stone met the warm air entering through the open door, forming a faint haze of condensation.',
'Barrymore raised a lantern to illuminate the interior of the storage room.',
'The same task could have been handled with mana, but the old butler performed it himself without the slightest awkwardness.',
'Vikir stepped inside.',
'Ingredients for the family’s Guardian Knights, relatives over fifteen, and other servants were neatly arranged throughout the room.',
'“The candies and jellies are over here, young master. If there’s anything you’d like prepared separately, I can have the chefs make it.”',
'Vikir shook his head at Barrymore’s kind offer.',
'“Chocolate is enough.”',
'Barrymore looked down at him with a trace of pity.',
'How badly must the boy have craved chocolate?',
'“Once you’re over fifteen, you’ll be able to eat whatever you like.”',
'It was sincere consolation.',
'The chefs behind them, watching the butler’s expression, began taking the finest chocolates from the shelves.',
'“These are the finest chocolates, favored by the gourmets of the Morgue Family. We managed to obtain several boxes this time. They say nuts from the south and honey from the west deepen the flavor even further.”',
'But Vikir shook his head.',
'“I don’t need anything processed.”',
'“…Pardon?”',
'Barrymore and the chefs stared at him in confusion. Vikir explained.',
'“I need raw cacao beans. A variety with an extremely intense flavor.”',
'Barrymore furrowed his brow.',
'Cacao beans were the raw material used to make chocolate.',
'But unprocessed cacao beans were not sweet at all. They were unbearably bitter.',
'And a variety prized for an especially intense flavor would be more bitter still.',
'After hearing the chefs’ report, Barrymore spoke.',
'“Hmm. An especially intense variety… there is one. Long ago, the patriarch personally led the family elders against the barbarians on the western frontier, then cleared the vast jungle there into farmland. A local specialty called the ‘Bloody Bean’ is so concentrated that a single bean can make one hundred liters of chocolate.”',
'“Good. Bring it.”',
'“How much should we bring?”',
'“All you have.”',
'At Vikir’s order, the chefs immediately moved.',
'Before long, one returned carrying a small leather pouch.',
'The pouch, barely large enough to hold two fists, was filled with vivid red cacao beans.',
'There were easily more than a hundred of them.',
'These were Bloody Beans. Each bean was concentrated enough to make roughly one hundred liters of chocolate.',
'Vikir bit into one as a test.',
'Crunch!',
'The reaction in his mouth was immediate.',
'The astringent bitterness was so intense that his entire tongue went numb.',
'Vikir spat out the bean and nodded in satisfaction.',
'Barrymore nodded as well.',
'‘He really does love chocolate.’',
'Hugo had told them to let Vikir take as much food as he could carry, so there was no problem with him taking all of the cacao beans.',
'But this single pouch held enough concentrated cacao to make roughly ten thousand liters of chocolate.',
'Barrymore marveled at the greed and foresight of an eight-year-old.',
'At this rate, Vikir could spend the rest of his life indulging in his beloved chocolate.',
'“Young master, shall we process these and send them to your room?”',
'…But—',
'Vikir gave an answer that left everyone puzzled.',
'“No processing. They’re fine as they are.”',
'Apparently, he had not taken them to eat.'
]

SPECIFIC_REASONS = {
4:'Repair historical audit ED-00072 and restore Hugo’s self/family-focused utilitarian characterization from Korean.',
7:'Use the Korean weapon-poison metaphor rather than the MTL’s altered quantity-of-weapons reading.',
13:'Restore the explicit strong-respected/weak-sinner half of the Baskerville creed.',
28:'Clarify that the triplets offered forgiveness in their role as Vikir’s older brothers.',
32:'Restore Korean’s fuller implication that the frightened triplets likely wanted distance from Vikir.',
34:'Reconstruct the age/eldest wordplay using the supplied Korean age line plus the later callback as narrow corroboration.',
38:'Preserve Hugo’s self-reference as “this father” and the dark claim that he worked to become the eldest son.',
42:'Preserve Korean’s explicit statement that Hugo became patriarch by killing his older brothers.',
44:'Repair historical audit ED-00073 with a natural statement of Vikir recognizing Baskerville’s true nature.',
55:'Use Hugo’s established forgiveness maxim, corroborated by the series reference.',
56:'Clarify that Vikir is repeating Hugo’s old words in the present rather than leaving the active speaker ambiguous.',
61:'Preserve Korean’s comparison to Hugo’s eldest son.',
71:'Restore Korean’s fuller haggis description, including its calorie/nutrient density and salty unpleasant taste.',
80:'Render Vikir’s interpretation of Hugo’s reaction naturally without awkward nested quotation.',
91:'Keep Korean/MTL direct-line distinction without naming later competitors.',
94:'Repurpose the MTL scene-divider paragraph as the first post-break narrative slot; Korean line 98 is separately restored as ◆◆◆ after paragraph 93.',
95:'Use established Fang Castle terminology for the juvenile residence/kitchen location.',
97:'Repair historical audit ED-00074 by rendering the underground food-storage statement as a complete sentence in the post-break realignment.',
99:'Follow Korean: Barrymore raises a lantern to illuminate the storage room; reject the MTL hand-dissipating-mist corruption.',
100:'Conservatively render the mana-versus-manual-lighting contrast without inventing a new technique.',
111:'Use Morgue Family consistently with accepted terminology.',
116:'Normalize raw cacao beans, not MTL coca beans.',
120:'Preserve the Korean-only separate sentence that an intense-flavored variety would be even more bitter.',
122:'Restore the Bloody Bean origin/concentration explanation with family elders rather than MTL senators.',
125:'Render Korean 있는 만큼 as all available beans.',
130:'Use concentration/enough-to-make wording rather than MTL consistency.',
132:'Replace the opaque bite sound token with contextual Crunch!.',
135:'Correct MTL peas to cacao bean.',
139:'Correct the 10,000-liter figure to the whole pouch, not one bean; over 100 beans × about 100 liters each supports the total.',
146:'Preserve the exact endpoint: Vikir did not take the raw beans to eat; do not reveal their later use.'
}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def kmap(p):
    return [p + 4] if p <= 93 else [p + 5]

def main():
    mtl_bytes = MTL.read_bytes()
    korean_bytes = KOREAN.read_bytes()
    if sha(mtl_bytes) != MTL_SHA:
        raise SystemExit('Chapter 7 MTL checksum mismatch')
    if sha(korean_bytes) != KOREAN_SHA:
        raise SystemExit('Chapter 7 Korean checksum mismatch')
    doc = ET.fromstring(mtl_bytes)
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    originals = [''.join(p.itertext()) for p in body.findall('.//h:p', NS)]
    if len(originals) != 146 or len(FINAL) != 146:
        raise SystemExit(f'Expected 146 paragraphs, got source={len(originals)} final={len(FINAL)}')
    edits=[]
    for number,(old,new) in enumerate(zip(originals,FINAL),1):
        if old == new: continue
        nums=kmap(number)
        default='Repair English tense, phrasing, punctuation, attribution or perspective after comparing Korean line '+str(nums[0])+'.'
        edits.append([number,new,SPECIFIC_REASONS.get(number,default)])
    spec={'chapter':7,'source':'source/chapters/chapter-007.xhtml','source_sha256':MTL_SHA,'expected_paragraphs':146,'notice':'New reconstruction, not recovered production. Explicit source adjudications and limitations are recorded in editorial/reviews/chapter-0007.md.','korean_alignment':'editorial/korean-alignment/chapter-0007.json','scene_breaks_after':[93],'edits':edits}
    lines=korean_bytes.decode('utf-8-sig').splitlines()
    if len(lines) != 151:
        raise SystemExit(f'Expected 151 Korean physical lines, got {len(lines)}')
    alignment={'chapter':7,'korean_source':'source/korean/chapters/007.txt','korean_sha256':KOREAN_SHA,'mtl_source':'source/chapters/chapter-007.xhtml','mtl_sha256':MTL_SHA,'line_numbering':'One-based physical UTF-8 splitlines; original bytes unchanged.','line_count':151,'paragraphs':[],'non_body_lines':[{'line':1,'disposition':'Repeated title/edition heading.'},{'line':2,'disposition':'Repeated title/edition heading.'},{'line':3,'disposition':'Repeated title/edition heading.'},{'line':4,'disposition':'Repeated title/edition heading.'},{'line':98,'disposition':'Scene break restored after paragraph 93 as ◆◆◆; the MTL divider paragraph is repurposed as the first post-break narrative slot.'}],'shared_lines':[]}
    for p in range(1,147):
        nums=kmap(p)
        alignment['paragraphs'].append({'mtl_paragraph':p,'korean_lines':nums,'line_text_sha256':[sha(lines[n-1].encode()) for n in nums],'comparison':SPECIFIC_REASONS.get(p,'Compared corresponding meaning, event and speaker; source decisions in editorial/reviews/chapter-0007.md.')})
    (ROOT/'editorial/edits').mkdir(parents=True,exist_ok=True)
    (ROOT/'editorial/korean-alignment').mkdir(parents=True,exist_ok=True)
    (ROOT/'editorial/edits/chapter-0007.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'editorial/korean-alignment/chapter-0007.json').write_text(json.dumps(alignment,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    subprocess.run([sys.executable,str(ROOT/'tools/build_editorial_draft.py'),'7'],check=True)
    subprocess.run([sys.executable,str(ROOT/'tools/build_chapter_preview.py'),'7'],check=True)
    print(f'Chapter 7 materialized: {len(edits)} changed paragraphs; all 151 Korean lines accounted for.')

if __name__ == '__main__':
    main()
