# 🚫 Simple FontChecker
A very simple program to check if a text contains special 𝒻𝑜𝓃𝓉𝓈.

# ✔️ Features
- Check **if** a text uses special characters to changestyle.
- Check **which** font and character has been detected
- Simple and very short program
- Doesn't blacklist (most) language characters
- Easy to use
- Lightweight

# ❔ Why should I check my text for fonts
- **Annoying**: fonts can be very annoying and hard to read.
- **Draws attention**: fonts can kind of "highlight" a post or comment, so more people click on it.
- **Design**: fonts change the way a text looks, and special fonts can make a text look ugly.
- **Spam-Bypass**: most of the anti-spam-databases just have the "normal" font registered, and you can block them completely.

# 📜 Supports
This program supports most of the fonts used in: https://www.fancytextguru.com/common.html

# 🔨 Usage
```py
import fontchecker
print("No detection: " + str(check("I am using no font."))) # Output: 'False'
print("Detection: " + str(check("Hello, I am using a 🅵🅾🅽🆃!"))) # Output: 'inverted_squares, char: 🅵' 
```
