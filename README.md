# A Model for Coreference in Hebrew


האיגוד הישראלי לטכנולוגיות שפת אנוש
الرابطة الإسرائيلية لتكنولوجيا اللغة البشرية

The Israeli Association of Human Language Technologies
https://www.iahlt.org


This project includes a model trained for the coreference task in Hebrew, using the dataset available at [this repository](https://github.com/IAHLT/coref).

## Install
To install and use the model, please follow the steps described below:

1. Clone the repo.
2. pip install it.
3. Download the models: https://drive.google.com/file/d/1jNQ3LfjQ0dZp1B3N54KLFy0Qw9-DN-t3/view?usp=drive_link
4. Extract the directory (denoted as $PATH_TO_MODELS_DIR).

## Example
```
import os
from iahlt_coref_he.coref_pipeline import CorefPipeline

text = '''
מייקל ג'פרי ג'ורדן (באנגלית: Michael Jeffrey Jordan; נולד ב-17 בפברואר 1963) הוא כדורסלן עבר אמריקאי, ששיחק בעמדת הקלע. ג'ורדן, אשר ניצב במקום החמישי ברשימת הקלעים המובילים בתולדות ה-NBA, נחשב בעיני רבים לכדורסלן הטוב ביותר בהיסטוריה,[1][2][3] וזכה להצלחה רבה שסייעה לפרסומה של ליגת ה-NBA ברחבי העולם בשנות ה-80 וה-90 של המאה ה-20. הצטרף לשיקגו בולס בעונת 1984/1985, ותוך זמן קצר הפך לאחד הכוכבים הבולטים בליגת ה-NBA. יכולותיו ככדורסלן וכאתלט זיכו אותו בכינויים "אייר ג'ורדן", "הוד אוויריותו", "ישו השחור" ו-"אלוהים".

במהלך הקריירה ג'ורדן זכה במגוון תארים שונים, בין השאר, שש פעמים באליפות ה-NBA במדי שיקגו בולס, ופעמיים במדליית זהב אולימפית במדי נבחרת ארצות הברית. הישגיו האישיים כוללים חמש זכיות בתואר MVP של העונה הסדירה, עשר פעמים חבר בחמישיית העונה, תשע פעמים חבר בחמישיית ההגנה, 14 השתתפויות במשחק האולסטאר, שלוש זכיות בתואר ה-MVP של משחק האולסטאר, שלוש זכיות בתואר מלך החטיפות, שש זכיות בתואר ה-MVP של סדרת הגמר, וזכייה בתואר שחקן ההגנה של העונה ב-1988.[4] בנוסף, מחזיק ג'ורדן בשיא ממוצע הנקודות לקריירה ב-NBA עם 30.12 נקודות למשחק, ובשיא של 33.4 נקודות בממוצע למשחק פלייאוף. בשנת 2015, לאור הישגיו יוצאי הדופן ותרומתו לענף הכדורסל, צורף ג'ורדן להיכל התהילה של פיב"א, וב-2016 העניק לו נשיא ארצות הברית ברק אובמה את מדליית החירות הנשיאותית, עיטור הכבוד הגבוה ביותר של ארצות הברית.[5]-NBA הראשון שהפך לבעלים של קבוצה בליגה, וכן לבעלי הקבוצה היחידי בליגה ממוצא אפרו-אמריקאי. במהלך שנותיו של ג'ורדן כבעלי הקבוצה, ההורנטס לא זכו להישגים מקצועיים משמעותיים, והגיעו רק שלוש פעמים למעמד הפלייאוף.[6] אף על פי כן הצליח ג'ורדן ב-2023 למכור את רוב זכויות הבעלות שלו בקבוצה לפי שווי של כשלושה מיליארד דולר.[7]
'''.strip()

tokenizer_model_path = os.path.join($PATH_TO_MODELS_DIR, 'tokenizer.udpipe')
coref_model_path = os.path.join($PATH_TO_MODELS_DIR, 'coref_model')

coref = CorefPipeline(tokenizer_model_path=tokenizer_model_path, coref_model_path=coref_model_path)
res = coref.predict([text])
print(res)
```
