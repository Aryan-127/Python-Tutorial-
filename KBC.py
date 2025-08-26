print("Swagat hai aapka Kaun Banega Crorepati mein")
print("Aaiye shuru karte hai,haay!")
num = ["pahla","dusra","tisra","chautha",
"paanchva","chhatha","saantva","aanthva","nauva",
"dasva"]
prize = ["1 hazaar","5 hazaar","10 hazaar","50 hazaar","1 lakh","5 lakh","10 lakh","50 lakh","1 crore","7 crore"]
quiz = {
    1: {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    2: {
        "question": "Who wrote the national anthem of India?",
        "options": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Subramania Bharati"],
        "answer": "Rabindranath Tagore"
    },
    3: {
        "question": "What is the currency of Japan?",
        "options": ["Won", "Yuan", "Yen", "Ringgit"],
        "answer": "Yen"
    },
    4: {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Osmium", "Oxide", "Organium"],
        "answer": "Oxygen"
    },
    5: {
        "question": "In which year did World War II end?",
        "options": ["1942", "1945", "1947", "1950"],
        "answer": "1945"
    },
    6: {
        "question": "Which organ in the human body purifies blood?",
        "options": ["Heart", "Lungs", "Kidneys", "Liver"],
        "answer": "Kidneys"
    },
    7: {
        "question": "Who was the first woman to go to space?",
        "options": ["Valentina Tereshkova", "Sally Ride", "Kalpana Chawla", "Yuri Gagarin"],
        "answer": "Valentina Tereshkova"
    },
    8: {
        "question": "Which is the largest desert in the world?",
        "options": ["Sahara", "Gobi", "Antarctic", "Kalahari"],
        "answer": "Antarctic"
    },
    9: {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    10: {
        "question": "The Great Wall of China was primarily built to protect against which group?",
        "options": ["Romans", "Mongols", "Vikings", "Persians"],
        "answer": "Mongols"
    }
}
for i in range(len(num)):
  print(f"Yeh raha {num[i]} sawaal {prize[i]} rupayo ke liye,aapki computer screen par:")
  print(quiz[i+1]["question"])
  print(quiz[i+1]["options"])
  while True:
    chosen = input("Apna uttar dakhil kare ==> ").title()
    if chosen not in quiz[i+1]["options"]:
      print("Please enter a valid answer!")
      continue
    elif chosen in quiz[i+1]["options"]:
      print(f"Computer ji {chosen} par taala lagaya jaaye.")
      if chosen == quiz[i+1]["answer"]:
        if i+1 < len(quiz):
          print(f"Bilkul sahi uttar hai,aap jeet chuke ho {prize[i]} rupaye!\nChaliye badhte hai agle sawaal ki taraf.")
          break
        else:
          print(f"{prize[i]}!!!!!!!!\nAap jeet chuke hai pure {prize[i]},badhai ho!!Aap is dhan raashi kya karenge,ye ghar jake kisi aur ko bataiyega hum chalte hai!")
      if chosen != quiz[i+1]["answer"]:
        if i <= 2:
          print("Ji aapka uttar galat hai! Sahi uttar tha", quiz[i+1]["answer"], "\nMaaf kijiye par aapko khali haanth hi ghar jana padega!")
          break
        else: 
          print("Ji aapka uttar galat hai! Sahi uttar tha", quiz[i+1]["answer"], "\nPar aap jeet chuke ho", prize[i-2], "rupaye, aapko shubhkaamnaye!")
          break
  if i < 9:
    if chosen == quiz[i+1]["answer"]:
        continue
    else:
        print("Thanks for playing!")
        break
  else:
    print("Thanks for playing!")
    break
      
        
        
    