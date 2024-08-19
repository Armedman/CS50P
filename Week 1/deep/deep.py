def deep_thought():
    answer = input("پرسش‌هایی درباره‌ی زندگی، جهان و همه‌چی: ").strip().lower()
    if answer in ["42", "forty two", "forty-two"]:
        print("yes")
    else:
        print("no")

deep_thought()
