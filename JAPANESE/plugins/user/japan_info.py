from pyrogram import Client, filters

# Information about Japanese prefectures and major cities
japan_prefectures_info = """
**Japanese Prefectures and Major Cities:**

- **Hokkaido**
  - Major Cities: Sapporo, Asahikawa, Hakodate, Obihiro

- **Aomori**
  - Major Cities: Aomori, Hirosaki, Misawa, Goshogawara

- **Iwate**
  - Major Cities: Morioka, Kitakami, Ichinoseki, Oshu

- **Miyagi**
  - Major Cities: Sendai, Ishinomaki, Tagajo, Shiroishi

- **Akita**
  - Major Cities: Akita, Yokote, Odate, Daisen

- **Yamagata**
  - Major Cities: Yamagata, Tendo, Sakata, Kaminoyama

- **Fukushima**
  - Major Cities: Fukushima, Koriyama, Iwaki, Shirakawa

- **Ibaraki**
  - Major Cities: Mito, Tsukuba, Hitachi, Hitachinaka

- **Tochigi**
  - Major Cities: Utsunomiya, Tochigi, Kanuma, Nikko

- **Gunma**
  - Major Cities: Maebashi, Takasaki, Kiryu, Numata

- **Saitama**
  - Major Cities: Saitama, Kawaguchi, Koshigaya, Urawa

- **Chiba**
  - Major Cities: Chiba, Funabashi, Matsudo, Narita

- **Tokyo**
  - Major Cities: Tokyo, Shinjuku, Shibuya, Ikebukuro

- **Kanagawa**
  - Major Cities: Yokohama, Kawasaki, Sagamihara, Kamakura

- **Niigata**
  - Major Cities: Niigata, Joetsu, Nagaoka, Sanjo

- **Toyama**
  - Major Cities: Toyama, Takaoka, Uozu, Kurobe

- **Ishikawa**
  - Major Cities: Kanazawa, Nonoichi, Komatsu, Kaga

- **Fukui**
  - Major Cities: Fukui, Tsuruga, Sabae, Echizen

- **Yamanashi**
  - Major Cities: Kofu, Fujiyoshida, Minami Alps, Otsuki

- **Nagano**
  - Major Cities: Nagano, Matsumoto, Ueda, Suwa

- **Gifu**
  - Major Cities: Gifu, Ogaki, Kakamigahara, Toki

- **Shizuoka**
  - Major Cities: Shizuoka, Hamamatsu, Numazu, Fujinomiya

- **Aichi**
  - Major Cities: Nagoya, Toyota, Okazaki, Anjo

- **Mie**
  - Major Cities: Tsu, Yokkaichi, Matsusaka, Ise

- **Shiga**
  - Major Cities: Otsu, Hikone, Kusatsu, Nagahama

- **Kyoto**
  - Major Cities: Kyoto, Uji, Fushimi, Kameoka

- **Osaka**
  - Major Cities: Osaka, Sakai, Higashiosaka, Suita

- **Hyogo**
  - Major Cities: Kobe, Himeji, Amagasaki, Nishinomiya

- **Nara**
  - Major Cities: Nara, Tenri, Kashihara, Yamatokoriyama

- **Wakayama**
  - Major Cities: Wakayama, Tanabe, Hashimoto, Shirahama

- **Tottori**
  - Major Cities: Tottori, Yonago, Kurayoshi, Sakaiminato

- **Shimane**
  - Major Cities: Matsue, Izumo, Hamada, Masuda

- **Okayama**
  - Major Cities: Okayama, Kurashiki, Tamano, Soja

- **Hiroshima**
  - Major Cities: Hiroshima, Kure, Fukuyama, Higashihiroshima

- **Yamaguchi**
  - Major Cities: Yamaguchi, Ube, Shunan, Hofu

- **Tokushima**
  - Major Cities: Tokushima, Naruto, Awa, Komatsushima

- **Kagawa**
  - Major Cities: Takamatsu, Marugame, Kotohira, Zentsuji

- **Ehime**
  - Major Cities: Matsuyama, Imabari, Uwajima, Saijo

- **Kochi**
  - Major Cities: Kochi, Nankoku, Shimanto, Tosashimizu

- **Fukuoka**
  - Major Cities: Fukuoka, Kitakyushu, Kurume, Iizuka

- **Saga**
  - Major Cities: Saga, Karatsu, Takeo, Imari

- **Nagasaki**
  - Major Cities: Nagasaki, Sasebo, Isahaya, Hirado

- **Kumamoto**
  - Major Cities: Kumamoto, Yatsushiro, Amakusa, Hitoyoshi

- **Oita**
  - Major Cities: Oita, Beppu, Nakatsu, Usa

- **Miyazaki**
  - Major Cities: Miyazaki, Nobeoka, Hyuga, Kanoya

- **Kagoshima**
  - Major Cities: Kagoshima, Kanoya, Izumi, Amami

- **Okinawa**
  - Major Cities: Naha, Okinawa City, Urasoe, Itoman
"""

@app.on_message(filters.command("japan_info"))
def send_japan_info(client, message):
    message.reply_text(japan_prefectures_info, parse_mode="markdown")

