import datetime


def get_weekday_for_july_14(year: int) -> str:
    date = datetime.date(year, 7, 14)
    return date.strftime("%A")


if __name__ == "__main__":
    try:
        year_input = input("년도를 입력하세요: ")
        year = int(year_input.strip())
        weekday = get_weekday_for_july_14(year)
        print(f"{year}년 7월 14일은 {weekday}입니다.")
    except ValueError:
        print("올바른 숫자 형태의 년도를 입력해주세요.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
