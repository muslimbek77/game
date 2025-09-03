quiz = {
    #key:value
    "Python dasturlash tili qachon yaratilgan ? ":"1991",
    "Gvido van Rossum qaysi dasturlash tilini yaratgan ?":"Python",
    "'1.5' Bu qanday ma'lumot turiga tegishli ? ":"str",
    "Pythonda web sayt yaratish uchun qaysi frameworkdan foydalanamiz ? ":"Django"
}
point = 0
for savol,javob in quiz.items():
    j = input(savol)
    if j.lower() == javob.lower():
        point += 1
        print("✅ To'g'ri topdingiz...🎉")
    else:
        print(f"❌Afsuski topa olmadingiz. 😔\nJavob:{javob}")
foiz = point/len(quiz)*100
print(f"🟢 Topshiriq yakunlandi siznig natijangiz: {foiz}%")