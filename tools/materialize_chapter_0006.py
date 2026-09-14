"""Materialize the reviewed Chapter 6 reconstruction from immutable source witnesses."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'h': 'http://www.w3.org/1999/xhtml'}
MTL = ROOT / 'source/chapters/chapter-006.xhtml'
KOREAN = ROOT / 'source/korean/chapters/006.txt'
MTL_SHA = 'e3d04aedc45bede6f35674fba1189ac452f76189c94802afe3fb818271eff938'
KOREAN_SHA = '98f2e69064d358227ce68d32c0f576c20b1d007ad5c56d0b0afa244e4a0cd567'

FINAL = [
'John Barrymore.',
'He had served the Baskerville family as a butler for four generations.',
'“My lord. I’m here to give today’s report.”',
'Seated before Barrymore was a middle-aged man.',
'He had a blade-sharp nose, a thick beard, and eyes as cold as ice.',
'A Sword Master. The Sword Star. One of the Seven Pillars who had saved the Empire.',
'Hugo Le Baskerville, patriarch of the Iron-Blooded Sword Clan, watched Barrymore with an expressionless face.',
'“First report: the bloodshed with the Morgue Family at the ruby mines of Red Fang Mountain.”',
'The Morgue Family, famed for its magic, was one of the seven great families alongside the Baskervilles.',
'The two families had recently been locked in a territorial dispute over a rich ruby mine in the west, right along the boundary of their domains.',
'After a while, Hugo finally spoke.',
'“We’ll have a chance to discuss that soon. Morgue will contact us first.”',
'Hugo gestured for him to continue.',
'Barrymore resumed his report.',
'Hugo listened with little interest, his expression barely changing.',
'An occasional irritated frown was his only response.',
'Just then—',
'One report, however, was different.',
'For the first time that day, Hugo’s expression changed.',
'“…Master Vikir placed first in the written portion of this midterm evaluation at Fang Castle.”',
'At Barrymore’s words, Hugo gently stroked his chin.',
'Barrymore knew from experience that this was Hugo’s habit whenever he was pleased.',
'Hugo rarely remembered the names of the family’s children, so Barrymore’s expression brightened as well.',
'Soon Hugo asked a question.',
'“Butler. When do the children take their practical exam?”',
'“Soon. It starts in five days. Most of Fang Castle’s Guardian Knights have already left to prepare.”',
'“Then Fang Castle must be nearly empty.”',
'Barrymore’s expression shifted slightly.',
'“As it happens, the next report concerns Fang Castle, my lord.”',
'“Did something happen?”',
'“Well… there’s good news and bad news.”',
'“Good news first.”',
'At Hugo’s show of interest, Barrymore’s voice gained a little strength.',
'“They say two suns appeared in the sky above Fang Castle.”',
'“Two suns?”',
'Hugo’s eyes widened slightly.',
'The Baskerville family was surprisingly superstitious.',
'“An auspicious sign?”',
'“At the very least, there were two suns, weren’t there? The servants are saying a little sun has been born to aid the heir.”',
'“…Hmm. Could someone have been playing a trick with mana?”',
'“Everyone capable of such a prank was away on official business or helping prepare the practical exam.”',
'“Then it doesn’t sound like a bad omen. Another sun…”',
'Hugo nodded quietly.',
'Since ancient times, the appearance of two suns—or of multicolored clouds—had been regarded as an auspicious sign.',
'“Whenever such signs appear, good fortune comes to the family. I wonder what will happen at Fang Castle.”',
'Barrymore’s expression darkened.',
'“Well… something did happen.”',
'“That’s the bad news you mentioned? Tell me.”',
'Barrymore resumed his report in a grave tone.',
'“There was a serious fight among the young masters.”',
'At once, Hugo’s expression changed completely.',
'“A serious fight? How many died?”',
'“…No one died. But Master Highbro’s teeth were shattered, Master Middlebro’s jaw was broken, and Master Lowbro’s right index finger was severed. They have all received treatment and recovered.”',
'“Then it was only a minor scuffle. Brothers grow up fighting.”',
'Relieved, Hugo leaned back in his chair.',
'He flipped through the reports on the triplets and murmured.',
'“The three of them are always together. Surely they didn’t fight one another?”',
'“Correct. They clashed with another young master.”',
'“Fools. In this family, anyone older than them should obviously be stronger. Even pups size up whether an opponent is stronger or weaker before attacking.”',
'Hugo clicked his tongue, and Barrymore corrected him.',
'“Actually… the young master who did that to them was younger.”',
'“What? Younger? Are you saying the entire class of eight-year-olds ganged up on them?”',
'“No. One boy.”',
'A strange light returned to Hugo’s eyes.',
'Barrymore’s next words made that light sharpen.',
'“The culprit was Master Vikir—the same boy I mentioned, who ranked first on the written exam.”',
'Vikir Van Baskerville was eight years old that year.',
'Summoned by the patriarch, he made his way to a private study deep within the mansion.',
'When he opened the door, Hugo Le Baskerville’s imposing frame came into view.',
'“Sit.”',
'Though Hugo released no deliberate aura, the pressure of his mere presence was immense.',
'Vikir moved carefully, making sure not to expose the mana hidden within his body.',
'‘I’m confident in hiding my mana.’',
'Warriors who had survived the war against demons and the long Age of Destruction were masters at concealing their mana.',
'No warrior of the present era, who had never lived through that age, knew how to hide mana so completely.',
'It was a matter of experience, not strength.',
'Yet even that technique had limits. If his mana grew much stronger, Hugo would inevitably notice.',
'‘I’ll need a solution before that happens.’',
'With that thought, Vikir sat down on the small chair prepared for him.',
'Hugo spoke.',
'“It’s been a while. You’ve grown a lot.”',
'Vikir was slightly surprised.',
'His voice, usually honed like a blade and sharp enough to cut merely by being heard, sounded strangely subdued today.',
'The words themselves were just as unexpected.',
'‘Piglets grow quickly. Why do these brats look so scrawny every time I see them?’',
'Before his regression, Hugo used to say things like that all the time.',
'Back then, he watched children grow the way a butcher judged livestock for market. Today, however, his gaze was strangely warm.',
'Almost as if he expected something from Vikir.',
'“Greetings, Patriarch.”',
'Vikir greeted him brightly, like a child.',
'But Hugo seemed oddly dissatisfied with the title “Patriarch.”',
'“Patriarch, huh? Not ‘Father’?”',
'He considered something for a moment, then changed the subject.',
'“I hear you crippled the triplets in the nine-year-old advanced class.”',
'“As I understand it, they received proper treatment afterward.”',
'“I’m not talking about their bodies.”',
'Hugo frowned.',
'“What about their minds?”',
'“… ”',
'“Since that day, they eat separately, sleep separately, and barely speak to one another. Their teamwork used to be excellent, but now they’ve completely fallen apart.”',
'And that wasn’t all. These days, all three were so terrified of Vikir that they wet themselves whenever they saw him.',
'A hound that had lost its fighting spirit was useless on the battlefield.',
'Vikir saw no need to mention that.',
'Instead, he simply stated his opinion.',
'“Carrying three dull blades only weighs you down. Better one finely forged sword.”',
'Admiration flashed through Hugo’s eyes.',
'“…Indeed.”',
'Stroking his chin, he looked down at the eight-year-old before him.',
'A faint smile tugged at the corners of his mouth.',
'“But don’t you think it was wrong to hurt your brothers?”',
'Vikir looked genuinely puzzled.',
'“Wrong? What did I do wrong?”',
'“What are you talking about? You battered your brothers.”',
'Vikir tilted his head as though he truly did not understand.',
'“What’s wrong with that? I’m stronger.”',
'“…What?”',
'Vikir turned the question back on the stunned Hugo.',
'“How can the strong be wrong?”',
'Strength was justice. Weakness was sin.',
'Wasn’t that the creed of Baskerville?',
'A moment passed.',
'“… ”',
'The corners of Hugo Le Baskerville’s mouth began to twitch.',
'The little boy before him was so endearing it made his chest ache.'
]

SPECIFIC_REASONS = {
4:'Repair historical audit fragment ED-00070 by restoring a complete seated-subject sentence from Korean line 6.',
5:'Repair historical audit fragment ED-00071 while preserving the separate physical-description paragraph.',
6:'Restore Hugo’s Sword Master/Sword Star/Seven Pillars titles from the combined Korean line and canonical series terminology.',
8:'Use Morgue Family and canonical Red Fang Mountain; preserve Red Cane/Red Peak only in the source review as variants.',
13:'Render the Korean action as Hugo gesturing for Barrymore to continue, rather than the MTL’s broken folded-hands clause.',
17:'Remove the MTL-only advertising insertion by assigning this conserved paragraph to Korean line 17, “Just then—”.',
18:'Split Korean line 18 across two conserved MTL paragraphs; shared-line ownership is declared explicitly.',
19:'Complete the second half of Korean line 18 without restoring the advertisement text.',
20:'Correct MTL “handwriting” to the written portion of the midterm evaluation.',
39:'Restore Korean’s rumor that a little sun was born to aid the heir, not merely the children.',
41:'Restore Korean’s official-business/practical-exam preparation explanation for why no capable prankster was present.',
44:'Restore Korean’s two-suns/multicolored-cloud omen; reject MTL “Chae-un” as a corrupted proper noun.',
53:'Keep the accepted Chapter 5 injury sequence and note that treatment restored the triplets physically.',
57:'Repair the malformed question about whether the inseparable triplets fought one another.',
59:'Preserve Hugo’s assumption that older Baskerville children should be stronger and his pups-sizing-up-opponents analogy.',
61:'Clarify that the attacker was younger than the triplets.',
66:'Identify Vikir as both the sole attacker and the written-exam first place immediately before the Korean scene break.',
68:'Render the summons as a visit to the patriarch’s private study without treating the Korean “city” corruption as a new location.',
75:'Restore Korean’s Age-of-Destruction knowledge distinction rather than the MTL’s vague “unknown right now”.',
76:'Use Korean experience, not MTL skill, as the basis of advanced mana concealment.',
78:'Conservatively repair the conflicting witnesses as Vikir needing a solution before stronger mana becomes noticeable.',
87:'Restore the livestock/butcher comparison while keeping today’s warmer gaze distinct.',
92:'Adjudicate the corrupted title exchange as Patriarch versus Father; Hugo is canonically Vikir’s father and the reaction otherwise has no coherent object.',
101:'Restore Korean’s explicit detail that the triplets now wet themselves in fear when they see Vikir.',
102:'Use battlefield for the hound-without-fighting-spirit maxim.',
105:'Restore the Korean metaphor of three dull blades versus one finely forged blade.',
118:'Render Vikir’s challenge in direct modern English: how can the strong be wrong?',
119:'Use the established Baskerville creed “Strength is justice. Weakness is sin.”',
124:'Preserve the Korean endpoint that the child is endearing enough to make Hugo’s chest ache; do not import later reconciliation.'
}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def kmap(p):
    if p in (1, 2): return [4]
    if p == 3: return [5]
    if p in (4, 5, 6): return [6]
    if 7 <= p <= 17: return [p]
    if p in (18, 19): return [18]
    if 20 <= p <= 66: return [p - 1]
    return [p]

def main():
    mtl_bytes = MTL.read_bytes()
    korean_bytes = KOREAN.read_bytes()
    if sha(mtl_bytes) != MTL_SHA:
        raise SystemExit('Chapter 6 MTL checksum mismatch')
    if sha(korean_bytes) != KOREAN_SHA:
        raise SystemExit('Chapter 6 Korean checksum mismatch')
    doc = ET.fromstring(mtl_bytes)
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    originals = [''.join(p.itertext()) for p in body.findall('.//h:p', NS)]
    if len(originals) != 124 or len(FINAL) != 124:
        raise SystemExit(f'Expected 124 paragraphs, got source={len(originals)} final={len(FINAL)}')
    edits=[]
    for number,(old,new) in enumerate(zip(originals,FINAL),1):
        if old == new: continue
        nums=kmap(number)
        default='Repair English tense, phrasing, punctuation, attribution or perspective after comparing Korean '+('lines ' if len(nums)>1 else 'line ')+', '.join(map(str,nums))+'.'
        edits.append([number,new,SPECIFIC_REASONS.get(number,default)])
    spec={'chapter':6,'source':'source/chapters/chapter-006.xhtml','source_sha256':MTL_SHA,'expected_paragraphs':124,'notice':'New reconstruction, not recovered production. Explicit source adjudications and limitations are recorded in editorial/reviews/chapter-0006.md.','korean_alignment':'editorial/korean-alignment/chapter-0006.json','scene_breaks_after':[66],'edits':edits}
    lines=korean_bytes.decode('utf-8-sig').splitlines()
    if len(lines) != 124:
        raise SystemExit(f'Expected 124 Korean physical lines, got {len(lines)}')
    specific_compare={k:v for k,v in SPECIFIC_REASONS.items()}
    alignment={'chapter':6,'korean_source':'source/korean/chapters/006.txt','korean_sha256':KOREAN_SHA,'mtl_source':'source/chapters/chapter-006.xhtml','mtl_sha256':MTL_SHA,'line_numbering':'One-based physical UTF-8 splitlines; original bytes unchanged.','line_count':124,'paragraphs':[],'non_body_lines':[{'line':1,'disposition':'Repeated title/edition heading.'},{'line':2,'disposition':'Repeated title/edition heading.'},{'line':3,'disposition':'Repeated title/edition heading.'},{'line':66,'disposition':'Scene break restored after paragraph 66 as ◆◆◆.'}],'shared_lines':[{'line':4,'mtl_paragraphs':[1,2],'reason':'Korean physical line combines the Barrymore name and four-generation service statement split across MTL paragraphs 1–2.'},{'line':6,'mtl_paragraphs':[4,5,6],'reason':'Korean physical line combines the seated man, physical description and titles split across MTL paragraphs 4–6.'},{'line':18,'mtl_paragraphs':[18,19],'reason':'After removing the MTL-only advertisement insertion, Korean line 18 is rendered across two conserved MTL paragraphs.'}]}
    for p in range(1,125):
        nums=kmap(p)
        comparison=specific_compare.get(p,'Compared corresponding meaning, event and speaker; source decisions in editorial/reviews/chapter-0006.md.')
        alignment['paragraphs'].append({'mtl_paragraph':p,'korean_lines':nums,'line_text_sha256':[sha(lines[n-1].encode()) for n in nums],'comparison':comparison})
    (ROOT/'editorial/edits').mkdir(parents=True,exist_ok=True)
    (ROOT/'editorial/korean-alignment').mkdir(parents=True,exist_ok=True)
    (ROOT/'editorial/edits/chapter-0006.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'editorial/korean-alignment/chapter-0006.json').write_text(json.dumps(alignment,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    subprocess.run([sys.executable,str(ROOT/'tools/build_editorial_draft.py'),'6'],check=True)
    subprocess.run([sys.executable,str(ROOT/'tools/build_chapter_preview.py'),'6'],check=True)
    print(f'Chapter 6 materialized: {len(edits)} changed paragraphs; all 124 Korean lines accounted for.')

if __name__ == '__main__':
    main()
