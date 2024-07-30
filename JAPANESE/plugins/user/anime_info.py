from pyrogram import Client, filters


# Information about popular anime
anime_list_info = """
**Popular Anime List:**

- **Naruto**
  - **Rating:** 8.3/10
  - **Story:** A young ninja named Naruto Uzumaki seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village. He faces various challenges and adventures as he grows from a mischievous boy into a powerful ninja.

- **One Piece**
  - **Rating:** 9.1/10
  - **Story:** Monkey D. Luffy, a young pirate with the ability to stretch his body like rubber, sets off on a quest to find the ultimate treasure known as One Piece. Alongside his diverse crew, Luffy faces numerous challenges on his journey to become the Pirate King.

- **Attack on Titan**
  - **Rating:** 8.8/10
  - **Story:** In a world where humanity lives within enormous walled cities to protect themselves from giant humanoid creatures known as Titans, Eren Yeager joins the military to seek revenge against the Titans that killed his mother and destroyed his home.

- **Dragon Ball Z**
  - **Rating:** 8.7/10
  - **Story:** The adventures of Goku and his friends as they defend Earth from powerful foes, search for the mystical Dragon Balls, and battle formidable enemies. The series follows Goku’s evolution from a child to a powerful warrior.

- **My Hero Academia**
  - **Rating:** 8.4/10
  - **Story:** In a world where nearly everyone has superpowers called Quirks, Izuku Midoriya, a Quirkless boy, dreams of becoming a hero. After inheriting the power of the greatest hero, All Might, he enrolls in U.A. High School to train as a professional hero.

- **Death Note**
  - **Rating:** 8.6/10
  - **Story:** High school student Light Yagami discovers a mysterious notebook that allows him to kill anyone by writing their name in it. He uses the Death Note to rid the world of criminals, while a brilliant detective known as L seeks to stop him.

- **Fullmetal Alchemist: Brotherhood**
  - **Rating:** 9.1/10
  - **Story:** After a failed alchemical experiment, brothers Edward and Alphonse Elric set out on a quest to find the Philosopher's Stone to restore their bodies. Their journey involves complex battles, deep moral questions, and the fight against dark forces.

- **Sword Art Online**
  - **Rating:** 7.7/10
  - **Story:** Players of a virtual reality MMORPG become trapped in the game, with the only way to escape being to clear the game's levels. Kirito, a skilled player, fights to survive and protect his friends in this high-stakes virtual world.

- **Demon Slayer: Kimetsu no Yaiba**
  - **Rating:** 8.7/10
  - **Story:** Tanjiro Kamado becomes a demon slayer after his family is slaughtered by demons and his sister Nezuko is turned into one. He embarks on a quest to avenge his family and cure his sister of her demon curse.

- **Cowboy Bebop**
  - **Rating:** 8.9/10
  - **Story:** Set in a futuristic world, the series follows a group of bounty hunters traveling aboard the spaceship Bebop as they chase criminals, face various adventures, and confront their troubled pasts.

- **Tokyo Ghoul**
  - **Rating:** 7.8/10
  - **Story:** Kaneki, a college student, is transformed into a half-ghoul after a near-fatal encounter with one. He must navigate the dangerous world of ghouls while grappling with his new identity and the hunger for human flesh.

- **Steins;Gate**
  - **Rating:** 8.9/10
  - **Story:** A group of friends discovers a method to send messages to the past using a modified microwave. Their experiments with time travel lead to unintended consequences and dangerous situations as they try to fix the timeline.

- **Neon Genesis Evangelion**
  - **Rating:** 8.5/10
  - **Story:** In a post-apocalyptic world, teenagers pilot giant mechs called Evangelions to protect humanity from mysterious beings known as Angels. The series explores psychological and existential themes as the pilots face both external threats and internal struggles.

- **Hunter x Hunter**
  - **Rating:** 9.0/10
  - **Story:** Gon Freecss, a young boy who aspires to be a Hunter like his absent father, embarks on a journey to become a Hunter himself. Along the way, he faces challenges, uncovers dark secrets, and meets a variety of characters.

- **One Punch Man**
  - **Rating:** 8.4/10
  - **Story:** Saitama, a hero who can defeat any opponent with a single punch, struggles with boredom and a lack of recognition. The series follows his quest for a worthy challenge while dealing with various villains and superhero organizations.

- **Bleach**
  - **Rating:** 7.9/10
  - **Story:** Ichigo Kurosaki, a teenager who can see ghosts, accidentally acquires the powers of a Soul Reaper and is tasked with protecting the living world from malevolent spirits known as Hollows while guiding lost souls to the afterlife.

- **Code Geass**
  - **Rating:** 8.7/10
  - **Story:** Lelouch vi Britannia gains the power of Geass, allowing him to command others to obey his will. He uses this power to lead a rebellion against the oppressive Britannian Empire to create a better world for his sister.

- **JoJo's Bizarre Adventure**
  - **Rating:** 8.3/10
  - **Story:** The Joestar family faces supernatural threats across generations in a series of bizarre adventures involving unique powers known as Stands. Each part of the series follows a different member of the Joestar family.

- **Fairy Tail**
  - **Rating:** 7.8/10
  - **Story:** Lucy Heartfilia, a young wizard, joins the Fairy Tail guild and teams up with powerful mages to undertake various missions and protect their guild from powerful enemies. The series focuses on friendship, adventure, and magic.

- **Mob Psycho 100**
  - **Rating:** 8.5/10
  - **Story:** Shigeo "Mob" Kageyama, a young psychic with powerful abilities, seeks to live a normal life while struggling with his overwhelming powers and trying to deal with personal and supernatural challenges.

- **Gintama**
  - **Rating:** 8.7/10
  - **Story:** In an alternate history where aliens have invaded Japan, Gintoki Sakata, a samurai, takes on various odd jobs in a chaotic world. The series blends action, comedy, and parodies of other anime and manga.

- **Psycho-Pass**
  - **Rating:** 8.1/10
  - **Story:** In a future society where mental states are monitored and crimes are prevented before they occur, young officer Akane Tsunemori must uphold the law and deal with criminals while navigating the complexities of the system.

- **Re:Zero - Starting Life in Another World**
  - **Rating:** 8.3/10
  - **Story:** Subaru Natsuki is transported to a fantasy world and discovers he has the ability to return to life after death, using this power to solve problems and protect those he cares about while navigating the challenges of his new world.
"""

@app.on_message(filters.command("anime_info"))
def send_anime_info(client, message):
    message.reply_text(anime_list_info, parse_mode="markdown")

