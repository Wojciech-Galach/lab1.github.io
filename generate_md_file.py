import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://chessfox.com/chess-openings-list/"

response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

list_items = [li.find("a") for li in soup.find_all("li") if li.find("a") and li.find("a").has_attr("href")]

print(list_items)

# valid_openings = [(a.get_text(strip=True), urljoin(base_url, a["href"])) for a in list_items if a["href"].startswith("#")]
# Get the first 10 valid openings
# openings = valid_openings[:10]

openings = [(opening, base_url+"#"+opening) for opening in ["Alekhine's-Defense", "Benko-Gambit"]]

markdown_content = """---
title: Chess Openings
---

# Chess: A Game of Strategy and Skill

<img src="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/CHESScom/phphK5JVu.png" alt="Chess Openings" style="width:100%; max-width:600px;">

## The Rise of Chess Popularity

Chess has been a game of intellect and strategy for centuries, but in recent years, it has experienced an unprecedented surge in popularity.  
Several factors have contributed to this renaissance:

- **Online Chess Platforms:** Websites like Chess.com and Lichess have made chess accessible to millions worldwide.  
- **The Queen’s Gambit Effect:** The hit Netflix series *The Queen’s Gambit* introduced chess to a new generation of players.  
- **Twitch & YouTube Boom:** Chess streamers like Hikaru Nakamura and GothamChess have made learning the game engaging and entertaining.  
- **AI & Engines:** With tools like Stockfish and AlphaZero, players can analyze and improve their gameplay like never before.  

## Mastering Chess Openings

A strong chess game often begins with a well-played opening. Here are some of the most important openings every player should know:


<ul>
"""

for name, link in openings:
    markdown_content += f'  <li><a href="{name}" target="_blank">{name}</a></li>\n'

markdown_content += "</ul>\n"

with open("index.markdown", "w", encoding="utf-8") as file:
    file.write(markdown_content)

for name, link in openings:
    subpage_content = f"""---
title: {name}
permalink: /{name}
---

# {name}

U can find more information about this opening here: <a href="{link}" target="_blank">{name}</a>
"""

    with open(name + ".markdown", "w", encoding="utf-8") as file:
        file.write(subpage_content)

print("index.markdown has been created successfully!")