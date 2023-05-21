def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Niedowaga"
    elif bmi < 25:
        return "Normalna waga"
    elif bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"

def get_bmi_advice(bmi):
    if bmi < 18.5:
        return "Zalecamy zwiększenie spożycia kalorii i odżywianie się bardziej zrównoważone."
    elif bmi < 25:
        return "Gratulacje! Twoja waga jest w normie. Zachowaj zdrowy styl życia."
    elif bmi < 30:
        return "Zalecamy ograniczenie spożycia kalorii i zwiększenie aktywności fizycznej."
    else:
        return "Zalecamy skonsultować się z lekarzem i rozważyć zmianę stylu życia."

def main():
    weight = float(input("Podaj wagę w kilogramach: "))
    height = float(input("Podaj wzrost w metrach: "))

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)
    advice = get_bmi_advice(bmi)

    print("Twój BMI wynosi:", round(bmi, 2))
    print("Interpretacja BMI:", interpretation)
    print("Porady dotyczące zdrowego stylu życia:", advice)

if __name__ == "__main__":
    main()
