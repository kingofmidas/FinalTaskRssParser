# RSS-READER

### Command-line utility which receives RSS URL and prints results in human-readable format.

**Example:**
python rss_reader.py https://news.yahoo.com/rss - -limit 1

**Output**:

Feed:  Yahoo News - Latest News & Headlines

Title:  Families come from across U.S. to grieve relatives slain in Mexico
Date:  Thu, 07 Nov 2019 01:06:45 -0500
Link:  https://news.yahoo.com/under-armed-escort-mourner-convoys-060645935.html

Description:  An American man whose grandchildren were slain in a massacre in Mexico demanded justice on Thursday for other victims of the country's drug war, as relatives gathered from
across the United States for a funeral guarded by heavily armed military.  Kenneth Miller lost his daughter-in-law and four grandchildren, all dual citizens, in an ambush on Monday in th
e northern border state of Sonora that killed three mothers and six children.  The attack on members of breakaway Mormon communities who  settled in Mexico decades ago prompted U.S. Pres
ident Donald Trump to urge Mexico and the United States to "wage war" together on drug cartels.

Links:
```
[1]:  https://news.yahoo.com/under-armed-escort-mourner-convoys-060645935.html (link)
[2]:  http://l.yimg.com/uu/api/res/1.2/rRx_J3xHKYzIQ4EsiCPRTw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en-US/reuters.com/9cbb9d9c38b8bbe10243ebfde0f6db48
```

```
positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

```