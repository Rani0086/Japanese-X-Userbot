from pyrogram import Client, filters


# Information about popular manga
manga_list_info = """
**Popular Manga List:**

- **One Piece**
  - **Rating:** 9.1/10
  - **Story:** Monkey D. Luffy, a young pirate with the ability to stretch his body like rubber, seeks the legendary treasure known as One Piece to become the Pirate King. He forms a diverse crew and embarks on adventures across the Grand Line.

- **Naruto**
  - **Rating:** 8.7/10
  - **Story:** Naruto Uzumaki, a young ninja with dreams of becoming the Hokage, seeks recognition and respect from his village. The manga follows his journey from a troubled child to a powerful ninja leader.

- **Attack on Titan**
  - **Rating:** 9.0/10
  - **Story:** Humanity fights for survival within walled cities against giant humanoid creatures known as Titans. Eren Yeager, the protagonist, joins the military to avenge his family and uncover the mysteries behind the Titans.

- **Death Note**
  - **Rating:** 8.9/10
  - **Story:** Light Yagami, a high school student, discovers a notebook that allows him to kill anyone by writing their name in it. He aims to rid the world of criminals while facing off against the genius detective L.

- **Fullmetal Alchemist**
  - **Rating:** 9.2/10
  - **Story:** After a failed alchemical experiment, brothers Edward and Alphonse Elric embark on a quest to find the Philosopher's Stone to restore their bodies. They uncover dark secrets and face numerous challenges on their journey.

- **Dragon Ball**
  - **Rating:** 8.8/10
  - **Story:** Goku, a young martial artist with a mysterious past, seeks powerful artifacts known as Dragon Balls. Along with his friends, he trains and battles formidable foes while striving to become the greatest warrior.

- **My Hero Academia**
  - **Rating:** 8.5/10
  - **Story:** In a world where most people have superpowers called Quirks, Izuku Midoriya, a Quirkless boy, dreams of becoming a hero. After inheriting the power of the greatest hero, All Might, he enrolls in U.A. High School.

- **Tokyo Ghoul**
  - **Rating:** 8.1/10
  - **Story:** Kaneki, a college student, becomes a half-ghoul after a near-fatal encounter. He must navigate the world of ghouls while struggling with his new identity and the hunger for human flesh.

- **One Punch Man**
  - **Rating:** 8.4/10
  - **Story:** Saitama, a hero who can defeat any opponent with a single punch, is bored with his overwhelming power. The manga follows his quest to find a worthy challenge and his interactions with various heroes and villains.

- **JoJo's Bizarre Adventure**
  - **Rating:** 8.6/10
  - **Story:** The Joestar family faces supernatural threats across generations, each with unique abilities called Stands. The manga follows their bizarre adventures as they battle enemies and uncover hidden truths.

- **Hunter x Hunter**
  - **Rating:** 9.0/10
  - **Story:** Gon Freecss, a young boy aspiring to be a Hunter like his father, embarks on a journey to find him. Along the way, he faces various trials, meets new friends, and confronts powerful adversaries.

- **Berserk**
  - **Rating:** 9.4/10
  - **Story:** Guts, a lone mercenary with a tragic past, seeks vengeance against his former friend Griffith. The manga explores themes of fate, ambition, and the struggle between good and evil in a dark medieval world.

- **Fairy Tail**
  - **Rating:** 7.8/10
  - **Story:** Lucy Heartfilia, a young wizard, joins the Fairy Tail guild and teams up with powerful mages to undertake missions and protect their guild from various threats. The manga focuses on friendship and adventure.

- **Black Clover**
  - **Rating:** 7.9/10
  - **Story:** Asta, a boy born without magic in a world where magic is everything, aims to become the Wizard King. He trains hard and faces numerous challenges alongside his childhood friend, Yuno, who is exceptionally talented.

- **Claymore**
  - **Rating:** 8.2/10
  - **Story:** In a world plagued by monstrous creatures called Yoma, half-human, half-demon warriors known as Claymores fight to protect humanity. The story follows Clare, one such warrior, as she seeks revenge for her past.

- **The Promised Neverland**
  - **Rating:** 8.8/10
  - **Story:** Emma, Norman, and Ray, children living in an orphanage, discover a horrifying secret about their existence and plan a daring escape to survive and uncover the truth behind their world.

- **D.Gray-man**
  - **Rating:** 8.1/10
  - **Story:** Allen Walker, a young exorcist with a cursed eye, fights against akuma (demonic creatures) created by the Millennium Earl. The manga follows his quest to prevent the destruction of the world and uncover his own past.

- **Magi: The Labyrinth of Magic**
  - **Rating:** 8.3/10
  - **Story:** Aladdin, a young boy with magical abilities, sets out on a journey to discover the truth about his origins. He encounters various adventures, ancient dungeons, and powerful entities.

- **Hellsing**
  - **Rating:** 8.5/10
  - **Story:** The Hellsing Organization, led by Sir Integra Hellsing, fights against supernatural threats, particularly vampires. The series follows Alucard, a powerful vampire, as he battles dark forces to protect humanity.

- **Nana**
  - **Rating:** 8.4/10
  - **Story:** Two young women named Nana, with vastly different personalities, meet by chance and form a close friendship. The manga explores their struggles with love, dreams, and the challenges of life.

- **Vinland Saga**
  - **Rating:** 8.9/10
  - **Story:** Set in the Viking Age, the story follows Thorfinn, a young warrior seeking revenge for his father's death. The manga explores themes of revenge, honor, and the quest for a promised land known as Vinland.
"""

@app.on_message(filters.command("manga_info"))
def send_manga_info(client, message):
    message.reply_text(manga_list_info, parse_mode="markdown")

