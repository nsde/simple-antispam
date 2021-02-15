fonts = {
    "box":      "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉",
    "dick":            "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
    # einfach Liste ergänzen
}

# Herausfinden, wo es detected wurde
def get_key(val, input_dict):
    for key, value in input_dict.items():
         if val == value:
             return key
# Überprüfen
def check(text):
    for char in text:
        for font in fonts.values():
            if char in font:
                return "DETECTED! Schrift: " + get_key(font, fonts) + ", Zeichen: " + char
    return False

# Austesten
print("Normaler text: " + str(check("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")))
print("Font-Text" + str(check("hallo, 🅳🅰🆂 🅸🆂🆃 🅴🅸🅽 𝐓𝐞𝐬𝐭")))
