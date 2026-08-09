from __future__ import annotations

from pydantic import BaseModel


class TriviaQuestion(BaseModel):
    id: str
    question: str
    answers: list[str]
    correct_answer: int
    explanation: str


# כל החידון נמצא בקובץ זה. הוסיפו שאלות למערך באותו מבנה.
TRIVIA_QUESTIONS = [
    TriviaQuestion(
        id="isaac-hall",
        question="מה מיוחד באולם יצחק במערת המכפלה?",
        answers=[
            "זה האולם היחיד שנמצא מחוץ למבנה המקורי",
            "זה האולם הגדול במתחם, ובו נמצא הפתח למערה עצמה",
            "שם נמצא קבר דוד המלך",
            "זהו האולם שנבנה על ידי האדמו\"ר האמצעי",
        ],
        correct_answer=1,
        explanation=(
            "נכון! אולם יצחק ורבקה הוא האולם הגדול במתחם, ובו נמצא הפתח "
            "למערה עצמה. כיום זהו גם האזור שנפתח ליהודים בימים מסוימים "
            "שבהם המתחם כולו מוקצה לתפילה יהודית. "
            "מקור: https://hebron.org.il/en/opening-and-closing-dates-for-the-cave-of-the-patriarchs-for-2026/"
        ),
    ),

    TriviaQuestion(
        id="current-isaac-opening",
        question="מה קורה באולם יצחק ורבקה בימים שבהם אינו פתוח ליהודים?",
        answers=[
            "הוא פתוח רק למוסלמים וזה משמש אותם כמסגד 😡",
            "הוא נפתח למתפללים יהודים",
            "הוא משמש רק את הכוהנים",
            "הוא הופך למוזיאון",
        ],
        correct_answer=0,
        explanation=(
            "נכון! במשך השנים שהמוסלמים שלטו בארץ הם הפכו כל דבר קדוש "
            "ליהודים למסגד. ממשלת רבין קבעה שיש לתת למוסלמים את האולם "
            "העיקרי למוסלמים. מיותר לציין שהמצב הזה מרתיח מאין כמוהו "
            "כשאנחנו שולטים בארץ ועדיין נותנים למוסלמים את המקומות הכי "
            "קדושים לעם היהודי. המצב לפני לא היה הרבה יותר טוב כאשר "
            "הייתה חלוקה בשעות שונות. "
            "מקור: https://hebron.org.il/en/opening-and-closing-dates-for-the-cave-of-the-patriarchs-for-2026/"
        ),
    ),

    TriviaQuestion(
        id="seventh-step",
        question="במשך מאות שנים, עד לאן הורשו יהודים להתקרב למערת המכפלה?",
        answers=[
            "עד פתח המערה",
            "עד המדרגה השלישית",
            "עד המדרגה השביעית",
            "עד הרחבה שמחוץ למתחם",
        ],
        correct_answer=2,
        explanation=(
            "נכון! החל משנת ה׳כ״ז המוסלמים ששלטו בארץ אסרו על יהודים "
            "להיכנס למבנה, ויהודים הורשו להגיע עד המדרגה השביעית בלבד. "
            "לפי המקורות הדבר נמשך כ-700 שנה, עד מלחמת ששת הימים. "
            "מקור: https://hebron.org.il/en/843-2/"
        ),
    ),

    TriviaQuestion(
        id="isaac-hall-days",
        question="כמה ימים בשנה ממשלת ישראל מסכימה לפתוח את אולם יצחק ליהודים?",
        answers=[
            "3 ימים",
            "7 ימים",
            "10 ימים",
            "30 ימים",
        ],
        correct_answer=2,
        explanation=(
            "נכון! כיום ישנם עשרה ימים בשנה שבהם האתר מוקצה לתפילה יהודית, "
            " ובשאר הימים החלק העיקרי של המערה מורשה לכניסה למוסלמים בלבד "
            "מקור: https://hebron.org.il/en/opening-and-closing-dates-for-the-cave-of-the-patriarchs-for-2026/"
        ),
    ),

    TriviaQuestion(
        id="window-purim",
        question="מהו 'פורימא דחברון' או 'פורימא דחלון'?",
        answers=[
            "חג שנקבע לזכר חנוכת בית הכנסת אברהם אבינו",
            "יום שבו הגיע הרבי הראשון לחברון",
            "יום הודאה שנקבע בעקבות נס הצלה של יהודי חברון",
            "פורים שנחגג במערת המכפלה בלבד",
        ],
        correct_answer=2,
        explanation=(
            "נכון! לפי המסורת החב\"דית, יהודי חברון ניצלו מגזירה קשה, "
            "ולזכר הנס נקבע יום חג מיוחד. הוא נקשר ל'חלון' שבאזור מערת "
            "המכפלה שדרכו, לפי הסיפור, הועבר פדיון לאבות. "
            "מקור: https://www.chabad.org/holidays/purim/article_cdo/aid/644264/jewish/Purim-Hebron.htm"
        ),
    ),

    TriviaQuestion(
        id="window-pidyon",
        question="לפי הסיפור החסידי של 'פורימא דחברון', כיצד ניסו יהודי חברון להעביר פתק לאבות?",
        answers=[
            "הם הסתירו אותו בתוך ספר תורה",
            "הם הורידו אותו בחבל דרך חלון הקשור למערה",
            "הם מסרו אותו ישירות לכהן",
            "הם השאירו אותו ליד המדרגה השביעית",
        ],
        correct_answer=1,
        explanation=(
            "נכון! לפי הסיפור, מכיוון שהיהודים לא הורשו להיכנס למערה, "
            "הם שיחדו את השומר וביקשו ממנו להשליך את ה'פדיון' דרך חלון "
            "שהיה קשור לפתח המערה. הסיפור הפך לאחד הסיפורים המזוהים "
            "עם 'פורימא דחברון'. "
            "מקור: https://www.chabad.org/holidays/purim/article_cdo/aid/644264/jewish/Purim-Hebron.htm"
        ),
    ),

    TriviaQuestion(
        id="azulai-sultan-sword",
        question="לפי המסורת, מדוע ירד המקובל רבי אברהם אזולאי לתוך מערת המכפלה?",
        answers=[
            "כדי לחקור את הקברים",
            "כדי למצוא כתב יד עתיק",
            "כדי להחזיר חרב של הסולטן שנפלה למערה",
            "כדי לפתוח את המערה לציבור",
        ],
        correct_answer=2,
        explanation=(
            "נכון! לפי הסיפור, חרבו של הסולטן נפלה למערה, וחיילים שנשלחו "
            "להוציא אותה לא חזרו. הסולטן דרש מיהודי חברון לספק מתנדב, "
            "ורבי אברהם אזולאי התנדב לרדת בעצמו. "
            "מקור: https://www.chabad.org/library/article_cdo/aid/588225/jewish/Cave-of-the-Patriarchs-Mearat-Hamachpelah.htm"
        ),
    ),

    TriviaQuestion(
        id="azulai-seven-days",
        question="לפי הסיפור על רבי אברהם אזולאי, מה עשה לאחר שחזר ממערת המכפלה?",
        answers=[
            "עזב מיד את חברון",
            "בנה בית כנסת חדש",
            "לימד את תלמידיו סודות קבלה במשך שבעה ימים",
            "כתב את ספר הזוהר",
        ],
        correct_answer=2,
        explanation=(
            "נכון! לפי המסורת, לאחר שיצא מהמערה רבי אברהם אזולאי הקדיש "
            "שבעה ימים ולילות ללימוד סודות קבליים עם תלמידיו. שבוע לאחר "
            "שירד למערה הוא נפטר. "
            "מקור: https://www.chabad.org/kabbalah/article_cdo/aid/1321931/jewish/The-Fallen-Sword-of-the-Sultan.htm"
        ),
    ),

    TriviaQuestion(
        id="frierdiker-rebbe-hebron",
        question="מה מיוחד בביקורו של הרבי הריי\"צ בחברון בשנת תרפ״ט?",
        answers=[
            "הוא היה היהודי הראשון שביקר בחברון",
            "הוא הצליח להיכנס לתוך מבנה מערת המכפלה, למרות שהכניסה ליהודים הייתה מוגבלת",
            "הוא הקים את ישיבת תורת אמת",
            "הוא קנה את מערת המכפלה",
        ],
        correct_answer=1,
        explanation=(
            "נכון! הרבי הריי\"צ, ביקר בחברון ב-13 "
            "באוגוסט 1929. הוא ופמלייתו קיבלו הזדמנות נדירה להיכנס לתוך "
            "מבנה מערת המכפלה, שבדרך כלל היה סגור בפני יהודים. "
            "מקור: https://hebron.org.il/en/52499-2/"
        ),
    ),

    TriviaQuestion(
        id="1929-eleven-days",
        question="כמה זמן בערך לפני פרעות תרפ״ט ביקר הרבי הריי\"צ בחברון?",
        answers=[
            "יום אחד",
            "כשבועיים",
            "כשלושה חודשים",
            "שנה",
        ],
        correct_answer=1,
        explanation=(
            "נכון! הרבי הריי\"צ ביקר בחברון ב-13 באוגוסט 1929, "
            "והפרעות החלו ב-24 באוגוסט — 11 ימים בלבד לאחר ביקורו. "
            "מקור לביקור: https://hebron.org.il/en/52499-2/"
        ),
    ),

    TriviaQuestion(
        id="mitteler-rebbe-property",
        question="מה היה הנכס החב\"די הראשון בארץ ישראל שנרכש על ידי האדמו\"ר האמצעי בחברון?",
        answers=[
            "בית רומנו",
            "בית הדסה",
            "בית הכנסת של האדמו\"ר האמצעי",
            "בית שניאורסון",
        ],
        correct_answer=2,
        explanation=(
            "נכון! האדמו\"ר האמצעי רכש בחברון בית כנסת שנודע לימים כבית "
            "הכנסת של האדמו\"ר האמצעי, והוא נחשב לפי מקור הקהילה היהודית "
            "בחברון לנכס החב\"די הראשון בארץ ישראל. "
            "מקור: https://hebron.org.il/en/the-history-of-chabad-in-hebron/"
        ),
    ),

    TriviaQuestion(
        id="chabad-investment-hebron",
        question="איזו עיר בארץ ישראל קיבלה בתקופת האדמו\"ר האמצעי השקעה חב\"דית גדולה במיוחד?",
        answers=[
            "טבריה",
            "צפת",
            "ירושלים",
            "חברון",
        ],
        correct_answer=3,
        explanation=(
            "נכון! לפי ההיסטוריה של חב\"ד בחברון, בתקופה זו חב\"ד השקיעה "
            "בחברון יותר מאשר בכל עיר אחרת בארץ ישראל, וחסידי חב\"ד היו "
            "חלק מרכזי מהקהילה האשכנזית בעיר. "
            "מקור: https://hebron.org.il/en/the-history-of-chabad-in-hebron/"
        ),
    ),

    TriviaQuestion(
        id="menucha-rochel-birth",
        question="מה הקשר המיוחד בין י\"ט כסלו, הרבנית מנוחה רחל וחברון?",
        answers=[
            "היא נולדה בי\"ט כסלו, יום שחרורו של סבה, האדמו\"ר הזקן, ובהמשך הפכה לדמות מרכזית בחב\"ד חברון",
            "היא נפטרה בי\"ט כסלו ונקברה במערת המכפלה",
            "היא הקימה את ישיבת תורת אמת בי\"ט כסלו",
            "היא הגיעה לחברון לראשונה בי\"ט כסלו",
        ],
        correct_answer=0,
        explanation=(
            "נכון! הרבנית מנוחה רחל סלונים נולדה בי\"ט כסלו תקנ\"ט, "
            "באותו יום שבו סבה, האדמו\"ר הזקן, השתחרר ממאסרו. לימים היא "
            "עברה לחברון והייתה במשך עשרות שנים דמות מרכזית בקהילה החב\"דית. "
            "מקור: https://www.chabad.org/theJewishWoman/article_cdo/aid/4276361/jewish/Walking-Between-the-Raindrops-The-Life-of-Rebbetzin-Menucha-Rochel-Slonim.htm"
        ),
    ),

    TriviaQuestion(
        id="menucha-rochel-blessings",
        question="מי נהגו להגיע לרבנית מנוחה רחל אליה לקבלת עצה וברכה?",
        answers=[
            "רק חסידי חב\"ד",
            "רק נשים יהודיות",
            "יהודים וגם שכנים מוסלמים",
            "רק רבני חברון",
        ],
        correct_answer=2,
        explanation=(
            "נכון! לפי המקורות על חייה, הרבנית מנוחה רחל הייתה ידועה כמקור "
            "לעצה וברכה, וגם נשים מוסלמיות מהעיר היו מגיעות אליה. "
            "מקור: https://hebron.org.il/en/memories-of-menucha-rachel-slonim-mother-of-hebron/"
        ),
    ),

    TriviaQuestion(
        id="menucha-rochel-house",
        question="איזה בית מזוהה במסורת החב\"דית עם מגוריה של הרבנית מנוחה רחל בחברון?",
        answers=[
            "בית הדסה",
            "בית רומנו",
            "בית שניאורסון",
            "בית המשקפיים",
        ],
        correct_answer=2,
        explanation=(
            "נכון! בית שניאורסון מזוהה במסורת עם משפחת שניאורסון ועם מגורי "
            "הרבנית מנוחה רחל ובעלה. עם זאת, מחקר היסטורי מאוחר יותר העלה "
            "שייתכן שהמבנה המזוהה כיום בשם זה אינו הבית המקורי שבו התגוררה. "
            "מקור: https://hebron.org.il/en/memories-of-menucha-rachel-slonim-mother-of-hebron/"
        ),
    ),

    TriviaQuestion(
        id="beit-romano",
        question="מי רכש את בית רומנו בחברון עבור חב\"ד?",
        answers=[
            "האדמו\"ר הזקן",
            "האדמו\"ר האמצעי",
            "הצמח צדק",
            "הרבי הרש\"ב",
        ],
        correct_answer=3,
        explanation=(
            "נכון! הרבי הרש\"ב, רבי שלום דובער שניאורסון, רכש את בית רומנו "
            "בשנת תרס\"ט. בהמשך הוא שלח לשם תלמידים מלובביץ', ובמקום הוקמה "
            "ישיבת תורת אמת. "
            "מקור: https://www.chabad.org/news/article_cdo/aid/596836/jewish/Reclaiming-Hebron-History.htm"
        ),
    ),

    TriviaQuestion(
        id="torat-emet",
        question="איזה מוסד חב\"די הוקם בבית רומנו בחברון?",
        answers=[
            "ישיבת תומכי תמימים",
            "ישיבת תורת אמת",
            "כולל חב\"ד",
            "בית הספר למלאכה",
        ],
        correct_answer=1,
        explanation=(
            "נכון! הרבי הרש\"ב הקים בבית רומנו את ישיבת תורת אמת, "
            "והמקום הפך למרכז חשוב של חב\"ד בחברון. "
            "מקור: https://www.chabad.org/library/article_cdo/aid/6390693/jewish/The-Social-Activism-of-the-Fifth-Chabad-Rebbe.htm"
        ),
    ),

    TriviaQuestion(
        id="beit-romano-police",
        question="מה קרה לבית רומנו לאחר שהבריטים השתלטו על ארץ ישראל?",
        answers=[
            "הוא הפך לבית חולים",
            "הוא נהרס",
            "הוא הפך למטה משטרת המנדט הבריטי",
            "הוא הפך למוזיאון",
        ],
        correct_answer=2,
        explanation=(
            "נכון! לאחר שהבריטים השתלטו על הארץ ב-1917, בית רומנו הוסב "
            "למטה משטרת המנדט הבריטי. לאחר מכן שימש גם למטרות אחרות בתקופות "
            "השלטון הירדני והישראלי. "
            "מקור: https://hebron.org.il/en/220-2/"
        ),
    ),

    TriviaQuestion(
        id="rebbes-property-1967",
        question="מה עשה הרבי מליובאוויטש עם זכויות חב\"ד בנכסים בחברון לאחר 1967?",
        answers=[
            "מכר את כל הנכסים",
            "העביר את הזכויות לקהילה היהודית המתחדשת בחברון",
            "השאיר אותם סגורים",
            "העביר אותם לישיבות בירושלים",
        ],
        correct_answer=1,
        explanation=(
            "נכון! לפי מקורות הקהילה בחברון, לאחר מלחמת ששת הימים הרבי "
            "מליובאוויטש העביר את הזכויות בנכסים חב\"דיים שהיו בעיר לקהילה "
            "היהודית המתחדשת, ובירך את המשפחות הצעירות שביקשו לחדש את "
            "החיים היהודיים בעיר. "
            "מקור: https://hebron.org.il/en/766/"
        ),
    ),

    TriviaQuestion(
        id="baruch-nachshon",
        question="איזה חסיד חב\"ד היה מהדמויות המרכזיות בחידוש הקהילה היהודית בחברון לאחר תשכ'ז ?",
        answers=[
            "הרב בערל לאזאר",
            "הרב ברוך נחסון",
            "הרב זלמן גוראריה",
            "הרב יהודה לייב גרונר",
        ],
        correct_answer=1,
        explanation=(
            "נכון! האמן החסידי ברוך נחסון היה מהחלוצים של חידוש הקהילה "
            "היהודית בחברון לאחר מלחמת ששת הימים, וזכה לעידוד ולתמיכה "
            "ממושכת מהרבי מליובאוויטש. "
            "מקור: https://pt.chabad.org/library/article_cdo/aid/5275413/jewish/O-Artista-e-Chassid-Baruch-Nachshon-zl.htm"
        ),
    ),

    TriviaQuestion(
        id="nachshon-brit",
        question="איזה אירוע הקשור לברוך נחסון נחשב לאחד הזרזים לפתיחת מערת המכפלה מחדש ליהודים?",
        answers=[
            "הקמת בית רומנו",
            "ברית המילה של בנו במערת המכפלה",
            "הקמת ישיבת תורת אמת",
            "שחזור בית הכנסת אברהם אבינו",
        ],
        correct_answer=1,
        explanation=(
            "נכון! לאחר שנולד בנו של ברוך נחסון בחברון, הוא ערך את ברית "
            "המילה במערת המכפלה. לפי מקור חב\"די, האירוע נתפס כאחד הגורמים "
            "שסייעו לפתיחת המקום לתפילה יהודית. "
            "מקור: https://www.chabad.org/library/article_cdo/aid/624279/jewish/A-Visit-to-Hebron.htm"
        ),
    ),

    TriviaQuestion(
        id="menucha-rochel-synagogue",
        question="מה מיוחד בבית הכנסת מנוחה רחל בחברון?",
        answers=[
            "זה בית הכנסת שנבנה על ידי הרבי הריי\"צ",
            "זה היה בית הכנסת הראשון שהיה בבעלות חב\"ד בארץ ישראל",
            "זה בית הכנסת היחיד בתוך מערת המכפלה",
            "זה בית הכנסת שנבנה על ידי הצמח צדק בירושלים",
        ],
        correct_answer=1,
        explanation=(
            "נכון! לפי ההיסטוריה של חב\"ד בחברון, בית הכנסת שנקרא כיום "
            "'בית הכנסת מנוחה רחל' היה בית הכנסת החב\"די הראשון בחברון "
            "והנכס הראשון בארץ ישראל שהיה בבעלות חב\"ד. האדמו\"ר האמצעי "
            "עצמו רכש אותו. "
            "מקור: https://hebron.org.il/en/the-history-of-chabad-in-hebron/"
        ),
    ),

    TriviaQuestion(
        id="chabad-hebron-headquarters",
        question="מה היה מעמדה של חברון עבור חסידי חב\"ד בארץ ישראל לפני 150 שנה?",
        answers=[
            "עיר שולית ללא קהילה חב\"דית",
            "המקום שבו התקיימה רק קהילה ספרדית",
            "מרכז חשוב של חב\"ד בארץ ישראל",
            "מקום שאליו הגיעו חסידי חב\"ד רק בחגים",
        ],
        correct_answer=2,
        explanation=(
            "נכון! במשך תקופות משמעותיות במאה ה-19 חברון הייתה מרכז חשוב "
            "של קהילת חב\"ד בארץ ישראל. מקורות חב\"ד מתארים אותה אף כמטה "
            "הקהילה החב\"דית בארץ באותה תקופה. "
            "מקור: https://www.chabad.org/library/article_cdo/aid/624279/jewish/A-Visit-to-Hebron.htm"
        ),
    ),

    TriviaQuestion(
        id="chabad-hebron-headquarters",
        question="אם הגעתם עד לפה אני רוצה לספר לכם שחברון היא מפוצצת בהיסטוריה וסיפורים מיוחדים לא רק על חב\"ד. רק חפשו באינטרנט או פשוט תשאלו את השווער שלי ",
        answers=[
            "",
            "",
            "",
            "",

        ],
        correct_answer=0,
        explanation=(
            ""
        ),
    ),

]


def public_questions() -> list[dict]:
    """מחזיר שאלות ללא התשובות הנכונות."""
    return [
        {"id": item.id, "question": item.question, "answers": item.answers}
        for item in TRIVIA_QUESTIONS
    ]


def check_answer(question_id: str, selected_answer: int) -> dict | None:
    question = next(
        (item for item in TRIVIA_QUESTIONS if item.id == question_id),
        None,
    )

    if question is None:
        return None

    return {
        "is_correct": selected_answer == question.correct_answer,
        "correct_answer": question.correct_answer,
        "explanation": question.explanation,
    }
