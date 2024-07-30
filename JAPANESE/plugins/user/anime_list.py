from pyrogram import Client, filters


# Information about popular anime
anime_list_info = """
**Popular Anime List:**

- **Naruto**
  - Description: A young ninja named Naruto seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village.

- **One Piece**
  - Description: Monkey D. Luffy and his pirate crew search for the ultimate treasure, One Piece, in order to become the Pirate King.

- **Attack on Titan**
  - Description: Humanity fights for survival against gigantic humanoid creatures known as Titans that have brought the world to the brink of extinction.

- **Dragon Ball Z**
  - Description: The adventures of Goku continue as he defends Earth against powerful foes and searches for the mystical Dragon Balls.

- **My Hero Academia**
  - Description: In a world where superpowers (known as Quirks) are common, a powerless boy enrolls in a hero academy to become the greatest hero.

- **Death Note**
  - Description: A high school student discovers a mysterious notebook that allows him to kill anyone by writing their name in it and sets out to rid the world of criminals.

- **Fullmetal Alchemist: Brotherhood**
  - Description: Two brothers use alchemy in their quest to find the Philosopher's Stone to restore their bodies after a failed alchemical experiment.

- **Sword Art Online**
  - Description: Players trapped in a virtual reality MMORPG must clear the game to escape, while the protagonist aims to rescue his friends and escape the game.

- **Demon Slayer: Kimetsu no Yaiba**
  - Description: A young boy becomes a demon slayer to avenge his family and cure his sister, who has been turned into a demon.

- **Cowboy Bebop**
  - Description: A group of bounty hunters traveling in their spaceship, the Bebop, deal with various challenges as they try to capture criminals and make a living.

- **Tokyo Ghoul**
  - Description: Kaneki, a college student, is turned into a half-ghoul and must navigate a world where he is neither fully human nor fully ghoul.

- **Steins;Gate**
  - Description: A group of friends accidentally invent a time machine and must deal with the consequences of altering the past.

- **Neon Genesis Evangelion**
  - Description: Pilots of giant mechs are humanity's last defense against mysterious beings known as Angels in a post-apocalyptic world.

- **Hunter x Hunter**
  - Description: A young boy becomes a Hunter to find his father, a legendary Hunter, and embarks on adventures filled with dangerous creatures and trials.

- **One Punch Man**
  - Description: Saitama, a hero who can defeat any opponent with a single punch, searches for a worthy challenge and struggles with boredom.

- **Bleach**
  - Description: Ichigo Kurosaki, a teenager with the ability to see ghosts, becomes a Soul Reaper and battles malevolent spirits known as Hollows.

- **Code Geass**
  - Description: After gaining the power of Geass, Lelouch vi Britannia leads a rebellion against a tyrannical empire to create a better world for his sister.

- **JoJo's Bizarre Adventure**
  - Description: The Joestar family faces supernatural threats across generations in a series of bizarre adventures involving unique powers called Stand.

- **Fairy Tail**
  - Description: A young wizard, Lucy Heartfilia, joins the Fairy Tail guild and embarks on adventures with her friends to grow stronger and protect their guild.

- **Mob Psycho 100**
  - Description: A young psychic boy tries to live a normal life while dealing with his powerful abilities and the challenges they bring.

- **Gintama**
  - Description: In an alternate history where aliens have invaded Japan, a samurai named Gintoki Sakata takes on various odd jobs in a chaotic world.

- **Psycho-Pass**
  - Description: In a future society where mental states are monitored, a young officer must uphold the law and deal with criminals in a high-tech dystopian world.

- **Re:Zero - Starting Life in Another World**
  - Description: Subaru Natsuki is transported to a fantasy world and discovers he has the ability to return to life after death, which he uses to solve problems and save his friends.
"""

@app.on_message(filters.command("anime_list"))
def send_anime_list(client, message):
    message.reply_text(anime_list_info, parse_mode="markdown")

